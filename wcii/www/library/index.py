#get_contex
import frappe

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = True

    return context