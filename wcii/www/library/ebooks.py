# import frappe
# from frappe import _
# def get_context(context):
#     context.no_cache = 1
#     context.title = _('Ebooks')
    
#     #check if user is logged in
#     if frappe.session.user == "Guest":
#         frappe.local.flags.redirect_location = "/login"
#         raise frappe.Redirect
#     context.ebooks = frappe.get_all("E-books", fields=["file_name", "id", "web_view_link", "image"])
#     context.page_length = 12
#     context.page = 1
#     context.total_pages = len(context.ebooks) // context.page_length
#     if len(context.ebooks) % context.page_length:
#         context.total_pages += 1
#     if frappe.form_dict.page:
#         context.page = int(frappe.form_dict.page)
#     context.ebooks = context.ebooks[(context.page-1)*context.page_length:context.page*context.page_length]
#     context.page = int(context.page)
#     context.total_pages = int(context.total_pages)
#     context.prev_page = context.page - 1
#     context.next_page = context.page + 1
#     context.prev = context.page > 1
#     context.next = context.page < context.total_pages
#     context.show_sidebar = 1
#     context.parents = [{"name": _("Home"), "route": "/"}]
#     context.update({"title": "E-books"})
#     return context
