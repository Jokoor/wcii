# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Payments(Document):
	def validate(self):
		fee_doc = frappe.get_doc("Fees", self.fee)
		if fee_doc.outstanding_amount <= 0:
			frappe.throw("There is no outstanding amount for this Fee")

	def before_naming(self):
		if self.name:
			frappe.throw("Payment can only be saved onced")

	def before_save(self):
		fee_doc = frappe.get_doc("Fees", self.fee)
		fee_doc.paid_amount = fee_doc.paid_amount + self.paid_amount
		fee_doc.outstanding_amount = fee_doc.total_amount - fee_doc.paid_amount
		if fee_doc.outstanding_amount < 0:
			frappe.throw(f"You over paid the fee by {abs(fee_doc.outstanding_amount)}")
		self.outstanding_amount=fee_doc.outstanding_amount
		self.change_status(fee_doc)
		fee_doc.save()
		frappe.db.commit()

	def change_status(self, fee_doc):
		if fee_doc.outstanding_amount == 0:
			fee_doc.status = "PAID"
		elif fee_doc.outstanding_amount > 0:
			fee_doc.status = "PARTIALLY-PAID"