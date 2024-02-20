#Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Class(Document):

    # append the resource if the class is saved

    def after_insert(self):
        self.get_resource()

    # get resource from the module of the class

    def get_resource(self):
        module_resources = frappe.get_doc('Module',
                self.module).get('resources')
        if module_resources:
            for resource in module_resources:
                self.append('resources', {
                    'file_path': resource.file_path,
                    'file_name': resource.file_name,
                    'file_type': resource.file_type,
                    'file_size': resource.file_size,
                    'file_id': resource.file_id,
                    })
            self.save()