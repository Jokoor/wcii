# Copyright (c) 2019, Frappe Technologies and contributors
# License: MIT. See LICENSE

import os
from urllib.parse import quote

from apiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

import frappe
from frappe import _
from frappe.integrations.google_oauth import GoogleOAuth
from frappe.integrations.offsite_backup_utils import (
	get_latest_backup_file,
	send_email,
	validate_file_size,
)
from frappe.model.document import Document
from frappe.utils import get_backups_path, get_bench_path
from frappe.utils.background_jobs import enqueue
from frappe.utils.backups import new_backup


def after_install():
	frappe.db.set_value("Wensite Settings", None, "home_page", "home")


@frappe.whitelist(methods=["POST"])
def authorize_access(reauthorize=False, code=None):
	"""
	If no Authorization code get it from Google and then request for Refresh Token.
	Google Contact Name is set to flags to set_value after Authorization Code is obtained.
	"""

	oauth_code = (
		frappe.db.get_single_value("Google Drive", "authorization_code") if not code else code
	)
	oauth_obj = GoogleOAuth("drive")

	if not oauth_code or reauthorize:
		if reauthorize:
			frappe.db.set_single_value("Google Drive", "backup_folder_id", "")
		return oauth_obj.get_authentication_url(
			{
				"redirect": f"/app/Form/{quote('Google Drive')}",
			},
		)

	r = oauth_obj.authorize(oauth_code)
	frappe.db.set_single_value(
		"Google Drive",
		{"authorization_code": oauth_code, "refresh_token": r.get("refresh_token")},
	)


def get_google_drive_object():
	"""
	Returns an object of Google Drive.
	"""
	account = frappe.get_doc("Google Drive")
	oauth_obj = GoogleOAuth("drive")

	google_drive = oauth_obj.get_google_service_object(
		account.get_access_token(),
		account.get_password(fieldname="indexing_refresh_token", raise_exception=False),
	)

	return google_drive, account






#get folder
@frappe.whitelist()
def get_folder(google_drive, folder_id):
    folder = google_drive.files().get(fileId=folder_id, fields='name').execute()
    return folder

#geta all the pdf 
@frappe.whitelist()
def get_pdf():
    google_drive, account = get_google_drive_object()
    next_page_token = None
    while True:
        files = google_drive.files().list(q="mimeType='application/pdf'", pageToken=next_page_token).execute()
        next_page_token = files.get('nextPageToken')
        items = files.get('files', [])
        for i, f in enumerate(items):
            count = 1
            file = google_drive.files().get(fileId=f.get('id'), fields='thumbnailLink, id, name, webViewLink, parents').execute()
            if not frappe.db.exists('E-Books', file.get('id')):
                doc = frappe.new_doc('E-Books')
                doc.file_name = file.get('name')
                doc.id = file.get('id')
                doc.image = file.get('thumbnailLink')
                doc.web_view_link = file.get('webViewLink')
                parent = file.get('parents')
                if parent:
                    category = get_folder(google_drive, parent[0]).get('name')
                    if not frappe.db.exists('E-Book Category', parent[0]):
                        category_doc = frappe.new_doc('E-Book Category')
                        category_doc.category_name = category
                        category_doc.category_id = parent[0]
                        category_doc.insert(ignore_permissions=True)
                    doc.category = parent[0]
                    doc.category_name = category
                doc.thumbnail_link = file.get('thumbnailLink')
                doc.insert(ignore_permissions=True)
            frappe.publish_progress(int((i/len(items)) * 100), title='Fetching E-Books', doctype='E-Books', description='Fetching E-Books')
        if not next_page_token:
            break  # Exit the loop if there are no more pages
    return next_page_token
