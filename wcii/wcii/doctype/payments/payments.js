// Copyright (c) 2023, Royalsmb and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payments', {
	//qurey the only the fees that are not paid and not draft
	refresh: function(frm) {
		frm.set_query('fee', () => {
			return {
				filters: [
					['Fees', 'status', 'in', ['Partly-paid', 'Unpaid', 'Overdue']]
				]
			};
		});
	},
});
