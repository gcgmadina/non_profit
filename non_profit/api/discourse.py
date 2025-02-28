import frappe
from frappe import _
from frappe.utils import today

@frappe.whitelist(allow_guest=True)
def get_islamic_discourse_list(start=0, length=10, upcoming = True):
    try:
        if upcoming:
            filters = {
                "time": (">=", today())
            }
            order_by = "time asc"
        else :
            filters = {
                "time": ("<", today())
            }
            order_by = "time desc"

        discourse_list = frappe.get_list("Islamic Discourse", 
                                        filters=filters,
                                        fields=[
                                            "name", 
                                            "subject",
                                            "speaker",
                                            "time", 
                                            "location",
                                            "thumbnail", 
                                            "description"
                                        ],
                                        start=start, page_length=length, order_by=order_by)
        return {
            "status": "success",
            "data": discourse_list
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse List Error"))
        return {
            "status": "error",
            "message": _("Gagal mengambil data ceramah: {0}".format(str(e)))
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
            "message": _("Gagal mengambil data ceramah: {0}".format(str(e)))
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
            "message": _("Berhasil membuat jadwal kajian")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse Creation Error"))
        return {
            "status": "error",
            "message": _("Gagal membuat jadwal kajian: {0}".format(str(e)))
        }

@frappe.whitelist()
def update_islamic_discourse(name, data):
    try:
        discourse = frappe.get_doc("Islamic Discourse", name)
        discourse.update(data)
        discourse.save()
        frappe.db.commit()
        return {
            "status": "success",
            "message": _("Berhasil mengedit kajian")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse Update Error"))
        return {
            "status": "error",
            "message": _("Gagal mengedit kajian: {0}".format(str(e)))
        }
    
@frappe.whitelist()
def delete_islamic_discourse(name):
    try:
        frappe.delete_doc("Islamic Discourse", name)
        frappe.db.commit()
        return {
            "status": "success",
            "message": _("Berhasil menghapus kajian")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Islamic Discourse Deletion Error"))
        return {
            "status": "error",
            "message": _("Gagal menghapus kajian: {0}".format(str(e)))
        }