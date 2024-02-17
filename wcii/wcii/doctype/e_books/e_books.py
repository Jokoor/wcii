# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

from urllib.request import urlopen
import frappe
from frappe.model.document import Document
import requests
class EBooks(Document):
	def validate(self):
		kwargs={
			"thumbnail_link": self.thumbnail_link
		}
		self.get_book_thumbnail(**kwargs)	
#download the file using urrlib
	def get_book_thumbnail(self, **kwargs):
			data = frappe._dict(kwargs)
			try:
				f = urlopen(data.get("thumbnail_link"))
				myfile = f.read()
				_file  = frappe.get_doc({
					"doctype": "File",
					"file_name": self.file_name,
					"is_private": 0,
					"content": myfile
				})
			except Exception as e:
				frappe.log_error(frappe.get_traceback())
				
			