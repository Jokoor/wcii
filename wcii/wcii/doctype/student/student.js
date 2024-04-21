// Copyright (c) 2023, Royalsmb and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {

		//hide the student enable check if document is new
		if (frm.doc.__islocal) {
			frm.toggle_display('enabled', false);
		}


		//add custom button to enroll student
		frm.add_custom_button('Enroll Student', () => {
			//open modal to select course
			frappe.prompt([
				{'fieldname': 'course', 'fieldtype': 'Link', 'label': 'Course', 'options': 'Course', 'reqd': 1},
			], (values) => {	
				frm.call({
					method: 'enroll_student',
					args: {
						student: frm.doc.name,
						course: values.course
					},
					callback: (r) => {
						if (r.message) {
							//refresh the form
							frm.doc.refresh();
						}
					}

				});
				});


			
		}
		);




	},
	first_name: function(frm) {
		full_name(frm);
		email(frm);

	},
	middle_name: function(frm) {
		full_name(frm);
	},
	last_name: function(frm) {
		full_name(frm);
		email(frm);
	},
	
});

function full_name(frm) {
		//set the full name from the first name, middle name and last name
		frm.set_value('full_name', `${frm.doc.first_name || ''} ${frm.doc.middle_name || ''} ${frm.doc.last_name || ''}`);	
}

