# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class AcademicTerm(Document):
	def validate(self):
		acc_year = frappe.get_doc("Academic Year", self.academic_year)
		if getdate(self.start_date) < getdate(acc_year.start_date) or getdate(self.end_date) > getdate(acc_year.end_date):
			frappe.throw("Start Date and End Date must be within the Academic Year")
	def autoname(self):
		self.name = f'{self.term_name} | {self.academic_year}'
		