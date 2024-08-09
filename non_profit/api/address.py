import frappe
from frappe import _
import json

@frappe.whitelist()
def input_address(address, is_mosque=False):
    try:
        # Load doctype
        doc = frappe.new_doc("Address")

        # Update address fields
        doc.address_title = address["name"]
        doc.address_line1 = address["address_line1"]
        doc.city = address["city"]
        doc.state = address["province"]
        doc.pincode = address["postalcode"]
        doc.country = address["country"]
        doc.phone = address["phone"]
        doc.email_id = address["email"]

        if is_mosque:
            doc.address_type = "Permanent"
            

        # Save address
        doc.save()

        return {'status': 'success', 'message': _('Address updated successfully')}
    except Exception as e:
        frappe.log_error("Error updating address: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error updating address: {0}').format(str(e))}

@frappe.whitelist(allow_guest=True)
def get_permanent_address():
    try:
        # Get address
        address = frappe.get_all("Address", filters={"address_type": "Permanent"}, fields=["name", "address_title", "address_line1", "city", "state", "pincode", "country", "phone", "email_id", "image"])

        return {'status': 'success', 'data': address}
    except Exception as e:
        frappe.log_error("Error fetching address: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error fetching address: {0}').format(str(e))}
    
@frappe.whitelist()
def edit_address(address):
    try:
        address_list = frappe.get_all("Address", filters={"address_title": address["name"]}, fields=["name"])
        doc = frappe.get_doc("Address", address_list[0].name)

        doc.update({
            "address_title": address["name"],
            "address_line1": address["address_line1"],
            "city": address["city"],
            "state": address["province"],
            "pincode": address["postalcode"],
            "country": address["country"],
            "phone": address["phone"],
            "email_id": address["email"],
            "image": address["image"]
        })
        doc.save()

        return {'status': 'success', 'message': _('Address updated successfully')}
    except Exception as e:
        frappe.log_error("Error fetching address: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error fetching address: {0}').format(str(e))}