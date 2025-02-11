import frappe
from frappe import _
from frappe.utils import today
from .fundraising import get_user_info, create_new_donor
import erpnext
from erpnext.accounts.utils import get_account_balances

@frappe.whitelist(allow_guest=True)
def get_fundraisings(start=0, length=10, show_all=False, ended=False):
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
        elif user and ended:
            filters = {
                "ends_on": ("<", today())
            }
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
                                    "income_account",
                                    "outcome_account",
                                    "goal"
                                ],
                                order_by="ends_on asc",
                                start=start,
                                page_length=length)
        
        company = frappe.defaults.get_user_default("Company")
        
        for fundraising in fundraisings:
            account = frappe.get_all("Account",
                                    filters={"name": fundraising.income_account},
                                    fields=["name as value","account_currency"])
            income = get_account_balances(account, company)
            fundraising["income"] = income[0]["balance"] * -1

            account = frappe.get_all("Account",
                                    filters={"name": fundraising.outcome_account},
                                    fields=["name as value","account_currency"])
            outcome = get_account_balances(account, company)
            fundraising["outcome"] = outcome[0]["balance"]

        return {'status': 'success', 'data': fundraisings}
    except Exception as e:
        frappe.log_error("Error fetching fundraisings: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Gagal mendapatkan informassi penggalangan dana: {0}').format(str(e))}

@frappe.whitelist(allow_guest=True)
def get_fundraising_details(fundraising):
    try:
        fundraising = frappe.get_doc("Fundraising", fundraising)
        company = frappe.defaults.get_user_default("Company")
        
        account = frappe.get_all("Account",
                                filters={"name": fundraising.income_account},
                                fields=["name as value","account_currency"])
        income = get_account_balances(account, company)

        account = frappe.get_all("Account",
                                filters={"name": fundraising.outcome_account},
                                fields=["name as value","account_currency"])
        outcome = get_account_balances(account, company)

        fundraising_dict = fundraising.as_dict()
        fundraising_dict["income"] = income[0]["balance"] * -1
        fundraising_dict["outcome"] = outcome[0]["balance"]

        # print(fundraising.income)
        # print(fundraising.outcome)

        return {'status': 'success', 'data': fundraising_dict}
    except Exception as e:
        frappe.log_error("Error fetching fundraising details: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Gagal mendapatkan informassi penggalangan dana: {0}').format(str(e))}

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

            # raise Exception("Error creating fundraising account")
            raise Exception("Gagal membuat akun penggalangan dana")
        else:
            fundraising.insert()
            frappe.db.commit()

        return {'status': 'success', 'message': _('Penggalangan dana berhasil ditambahkan')}
    except Exception as e:
        frappe.log_error("Error adding fundraising: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Terjadi error paada proses pembuatan penggalangan dana: {0}').format(str(e))}
    
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
        return {"status": "failed", "message": f"Gagal membuat akun dana masuk: {str(e)}"}
    
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
        return {"status": "failed", "message": f"Gagal membuat akun untuk alokasi dana: {str(e)}"}
    
@frappe.whitelist(allow_guest=True)
def new_fundraising_journal_entry_receive(data):
    try:
        data = frappe._dict(data)

        user = get_user_info()

        fundraising = frappe.get_doc("Fundraising", data.fundraising)

        journal_entry = frappe.new_doc("Journal Entry")
        journal_entry.voucher_type = "Journal Entry"
        journal_entry.posting_date = today()
        journal_entry.company = frappe.defaults.get_user_default("Company")
        journal_entry.user_remark = f"Penerimaan Donasi - {data.cheque_name}"
        journal_entry.mode_of_payment = data.mode_of_payment

        if not frappe.db.exists("Donor", data.donor):
            create_new_donor(user.name, user.full_name)
        
        journal_entry.append("accounts", {
            "account": fundraising.income_account,
            "debit_in_account_currency": 0,
            "credit_in_account_currency": data.amount,
            "party_type": "Donor",
            "party": data.donor,
        })

        if data.mode_of_payment == "Cash":
            journal_entry.append("accounts", {
                "account": "1111.002 - Kas Besar - Madina",
                "debit_in_account_currency": data.amount,
                "credit_in_account_currency": 0,
            })
        elif data.mode_of_payment == "Wire Transfer":
            journal_entry.append("accounts", {
                "account": "1121.001 - Bank Masjid - Madina",
                "debit_in_account_currency": data.amount,
                "credit_in_account_currency": 0,
            })
            journal_entry.cheque_no = data.cheque_no
            journal_entry.cheque_date = data.cheque_date

        journal_entry.insert()
        frappe.db.commit()

        return {'status': 'success', 'message': _('Donasi berhasil dikirim. Tunggu konfirmasi dari pengurus masjid')}
    except Exception as e:
        frappe.log_error("Error creating journal entry: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Gagal mengirim donasi, silahkan coba kembali: {0}').format(str(e))}
    
@frappe.whitelist()
def submit_fundraising(name):
    try:
        fundraising = frappe.get_doc("Journal Entry", name)
        fundraising.submit()
        frappe.db.commit()

        return {'status': 'success', 'message': _('Berhasil mengkonfirmasi penerimaan donasi')}
    except Exception as e:
        frappe.log_error("Error submitting fundraising: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Gagal mengkonfirmasi penerimaan  donasi: {0}').format(str(e))}
    
@frappe.whitelist()
def new_fundraising_journal_entry_allocation(data):
    try:
        data = frappe._dict(data)

        fundraising = frappe.get_doc("Fundraising", data.fundraising)
        beneficiary = data.beneficiary if data.beneficiary else "owner@email.com"

        journal_entry = frappe.new_doc("Journal Entry")
        journal_entry.voucher_type = "Journal Entry"
        journal_entry.posting_date = today()
        journal_entry.company = frappe.defaults.get_user_default("Company")
        journal_entry.user_remark = "Penyaluran Dana Penggalangan"

        journal_entry.append("accounts", {
            "account": fundraising.outcome_account,
            "debit_in_account_currency": data.amount,
            "credit_in_account_currency": 0,
            "party_type": "Beneficiary",
            "party": beneficiary,
        })

        if data.mode_of_payment == "Cash":
            journal_entry.append("accounts", {
                "account": "1111.002 - Kas Besar - Madina",
                "debit_in_account_currency": 0,
                "credit_in_account_currency": data.amount,
            })
        elif data.mode_of_payment == "Wire Transfer":
            journal_entry.append("accounts", {
                "account": "1121.001 - Bank Masjid - Madina",
                "debit_in_account_currency": 0,
                "credit_in_account_currency": data.amount,
            })

        journal_entry.insert()
        journal_entry.submit()
        frappe.db.commit()

        return {'status': 'success', 'message': _('Data alokasi dana berhasil disimpan')}
    except Exception as e:
        frappe.log_error("Error creating journal entry: {}".format(str(e)))
        return {'status': 'failed', 'message': _('Gagal menyimpan alokasi dana: {0}').format(str(e))}
    
@frappe.whitelist(allow_guest=True)
def get_fundraising_journal_entry_received():
    try:
        user = get_user_info()

        filters = [["user_remark", "like", "Penerimaan Donasi -%"]]

        if user.user_type == "Website User":
            filters.append(["owner", "=", user.name])

        journal_entries = frappe.get_list(
            "Journal Entry",
            filters=filters,
            fields=["name", "posting_date", "user_remark", "total_debit", "total_credit", "voucher_type", "docstatus"]
        )
        return {"status": "success", "data": journal_entries}
    except Exception as e:
        frappe.log_error(f"Error fetching journal entries: {str(e)}")
        return {"status": "failed", "message": f"Gagal mengambil data: {str(e)}"}