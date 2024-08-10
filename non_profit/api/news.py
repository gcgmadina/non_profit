import frappe
from frappe import _
from frappe.utils import format_datetime, get_time, getdate

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

@frappe.whitelist(allow_guest=True)
def get_news_by_name(news_id):
    try:
        news = frappe.get_doc("Mosque News", news_id)
        
        # Format uploaded_time to display only hour and minute
        formatted_time = get_time(news.uploaded_time).strftime('%H:%M')
        
        # Format uploaded_date to Indonesian format (dd/mm/yyyy)
        formatted_date = getdate(news.uploaded_date).strftime('%d/%m/%Y')
        
        # Update the news dictionary with the formatted date and time
        news.update({
            'uploaded_time': formatted_time,
            'uploaded_date': formatted_date
        })
        
        return {'status': 'success', 'data': news}
    except Exception as e:
        frappe.log_error("Error fetching news: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error fetching news: {0}').format(str(e))}
