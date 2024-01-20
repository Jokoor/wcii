# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Course(Document):
	
	def after_insert(self):
         courses = frappe.db.count("Course")
         overview = frappe.get_doc("Overview")
         overview.total_courses = courses
         overview.save()
         frappe.db.commit()
