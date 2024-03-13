// Copyright (c) 2023, Royalsmb and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fees', {
	//set indicator
	refresh: function(frm) {
		frm.set_indicator_formatter('fee_status', (doc) => {
			if(doc.status==="Submitted") {
				return [__("Unpaid"), "orange", "status,=,Unpaid"];
			} else {
				return [__(doc.status), {
					"Draft": "red",
					"Unpaid": "orange",
					"Partly-paid": "yellow",
					"Paid": "green",
					"Cancelled": "red"
				}[doc.status], "status,=," + doc.status];
			}
		}
		);
	},
});
