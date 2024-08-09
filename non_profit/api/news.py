import frappe
from frappe import _

@frappe.whitelist()
def add_news(news):
    try:
        doc = frappe.new_doc('Mosque News')
        print(news)

        doc.update({
            "title": news["title"],
            "thumbnail": news["thumbnail"],
            "content": news["content"]
        })

        doc.save()

        return {'status': 'success', 'message': _('News added successfully')}
    except Exception as e:
        frappe.log_error("Error adding news: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error adding news: {0}').format(str(e))}

@frappe.whitelist(allow_guest=True)
def get_news():
    try:
        news = frappe.get_all("Mosque News", fields=["name", "title", "thumbnail", "content", "uploaded_date", "uploaded_time"])

        for item in news:
            uploaded_time = item.get("uploaded_time")
            if uploaded_time:
                total_seconds = int(uploaded_time.total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, _ = divmod(remainder, 60)
                item["uploaded_time"] = f"{hours:02}:{minutes:02}"

        return {'status': 'success', 'data': news}
    except Exception as e:
        frappe.log_error("Error fetching news: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error fetching news: {0}').format(str(e))}
    
@frappe.whitelist()
def edit_news(news):
    try:
        doc = frappe.get_doc("Mosque News", news["name"])

        doc.update({
            "title": news["title"],
            "thumbnail": news["thumbnail"],
            "content": news["content"]
        })

        doc.save()

        return {'status': 'success', 'message': _('News updated successfully')}
    except Exception as e:
        frappe.log_error("Error updating news: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error updating news: {0}').format(str(e))}