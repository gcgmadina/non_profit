import frappe
from frappe import _

@frappe.whitelist()
def update_qr_image(qr_image):
    try:
        # Load the single doctype
        doc = frappe.get_single('QR Receive')

        # Update the qr_image field
        doc.qr_image = qr_image

        # Save the document
        doc.save()

        return {'status': 'success', 'message': _('QR Image updated successfully')}
    except Exception as e:
        frappe.log_error("Error updating QR Image: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error updating QR Image: {0}').format(str(e))}
    
@frappe.whitelist(allow_guest=True)
def get_qr_image():
    try:
        # Load the single doctype
        doc = frappe.get_single('QR Receive')
        
        # Get the qr_image field
        qr_image = doc.qr_image
        
        # Return the image data
        return {'status': 'success', 'qr_image': qr_image}
    
    except Exception as e:
        return {'status': 'error', 'message': str(e)}