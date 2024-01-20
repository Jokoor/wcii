# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Fees(Document):

	def before_naming(self):
		if self.name:
			frappe.throw("Fee can only be saved onced")
			
	def after_insert(self):
		self.outstanding_amount = self.total_amount
		self.status='UNPAID'
		self.save()
		frappe.db.commit()