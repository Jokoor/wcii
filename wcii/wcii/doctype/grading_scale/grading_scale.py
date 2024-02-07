# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GradingScale(Document):
    #validate if the the grade for 0 is peresent
		def validate(self):
			if self.get('grades'):
				grade_0 = False
				for grade in self.get('grades'):
					if grade.min_percentage == '0':
						grade_0 = True
				if not grade_0:
					frappe.throw(("Grade for 0 is mandatory"))