# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import today

class Module(Document):
    def autoname(self):
        self.name = self.module_code

            

	

   