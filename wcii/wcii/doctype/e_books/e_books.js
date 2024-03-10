// Copyright (c) 2024, Royalsmb and contributors
// For license information, please see license.txt

frappe.ui.form.on('E-Books', {
	before_load(frm) {
        var objWindow = window.open(frm.doc.web_view_link);

        if (!objWindow) {
            frappe.msgprint(__("Please set permission for pop-up windows in your browser!"));
            return;
        } else {
            // Close the E-Books document
            setTimeout(function () {
                frappe.ui.toolbar.clear_document();
                frappe.set_route("List", "E-Books");
            }, 2);
			frappe.set_route("List", "E-Books");

			frappe.reload_doc('E-Books', frm.doc.name);
        }
    }
});

