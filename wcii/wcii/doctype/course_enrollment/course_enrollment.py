# Copyright (c) 2023, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class CourseEnrollment(Document):
    def on_submit(self):
        self.add_course_to_student()
        # frappe.msgprint(f"Course {self.course} has been added to students")
    
    # Add course to students after enrollment
    def add_course_to_student(self):
        enrolled_students = []
        course = frappe.get_doc("Course", self.course)
        for student in self.get("students"):
            student_doc = frappe.get_doc("Student", student.student)
            # Check if student is already enrolled
            if course.name in [course.course for course in student_doc.get("courses")]:
                enrolled_students.append(student.student_id)
                continue
                
            student_doc.append("courses", {
                "course": self.course,
                "course_name": course.course_name,
                # "enrollment_date": today()
            })
            # Get and add modules
            modules = course.get("modules")
            for module in modules:
                if module.module not in student_doc.get("modules"):
                    student.append("modules", {
                        "module": module.module,
                        "module_name": module.module_name,
                    })
            student.save(ignore_permissions=True)
        
        if enrolled_students:
            frappe.msgprint(f"Students {', '.join(enrolled_students)} already enrolled to this course")
