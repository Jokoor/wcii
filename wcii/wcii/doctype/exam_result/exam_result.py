# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ExamResult(Document):
	def validate(self):
		self.update_student_report()
	def after_insert(self):
		self.get_students()
	def on_update(self):
		pass		

	

	
	#get students from a particular class
	def get_students(self):
		class_name = frappe.get_doc('Class', self.class_name)
		students = class_name.get('students')
		for student in students:
			self.append('students', {
				'student': student.student, 
				'student_name': student.student_name,
				'mark': '0'
				})
		
	# update the student report doctype
	def update_student_report(self):
		#update the student report doctype
		class_name = frappe.get_doc('Class', self.class_name)
		for student in self.students:
			if frappe.db.exists('Student Report', student.student):
				student_report = frappe.get_doc('Student Report', student.student)
				#check if the module already exists
				for module in student_report.get('results'):
					if module.module == self.module:
						module.exam = student.mark
						student_report.save()
						break
				else:
					student_report.append('results', {
						'module': self.module,
						'module_name': frappe.db.get_value('Class', self.class_name, 'module_name'),
						'academic_year': class_name.academic_year,
						'academic_term': class_name.academic_term,
						'exam': student.mark,
						
						
					})
					student_report.save()