# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Payments(Document):
	def validate(self):
		self.outstanding_amount = self.fee_amount - self.paid_amount
		fee_doc = frappe.get_doc("Fees", self.fee)
		if self.paid_amount <= 0:
			frappe.throw("You cannot pay less than 0")
		if self.paid_amount > fee_doc.outstanding_amount:
			frappe.throw(f"You cannot pay more than {fee_doc.outstanding_amount}")


	def on_submit(self):
		fee_doc = frappe.get_doc("Fees", self.fee)
		student = frappe.get_doc("Student", fee_doc.student)
		frappe.db.set_value("Fees", self.fee, "paid_amount", fee_doc.paid_amount + self.paid_amount)
		frappe.db.set_value("Fees", self.fee, "outstanding_amount", fee_doc.outstanding_amount - self.paid_amount)
		if self.outstanding_amount == 0:
			frappe.db.set_value("Fees", self.fee, "status", "Paid")
			for fee in student.get("fees"):
				if fee.fee == fee_doc.name:
					fee.fee_status = "Paid"
					student.save()
	
		elif self.outstanding_amount > 0:
			frappe.db.set_value("Fees", self.fee, "status", "Partly-paid")
			for fee in student.get("fees"):
				if fee.fee == fee_doc.name:
					fee.fee_status = "Partly-paid"
					student.save()

	