# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
    def before_save(self):
        fullname = (
            f'{self.first_name or ""} {self.middle_name or ""} {self.last_name or ""}'
        )
        self.fullname = " ".join([i for i in fullname.split(" ") if i])

    def after_insert(self):
        self.create_user()
        self.create_student_report()
        students = frappe.db.count("Student")
        overview = frappe.get_doc("Overview")
        overview.total_students = students
        overview.save()
        frappe.db.commit()

    def validate(self):
        # self.get_module()
        pass

    def get_module(self):
        # Clear existing courses in the child table

        course_doc = frappe.get_doc("Course", self.course)
        for module in course_doc.module:
            self.append(
                "modules", {"module": module.module, "module_name": module.module_name}
            )

    # create student report doctype
    def create_student_report(self):
        # create student report doctype
        student_report = frappe.get_doc(
            {
                "doctype": "Student Report",
                "student": self.name,
                "student_name": self.first_name,
            }
        )
        student_report.insert()
        ignore_permissions = True

    #create user for the student
    def create_user(self):
        if not frappe.db.exists("User", self.email_address):
            student = frappe.get_doc({
                'doctype': 'User',
                'first_name': self.first_name,
                'last_name': self.last_name,
                'gender': self.gender,
                'email':self.email_address,
                'send_welcome_email': 0,
                'user_type': 'Website User'

            })
            student.add_roles('Student')
            student.save(ignore_permissions=True)
