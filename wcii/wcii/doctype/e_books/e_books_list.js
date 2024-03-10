
frappe.listview_settings['E-Books'] = {
   refresh: function(listview) {
       listview.page.add_inner_button("Fetch Books", function() {
            frappe.call({
                method: "wcii.api.get_pdf",
                args: {},
                callback: function(r) {
                    if(r.message) {
                        frappe.msgprint("Books Fetched Successfully");
                        listview.refresh();
                        console.log(r.message);
                    }
                }
            });
       });;
   },
};