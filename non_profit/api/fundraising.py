import frappe
import datetime
import json

@frappe.whitelist(allow_guest=True)
def get_total_amount():
    today = datetime.date.today()
    first = today.replace(day=1)
    try:
        # Use frappe.db.sql to execute SQL query
        total_amount = frappe.db.get_value("Donation",
                                            {"item_type": ("!=", "Barang"),
                                             "date": ("between", [first, today])},
                                            "sum(amount) as total")
        return total_amount or 0  # Return 0 if total_amount is Non
    except Exception as e:
        frappe.log_error("Error in get_total_amount: {0}".format(str(e)))
        return 0  # Return 0 in case of an error

@frappe.whitelist(allow_guest=True)
def get_jumatan_donations():
    total_amount = frappe.db.get_value("Donation", {"donation_type": "Jumatan"}, "amount")
    return total_amount

@frappe.whitelist(allow_guest=True)
def get_event_list():
    try:
        # Use frappe.get_list to get list of events
        events = frappe.get_list("Event", 
                                 filters={"starts_on": (">", datetime.date.today()),
                                          "status": "Open",
                                          "event_category": "Event",
                                          "event_type": "Public"},
                                 fields=["subject", "thumbnail", "starts_on", "ends_on", "description"],
                                 order_by="starts_on asc")
        return events
    except Exception as e:
        frappe.log_error("Error in get_event_list: {0}".format(str(e)))
        return []
    
@frappe.whitelist(allow_guest=True)
def get_donation_events():
    try:
        # Use frappe.get_list to get list of events
        events = frappe.get_list("Event", 
                                 filters={"ends_on": (">", datetime.date.today()),
                                          "status": "Open",
                                          "event_category": "Donation",
                                          "event_type": "Public"},
                                 fields=["subject", "thumbnail", "starts_on", "ends_on", "description"],
                                 order_by="starts_on asc")
        return events
    except Exception as e:
        frappe.log_error("Error in get_donation_events: {0}".format(str(e)))
        return []