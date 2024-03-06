import frappe
from frappe.model.document import Document
from frappe.utils import now
#import build
from googleapiclient.discovery import build
from google.oauth2 import service_account



# def overview():
#     total_students = frappe.db.count("Student")
#     total_courses = frappe.db.count("Course")
#     total_modules = frappe.db.count("Module")

#     doc = frappe.get_doc("Overview")

#     doc.db.set_value("total_students", total_students)
#     doc.db.set_value("total_courses", total_courses)
#     doc.db.set_value("total_modules", total_modules)
@frappe.whitelist()
def get_class_students(class_name=""):
    if not class_name or not frappe.db.exists('Class', class_name, cache=True): return []
    
    try:
        classdoc=frappe.get_doc('Class', class_name)
        
        return [s for s in classdoc.students]
    except: 
        return []

@frappe.whitelist()
def service_account():
    service_account_info = {
        "type": frappe.db.get_single_value("E-Book Settings", "type"),
        "project_id": frappe.db.get_single_value("E-Book Settings", "project_id"),
        "private_key_id": frappe.db.get_single_value("E-Book Settings", "private_key_id"),
        "private_key": frappe.db.get_single_value("E-Book Settings", "private_key"),
        "client_email": frappe.db.get_single_value("E-Book Settings", "client_email"),
        "client_id": frappe.db.get_single_value("E-Book Settings", "client_id"),
        "auth_uri": frappe.db.get_single_value("E-Book Settings", "auth_uri"),
        "token_uri": frappe.db.get_single_value("E-Book Settings", "token_uri"),
        "auth_provider_x509_cert_url": frappe.db.get_single_value("E-Book Settings", "auth_provider_x509_cert_url"),
        "client_x509_cert_url": frappe.db.get_single_value("E-Book Settings", "client_x509_cert_url"),
        "universe_domain": frappe.db.get_single_value("E-Book Settings", "universe_domain")
    }
    return service_account_info

credentials = service_account()
drive_service = build('drive', 'v3', credentials=credentials)

@frappe.whitelist()
def last_fetch():
    return frappe.db.get_single_value("E-Book Settings", "last_fetch_time")

@frappe.whitelist()
def set_last_fetch():
    frappe.db.set_value("E-Book Settings", None, "last_fetch_time", now())
    frappe.db.commit()

@frappe.whitelist()
def get_files(next_page_token=None, modified_time='2012-06-04T12:00:00'):
    try:
        last_fetch_time = frappe.db.get_single_value("E-Book Settings", "last_fetch_time")
        if last_fetch_time:
            modified_time = last_fetch_time
    except:
        pass

    diff = now() - now_datetime(modified_time)
    if diff.seconds < 1800:
        return []

    try:
        service = build('drive', 'v3', credentials=get_credentials())

        results = service.files().list(
            pageSize=1000,
            pageToken=next_page_token,
            q=f"modifiedTime > '{modified_time}' and (mimeType='application/pdf' or mimeType='application/vnd.google-apps.folder')",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime, parents)"
        ).execute()

        files = results.get('files', [])
        next_page_token = results.get('nextPageToken')

        if next_page_token:
            files.extend(get_files(next_page_token=next_page_token, modified_time=modified_time))

        frappe.db.set_value("E-Book Settings", "E-Book Settings", "last_fetch_time", now())
        frappe.db.commit()

        return files
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
        return []

def get_credentials():
    service_account_info = {
        "type": frappe.db.get_single_value("E-Book Settings", "type"),
        "project_id": frappe.db.get_single_value("E-Book Settings", "project_id"),
        "private_key_id": frappe.db.get_single_value("E-Book Settings", "private_key_id"),
        "private_key": frappe.db.get_single_value("E-Book Settings", "private_key"),
        "client_email": frappe.db.get_single_value("E-Book Settings", "client_email"),
        "client_id": frappe.db.get_single_value("E-Book Settings", "client_id"),
        "auth_uri": frappe.db.get_single_value("E-Book Settings", "auth_url"),
        "token_uri": frappe.db.get_single_value("E-Book Settings", "token_url"),
        "auth_provider_x509_cert_url": frappe.db.get_single_value("E-Book Settings", "auth_provider_x509_cert_url"),
        "client_x509_cert_url": frappe.db.get_single_value("E-Book Settings", "client_x509_cert_url"),
        "universe_domain": frappe.db.get_single_value("E-Book Settings", "universe_domain")
    }

    from google.oauth2 import service_account

    credentials = service_account.Credentials.from_service_account_info(service_account_info)

    return credentials

    try:
        last_fetch_time = frappe.db.get_single_value("E-Book Settings", "last_fetch_time")
        if last_fetch_time:
            modified_time = last_fetch_time
    except:
        pass

    diff = now() - now_datetime(modified_time)
    if diff.seconds < 3600:
        return []

    try:
        res = frappe.get_all("E-Book", filters={"modified": [">", modified_time]}, fields=["name", "modified"],
                                limit=1000, start=next_page_token)
        files = res if res else[]
        if files and res.next_page_token:
            files.extend(get_files(next_page_token=res.next_page_token, modified_time=modified_time))
        frappe.db.set_value("E-Book Settings", None, "last_fetch_time", now())
        frappe.db.commit()
        return files
    except Exception as e:
        frappe.msgprint(f"Error: {e}")
        return []

@frappe.whitelist()
def prepare_folder(folder, all_folders):
    tags = []
    for f in folder.parents:
        parent = next((x for x in all_folders if x.id == f), None)
        if parent:
            x = prepare_folder(parent, all_folders)
            tags.extend(x['tags'])
        else:
            tags = tags[:-1]

    return {
        'name': folder.name,
        'id': folder.id,
        'tags': list(set(tags + [folder.name.lower()] if folder.name else []))
    }

def prepare_drive_files(modified_time=None):
    global is_in_progress
    if is_in_progress:
        return
    is_in_progress = True
    category_set = set()
    files = get_files(modified_time=modified_time)
    
    for f in files:
        if f.get('mimeType') == 'application/pdf':
            folder = next((f2 for f2 in files if f2.get('id') == f.get('parents')[0]), None)
            category = (folder.get('name').upper().replace('-', ' ') if folder else 'Uncategorized').strip()