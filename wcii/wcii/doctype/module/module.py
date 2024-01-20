# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Module(Document):
	def after_insert(self):
         modules = frappe.db.count("Module")
         overview = frappe.get_doc("Overview")
         overview.total_modules = modules
         overview.save()
         frappe.db.commit()
