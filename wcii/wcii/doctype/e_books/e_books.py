# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EBooks(Document):
	def autoname(self):
		self.name = self.file_name