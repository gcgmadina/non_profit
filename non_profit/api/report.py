import frappe
from frappe.utils import getdate, today
from erpnext.accounts.report.trial_balance.trial_balance import execute
from non_profit.non_profit.utils import get_company
import datetime

@frappe.whitelist()
def report_data(filters=None):
    try:
        print(type(filters))
        if filters is None:
            filters = {}
        elif isinstance(filters, str):
            filters = frappe.parse_json(filters)

        filters["company"] = get_company()

        from erpnext.accounts.utils import get_fiscal_year
        fiscal_year = get_fiscal_year(today())[0]
        filters["fiscal_year"] = fiscal_year

        filters = frappe._dict(filters)
        data = execute(filters)

        cash_or_bank = []
        donation = []
        purchase = []
        expense = []
        for i in data[-1][:-1]:
            if "account" in i:
                if frappe.db.exists("Account", i["account"]):
                    account = frappe.get_doc("Account", i["account"])

                if account.is_group == 0:
                    i["account_name"] = account.account_name

                    parent_account = frappe.get_doc("Account", i["parent_account"])

                    if parent_account.account_name == "Kas Rupiah" or parent_account.account_name == "Bank Rupiah":
                        cash_or_bank.append(i)
                    elif parent_account.account_name == "Piutang Lain lain":
                        donation.append(i)
                    elif parent_account.account_name == "Persediaan Barang":
                        purchase.append(i)
                    elif parent_account.account_name == "Biaya Kantor & Gudang":
                        expense.append(i)

        return {
            "cash_or_bank": cash_or_bank,
            "donation": donation,
            "purchase": purchase,
            "expense": expense
        }

    except Exception as e:
        frappe.log_error("Error retrieving trial balance: {}".format(str(e)))
        return str(e)