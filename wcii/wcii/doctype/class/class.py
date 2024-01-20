# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Class(Document):
    pass
	# def on_submit(self):
	# 	self.get_students()
	
	# def get_students(self):
	# 	students = frappe.db.get_all(
	# 		"Student",
	# 		filters={"courses.course":self.course},
	# 		fields=["*"]
	# 	)
	# 	for student in students:
	# 		self.append("students", {
	# 		   "student":student.student,
	# 		   "student_name":student.student_name
	# 		   })