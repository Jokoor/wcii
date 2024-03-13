# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Fees(Document):
	def validate(self):
		self.outstanding_amount = self.total_amount
	def on_submit(self):
		frappe.db.set_value("Fees", self.name, "status", "Unpaid")

		student = frappe.get_doc("Student", self.student)
		student.append("fees", {
			"fee": self.name,
			"amount": self.total_amount,
			"fee_status": "Unpaid",
			"fee_type": self.fee_type,
		})
		student.save(ignore_permissions=True)
		frappe.msgprint("Fee added to Student")
