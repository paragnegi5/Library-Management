// Copyright (c) 2020, Parag and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Management Settings', {
	before_save: function(frm) {
		if (frm.doc.loan_period<30){
			frappe.throw("Loan period must be greater than or equal to 30 days")
		}
	 }
});
