// Copyright (c) 2020, Parag and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Membership', {
	 before_save: function(frm) {
		 if(frm.doc.from_date>=frm.doc.to_date){
			 frappe.throw("To Date must be greater than From Date")
		 }
	 }
	 
	});
