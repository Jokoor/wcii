import frappe
from frappe.model.document import Document


# def overview():
#     total_students = frappe.db.count("Student")
#     total_courses = frappe.db.count("Course")
#     total_modules = frappe.db.count("Module")

#     doc = frappe.get_doc("Overview")

#     doc.db.set_value("total_students", total_students)
#     doc.db.set_value("total_courses", total_courses)
#     doc.db.set_value("total_modules", total_modules)
@frappe.whitelist()
def get_class_students(class_name=""):
    if not class_name or not frappe.db.exists('Class', class_name, cache=True): return []
    
    try:
        classdoc=frappe.get_doc('Class', class_name)
        
        return [s for s in classdoc.students]
    except: 
        return []
    


