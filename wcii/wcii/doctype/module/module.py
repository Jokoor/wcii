# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Module(Document):
	def after_insert(self):
         modules = frappe.db.count("Module")
         overview = frappe.get_doc("Overview")
         overview.total_modules = modules
         overview.save()
         frappe.db.commit()

    #update the resource of the various classes create from the module
    # def on_update(self):
    #     classes = frappe.get_all("Class", filters={"module": self.name})
    #     for class_ in classes:
    #         class_doc = frappe.get_doc("Class", class_.name)
    #         if class_doc.resources and self.resources:
    #             self.clear_resources(class_doc.name)
    #             for resource in self.resources:
    #                 class_doc.append('resources', {
    #                     'file_path': resource.file_path,
    #                     'file_name': resource.file_name,
    #                     'file_type': resource.file_type,
    #                     'file_size': resource.file_size,
    #                     'file_id': resource.file_id
    #                 })
    #                 class_doc.save()
    # def clear_resources(doc):
    #     class_doc = frappe.get_doc("Class", doc)
    #     class_doc.resources = []
    #     class_doc.save()
