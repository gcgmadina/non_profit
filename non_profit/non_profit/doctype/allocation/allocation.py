# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Allocation(Document):
	pass

@frappe.whitelist()
def get_total_amount(donation_type):
	print("=================== donation_type : ", donation_type)
	print("test")
	doc_donation = frappe.db.get_list(doctype = "Donation", 
						filters = {
							"donation_type" : donation_type
						},
						fields = ['amount']
					)
	total_amount = 0

	for v_amount in doc_donation:
		total_amount += v_amount.get('amount')

	return total_amount

@frappe.whitelist()
def sync(donation_type):
	print("donation type : ", donation_type)
	doc_donation = frappe.db.get_list(doctype = "Donation", 
						filters = {
							"donation_type" : donation_type
						},
						fields = ['amount']
					)
	total_amount = 0

	for v_amount in doc_donation:
		total_amount += v_amount.get('amount')

	return total_amount


@frappe.whitelist()
def save(donation_type):
	doc_donation = frappe.db.get_list(doctype = "Donation", 
						filters = {
							"donation_type" : donation_type
						},
						fields = ['amount']
					)
	total_amount = 0

	for v_amount in doc_donation:
		total_amount += v_amount.get('amount')

	return total_amount