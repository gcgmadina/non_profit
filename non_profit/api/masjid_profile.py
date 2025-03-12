import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_masjid_profile():
    try:
        masjid_profile = frappe.get_doc("Masjid Profile")
        return {
            'status': "success",
            'data': masjid_profile.as_dict()
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to get Masjid Profile"))
        return {
            'status': "error",
            'message': _("Failed to get Masjid Profile: {0}").format(str(e))
        }
    
@frappe.whitelist()
def update_masjid_profile(data):
    try:
        data = frappe.parse_json(data)
        masjid_profile = frappe.get_single("Masjid Profile")
        masjid_profile.update(data)
        masjid_profile.save()  
        frappe.db.commit() 
        
        return {
            'status': "success",
            'message': _("Masjid Profile updated successfully")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Failed to update Masjid Profile"))
        return {
            'status': "error",
            'message': _("Failed to update Masjid Profile: {0}").format(str(e))
        }