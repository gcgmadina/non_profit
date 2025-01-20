import frappe
from frappe import _
from frappe.utils import today
from .fundraising import get_user_info

@frappe.whitelist(allow_guest=True)
def get_fundraisings(start=None, length=None, show_all=False):
    try:
        user = get_user_info()
        non_profit_roles = { 
            "Non Profit Manager", 
            "Non Profit Accounting", 
            "Non Profit Chief", 
            "Non Profit Secretary" 
            }

        if user and any(role in non_profit_roles for role in user.roles) and show_all:
            filters = {}
        else:
            filters = {
                "ends_on": (">=", today())
            }

        fundraisings = frappe.get_all("Fundraising", 
                                filters=filters,
                                fields=[
                                    "name", 
                                    "title", 
                                    "thumbnail", 
                                    "content",
                                    "starts_on",
                                    "ends_on",
                                    "account",
                                    "goal"
                                ],
                                order_by="ends_on asc",
                                start=start,
                                page_length=length)

        return {'status': 'success', 'data': fundraisings}
    except Exception as e:
        frappe.log_error("Error fetching fundraisings: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error fetching fundraisings: {0}').format(str(e))}

@frappe.whitelist()    
def add_new_funsraising(data):
    try:
        data = frappe._dict(data)

        fundraising = frappe.new_doc("Fundraising")
        fundraising.title = data.title
        fundraising.content = data.content
        fundraising.starts_on = data.starts_on
        fundraising.ends_on = data.ends_on
        fundraising.income_account = make_new_fundraising_income_account(data.title)
        fundraising.outcome_account = make_new_fundraising_outcome_account(data.title)
        fundraising.goal = data.goal
        fundraising.thumbnail = data.thumbnail

        if fundraising.income_account is None or fundraising.outcome_account is None:
            if fundraising.income_account:
                frappe.delete_doc("Account", fundraising.income_account)
            if fundraising.outcome_account:
                frappe.delete_doc("Account", fundraising.outcome_account)

            raise Exception("Error creating fundraising account")
        else:
            fundraising.insert()
            frappe.db.commit()

        return {'status': 'success', 'message': _('Fundraising added successfully')}
    except Exception as e:
        frappe.log_error("Error adding fundraising: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Error adding fundraising: {0}').format(str(e))}
    
def make_new_fundraising_income_account(account_name):
    try:
        user = get_user_info()

        parent_account = "4500.000 - Penggalangan Dana - Madina"
        
        child_accounts = frappe.get_all(
            "Account",
            filters={"parent_account": parent_account},
            fields=["account_number"],
            order_by="account_number asc"
        )
        
        if child_accounts:
            last_account_number = max(
                int(acc["account_number"].split(".")[-1]) for acc in child_accounts
            )
            next_account_number = f"4500.{last_account_number + 1:03}"
        else:
            next_account_number = "4500.001"

        if user.user_type == "Website User":
            return None
        else:
            account_doc = frappe.get_doc({
                "doctype": "Account",
                "account_name": account_name,
                "account_number": next_account_number,
                "parent_account": parent_account,
                "is_group": 0,
                "root_type": "Asset",  
                "account_type": "Receivable",
                "company": frappe.defaults.get_user_default("Company") 
            })

            account_doc.insert(ignore_permissions=True)
            frappe.db.commit()
            

        return account_doc.name

    except Exception as e:
        frappe.log_error(message=str(e), title="Account Creation Error")
        print(f"Error creating account: {str(e)}")
        return {"status": "failed", "message": f"Error creating account: {str(e)}"}
    
def make_new_fundraising_outcome_account(account_name):
    try:
        user = get_user_info()

        parent_account = "2150.000 - Alokasi Penggalangan Dana - Madina"
        
        child_accounts = frappe.get_all(
            "Account",
            filters={"parent_account": parent_account},
            fields=["account_number"],
            order_by="account_number asc"
        )
        
        if child_accounts:
            last_account_number = max(
                int(acc["account_number"].split(".")[-1]) for acc in child_accounts
            )
            next_account_number = f"2150.{last_account_number + 1:03}"
        else:
            next_account_number = "2150.001"

        if user.user_type == "Website User":
            return None
        else:
            account_doc = frappe.get_doc({
                "doctype": "Account",
                "account_name": account_name,
                "account_number": next_account_number,
                "parent_account": parent_account,
                "is_group": 0,
                "root_type": "Asset",  
                "account_type": "Payable",
                "company": frappe.defaults.get_user_default("Company") 
            })

            account_doc.insert(ignore_permissions=True)
            frappe.db.commit()
            

        return account_doc.name

    except Exception as e:
        frappe.log_error(message=str(e), title="Account Creation Error")
        print(f"Error creating account: {str(e)}")
        return {"status": "failed", "message": f"Error creating account: {str(e)}"}