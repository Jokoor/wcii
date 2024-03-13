# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

from frappe import _
import frappe
from frappe.website.website_generator import WebsiteGenerator


class Assignment(WebsiteGenerator):
    def validate(self):
            self.route = self.name
            self.published = 1

    def get_context(self, context):
        context.no_cache = 1
        context.assignment = self
        context.title = self.assignment_name
        show_sidebar = True
        return context
        