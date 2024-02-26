frappe.pages['donation-recap'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Donation Recap',
		single_column: true
	});
}