import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_islamic_discourse_list(start=0, length=10):
    try:
        discourse_list = frappe.get_list("Islamic Discourse", 
                                        fields=[
                                            "name", 
                                            "subject",
                                            "speaker",
                                            "time", 
                                            "location",
                                            "thumbnail", 
                                            "description"
                                        ],
                                        start=start, page_length=length, order_by="time desc")
        return {
            "status": "success",
            "data": discourse_list
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse List Error"))
        return {
            "status": "error",
            "message": _("Islamic Discourse List Error: ", str(e))
        }
    
@frappe.whitelist(allow_guest=True)
def get_islamic_discourse(name):
    try:
        discourse = frappe.get_doc("Islamic Discourse", name)
        return {
            "status": "success",
            "data": discourse
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse Error"))
        return {
            "status": "error",
            "message": _("Islamic Discourse Error: ", str(e))
        }
    
@frappe.whitelist()
def new_islamic_discourse(data):
    try:
        discourse = frappe.new_doc("Islamic Discourse")
        discourse.update(data)
        discourse.save()
        frappe.db.commit()
        return {
            "status": "success",
            "message": _("Islamic Discourse Created Successfully")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse Creation Error"))
        return {
            "status": "error",
            "message": _("Islamic Discourse Creation Error: ", str(e))
        }
