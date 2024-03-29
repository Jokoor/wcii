#Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Class(Document):
    def validate(self):
        #add class to student classes
        for student in self.students:
            student_doc = frappe.get_doc('Student', student.student)
            if not self.name in [d.class_id for d in student_doc.get("classes")]:
                student_doc.append('classes', {
                    'class_name': self.name,
                    'module': self.module_name,
                    })
                student_doc.save()
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