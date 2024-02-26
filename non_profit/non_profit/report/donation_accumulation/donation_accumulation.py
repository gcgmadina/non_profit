# Copyright (c) 2024, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe import _, log

def execute(filters=None):
	if not filters:
		return [], []
	
	validate_filters(filters)
	
	columns, data = get_columns(), get_data(filters)
	
	return columns, data

def validate_filters(filters):
	if not filters.get("from_date") and not filters.get("to_date"):
		frappe.throw(
			_("{0} and {1} are mandatory").format(frappe.bold(_("From Date")), frappe.bold(_("To Date")))
		)

	if filters.get("from_date") > filters.get("to_date"):
		frappe.throw(_("From Date must be before To Date"))

def get_columns():
	columns = [
		{
			"label": _("Donation Type"),
			"fieldname": "donation_type",
			"fieldtype": "Link",
			"options": "Donation Type",
			"width": 180,
		},
		{
			"label": _("Total Donations"),
			"fieldname": "total_donations",
			"fieldtype": "Int",
			"width": 180,
		},
		{
			"label": _("Total Amount"),
			"fieldname": "total_amount",
			"fieldtype": "Currency",
			"width": 180,
		},
	]

	return columns

def get_data(filters):
	data = []

	if not filters.get("donation_type"):
		for type in frappe.get_all("Donation Type", fields=["donation_type"]):
			total_donation, total_amount = get_donation_type_data(filters,type.get("donation_type"))

			data.append({
				"donation_type": type.get("donation_type"),
				"total_donations": total_donation,
				"total_amount": total_amount
			})
	else:
		total_amount, total_donation = get_donation_type_data(filters,filters["donation_type"])

		data.append({
			"donation_type": filters["donation_type"],
			"total_donations": total_donation,
			"total_amount": total_amount
		})
	
	return data

def get_donation_type_data(filters,type):
	total_donation = frappe.db.count("Donation", filters={"donation_type": type,
													   "date": ("between", [filters["from_date"], filters["to_date"]])
													   })

	total_amount = frappe.db.get_value("Donation", {"donation_type": type,
												 "date": ("between", [filters["from_date"], filters["to_date"]])
												 }, "sum(amount)")

	return total_donation, total_amount
