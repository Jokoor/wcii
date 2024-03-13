# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
    def validate(self):
        self.student_id = self.name
        frappe.db.set_value("User", self.email_address, "username", self.student_id)
    
    def after_insert(self):
        self.create_user()
        self.send_email()
        self.create_student_report()
        
    #set auto name for student
    def autoname(self):
        prefix = frappe.db.get_single_value("School Settings", "institution_code_prefix")
        register_no_start_from = frappe.db.get_single_value("School Settings", "register_no_start_from")
        register_digit = frappe.db.get_single_value("School Settings", "register_no_digit")
        #get the last student
        zeros = "0" * (int(register_digit) -1)
        last_student = frappe.get_last_doc("Student")
        if last_student:
            last_student = int(last_student.student_id.split("-")[-1])
            self.student_id = f"{prefix}-{zeros}{last_student + 1}"
            self.name = self.student_id
        else:
            self.student_id = f"{prefix}-{zeros}{register_no_start_from}"
            self.name = self.student_id



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
                'username': self.student_id,
                'user_type': 'Website User'

            })
            student.add_roles('Student')
            student.save(ignore_permissions=True)
    
    #delete user after student is delted
    def after_delete(self):
        frappe.delete_doc("User", self.email_address)
    
    def send_email(self):
        frappe.sendmail(recipients=self.email_address,
                    subject="Welcome To Wcii",
                    message= "You have successfully been registered to wcii"
    )
@frappe.whitelist()
def enroll_student(student, course):
    student = frappe.get_doc("Student", student)
    course_doc = frappe.get_doc("Course", course)
   
    #check if student is already enrolled
  
    if course in [course.course for course in student.get("courses")]:
        frappe.throw(f"{student.full_name}  is already enrolled to {course_doc.course_name}")
    else:
        student.append("courses",
            {"course": course_doc.name,
            "course_name": course_doc.course_name
            })

        #append modules to student
        if course_doc.get("modules"):
            for module in course_doc.get("modules"):
                #skip if module is already enrolled
    
                if module.module not in [module.module for module in student.get("modules")]:
                    student.append("modules", {
                    "module": module.module,
                    "module_name": module.module_name
                    })
        student.save(ignore_permissions=True)
        frappe.msgprint(f"{student.full_name} has been enrolled to {course_doc.course_name} successfully")
            