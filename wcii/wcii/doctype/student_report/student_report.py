# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentReport(Document):
	# def on_update(self):
		
	# 	self.calculate_total_marks()

	def on_change(self):
		self.student_grade()
		

	def student_grade(self):
		#calculate the grade of a student
		grades = frappe.get_doc('Grading Scale').get('grades')
		for result in self.results:
			result.total_marks = result.exam + result.assessment
			result.save()
			for grade in grades:
				if int(result.total_marks) >= int(grade.min_percentage) and int(result.total_marks) <= int(grade.max_percentage):
					result.grade = grade.grade_name
					result
					break

			
			