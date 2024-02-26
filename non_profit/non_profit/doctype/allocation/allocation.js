// Copyright (c) 2024, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Allocation', {
	validate: function(frm) {
		if(frm.doc.total_amount === undefined) {
			
			frappe.msgprint({
				title: __('Save Failed !'),
				indicator: 'red',
				message: __('Please make sure click on the update before save')
			});
		}else {
			return frappe.call({
				args: {
					donation_type: frm.doc.donation_type
				},
				method: 'non_profit.non_profit.doctype.allocation.allocation.get_total_amount',
				callback: (r) => {
					console.log("R : ", r.message)
					frm.set_value('total_amount', r.message)
				}
			});
		}
		},
	


	refresh: function(frm) {
		// frm.disable_save()
		$('input[data-fieldname="total_amount"]').attr('disabled', 'disabled');
		frm.add_custom_button(__('Update'), () => {
			return frm.trigger('sync');
		});
		// frm.add_custom_button(__('Save'), () => {
		// 	if(frm.doc.total_amount === undefined) {
		// 		frappe.msgprint({
		// 			title: __('Save Failed !'),
		// 			indicator: 'red',
		// 			message: __('Please make sure click on the update before save')
		// 		});
		// 	}	
		// 	else {
		// 		return frm.trigger('save');
		// 	}
			
		// }).addClass('btn-primary');

	},

	// save: function(frm) {
	// 	return frappe.call({
	// 		args: {
	// 			donation_type: frm.doc.donation_type
	// 		},
	// 		method: 'non_profit.non_profit.doctype.allocation.allocation.get_total_amount',
	// 		callback: (r) => {
	// 			console.log("R : ", r.message)
	// 			frm.set_value('total_amount', r.message)
	// 		}
	// 	});
	// },

	sync: function(frm) {
		return frappe.call({
			args: {
				donation_type: frm.doc.donation_type
			},
			method: 'non_profit.non_profit.doctype.allocation.allocation.sync',
			callback: (r) => {
				frm.set_value('total_amount', r.message)
				// console.log("R : ", r)
			}
		});
	}
});
