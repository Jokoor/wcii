#get_contex
import frappe

def get_context(context):
    # return login use
    context.no_cache = 1
    context.show_sidebar = True

    return context