import frappe

@frappe.whitelist(allow_guest=True)
def get_total_amount():
    try:
        # Use frappe.db.sql to execute SQL query
        total_amount = frappe.db.get_value("Donation",
                                            {"item_type": ("!=", "Barang")},
                                            "sum(amount) as total")
        print(total_amount)
        return total_amount or 0  # Return 0 if total_amount is None
    except Exception as e:
        frappe.log_error("Error in get_total_amount: {0}".format(str(e)))
        print("error")
        return 0  # Return 0 in case of an error

@frappe.whitelist(allow_guest=True)
def get_infaq_danations():
    total_amount = frappe.db.get_value("donation", {"donation_type": "Infaq"}, "sum(amount)", as_dict=True)
    return total_amount