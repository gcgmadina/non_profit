// Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Donation', {
	refresh: function(frm) {
		if (frm.doc.docstatus === 1 && !frm.doc.paid && frm.doc.item_type != 'Barang') {
			frm.add_custom_button(__('Create Payment Entry'), function() {
				frm.events.make_payment_entry(frm);
			});
		}

		frm.set_query('donation_event', function() {		
			return {
				filters: {
					"event_category": "Donation"
				}
			}
		});
	},

	make_payment_entry: function(frm) {
		return frappe.call({
			method: 'non_profit.non_profit.custom_doctype.payment_entry.get_donation_payment_entry',
			args: {
				'dt': frm.doc.doctype,
				'dn': frm.doc.name
			},
			callback: function(r) {
				var doc = frappe.model.sync(r.message);
				frappe.set_route('Form', doc[0].doctype, doc[0].name);
			}
		});
	},

	donation_type: function(frm) {
		// frm.doc.item_type = 'Uang';
		frm.doc.item_name = null;
		frm.doc.item_amount = null;
		frm.doc.paid = 0;
		frm.doc.amount = null;
		frm.doc.mode_of_payment = null;
		frm.doc.donation_event = null;

		if (frm.doc.donation_type == 'Infaq' || frm.doc.donation_type == 'Zakat Mal' || frm.doc.donation_type == 'Specific Donation') {
			set_field_options("item_type", ["Uang"])
		} else if (frm.doc.donation_type == 'Zakat Fitrah' || frm.doc.donation_type == 'Fidyah' || frm.doc.donation_type == 'Kafarat' || frm.doc.donation_type == 'Wakaf') {
			set_field_options("item_type", ["Uang", "Barang"])
		} else if (frm.doc.donation_type == 'Hibah') {
			set_field_options("item_type", ["Barang"])
		}
	},

	donor: function(frm) {
		if (frm.doc.donor != "hambaa@email.com"){
			frm.events.get_fullname(frm);
		}
		// frm.events.get_fullname(frm);
		// if (frm.doc.donor || frm.doc.donor != '') {
		// 	frm.doc.fullname.$input.prop('readonly', true); //doesn't work
		// }
	},

	get_fullname: function(frm) {
		if (frm.doc.donor != ""){
			return frappe.call({
				method: 'non_profit.non_profit.doctype.donation.donation.get_fullname',
				args: {
					'donor': frm.doc.donor
				},
				callback: function(r) {
					frm.set_value('fullname', r.message);
				}
			});
		}
	},

	before_save: function(frm) {
		console.log(frm.doctype);
		if ((frm.doc.donor == "" || frm.doc.donor == null) && (frm.doc.fullname == "" || frm.doc.fullname == null)) {
			frm.doc.donor = "hambaa@email.com";
			frm.doc.fullname = "Hamba Allah";
		} else if (frm.doc.donor == "" || frm.doc.donor == null) {
			frm.doc.donor = "hambaa@email.com";
		}
	}
});
