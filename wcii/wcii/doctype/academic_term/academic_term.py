# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class AcademicTerm(Document):
	def autoname(self):
		self.name=f'{self.term_name} | {self.academic_year}'