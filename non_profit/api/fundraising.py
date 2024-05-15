import frappe
from frappe.utils import get_datetime_str, format_date
from frappe.utils.file_manager import save_file
import datetime
from datetime import timedelta
import json
from faker import Faker

@frappe.whitelist()
def get_user_info() -> dict:
    try:
        # user = frappe.get_doc("User", frappe.session.user)
        current_user = frappe.session.user
        user = frappe.db.get_value("User", current_user, ["name", "first_name", "full_name", "user_image", "role_profile_name", "user_type"]
                                   , as_dict=True)
        user["roles"] = frappe.get_roles(current_user)
        return user
    except Exception as e:
        frappe.log_error("Error in get_user_info: {0}".format(str(e)))
        return None

@frappe.whitelist(allow_guest=True)
def get_total_amount():
    today = datetime.date.today()
    first = today.replace(day=1)
    try:
        # Use frappe.db.sql to execute SQL query
        total_amount = frappe.db.get_value("Donation",
                                            {"item_type": ("!=", "Barang"),
                                             "date": ("between", [first, today])},
                                            "sum(amount) as total")
        return total_amount or 0  # Return 0 if total_amount is Non
    except Exception as e:
        frappe.log_error("Error in get_total_amount: {0}".format(str(e)))
        return 0  # Return 0 in case of an error

@frappe.whitelist(allow_guest=True)
def get_jumatan_donations():
    total_amount_date = frappe.db.get_value("Donation", {"donation_type": "Jumatan"}, ["amount", "date"])
    return total_amount_date

@frappe.whitelist(allow_guest=True)
def get_donation_by_type():
    try:
        # Get list of all donation types
        donation_types = frappe.get_list("Donation Type", fields=["donation_type"])
        # print(donation_types)

        # Initialize a dictionary to store total amount for each donation type
        total_donations_by_type = {}

        # Iterate over each donation type and calculate total amount
        for donation_type in donation_types:
            # print(donation_type["donation_type"])
            total_amount = frappe.db.get_value("Donation",
                                               {"donation_type": donation_type["donation_type"],
                                                "item_type": ("!=", "Barang"),
                                                "date": ("between", [datetime.date.today().replace(day=1), datetime.date.today()])
                                                },
                                               ["sum(amount) as total"])
            total_donations_by_type[donation_type["donation_type"]] = total_amount or 0
        # print(total_donations_by_type)
        return total_donations_by_type
    except Exception as e:
        frappe.log_error("Error in get_donation_by_type: {0}".format(str(e)))
        return {}

@frappe.whitelist(allow_guest=True)
def get_event_list():
    try:
        # Use frappe.get_list to get list of events
        events = frappe.get_list("Event", 
                                 filters={# "starts_on": (">=", datetime.date.today()),
                                          "status": "Open",
                                          "event_type": "Public",
                                          "is_donation_event": 0},
                                 or_filters=[ ["starts_on", ">=", datetime.date.today()], ["ends_on", ">=", datetime.date.today()] ],
                                 fields=["name","subject", "event_thumbnail", 
                                         "DATE_FORMAT(starts_on, '%D %M %Y') as starts_on", 
                                         "DATE_FORMAT(ends_on, '%D %M %Y') as ends_on", 
                                         "description"],
                                 order_by="starts_on asc")
        return events
    except Exception as e:
        frappe.log_error("Error in get_event_list: {0}".format(str(e)))
        return []
    
@frappe.whitelist(allow_guest=True)
def get_event_by_id(event_id):
    try:
        event = frappe.get_doc("Event", event_id)
        return event
    except Exception as e:
        frappe.log_error("Error in get_event_by_id: {0}".format(str(e)))
        return None
    
@frappe.whitelist(allow_guest=True)
def get_donation_events():
    try:
        # Use frappe.get_list to get list of events
        events = frappe.get_list("Event", 
                                 filters={"ends_on": (">=", datetime.date.today()),
                                          "status": "Open",
                                          "event_type": "Public",
                                          "is_donation_event": 1},
                                 fields=["name","subject", "event_thumbnail", 
                                         "DATE_FORMAT(starts_on, '%D %M %Y') as starts_on", 
                                         "DATE_FORMAT(ends_on, '%D %M %Y') as ends_on", 
                                         "description"],
                                 order_by="ends_on asc")
        return events
    except Exception as e:
        frappe.log_error("Error in get_donation_events: {0}".format(str(e)))
        return []
    
def get_company_for_donations():
	company = frappe.db.get_single_value('Non Profit Settings', 'donation_company')
	if not company:
		from non_profit.non_profit.utils import get_company
		company = get_company()
	return company
    
@frappe.whitelist(allow_guest=True)
def new_donation(donation_type, date, amount, mode_of_payment, phone, donor="hambaa@email.com", fullname="Hamba Allah", item_type="Uang", naming_series='NPO-DTN-.YYYY.-', donation_event=None, bank=None ):
    try:
        company = get_company_for_donations()
        donation = frappe.new_doc("Donation")
        donation.update({
            "donation_type": donation_type,
            "donor": donor,
            "phone_number": phone,
            "fullname": fullname,
            "date": date,
            "amount": amount,
            "mode_of_payment": mode_of_payment,
            "item_type": item_type,
            "naming_series": naming_series,
            "company": company,
            "donation_event": donation_event,
            "bank": bank
        })
        donation.insert(ignore_permissions=True)
        print(donation.name)
        return donation.name
    except Exception as e:
        frappe.log_error("Error in new_donation: {0}".format(str(e)))
        user_type = frappe.db.get_value('User', frappe.session.user, 'user_type')
        print(e)
        return None

@frappe.whitelist(allow_guest=True)
def new_goods_donation(donation_type, date, item, amount, phone, donor="hambaa@email.com", fullname="Hamba Allah", item_type="Barang", naming_series='NPO-DTN-.YYYY.-'):
    try:
        company = get_company_for_donations()
        donation = frappe.new_doc("Donation")
        donation.update({
            "donation_type": donation_type,
            "donor": donor,
            "phone_number": phone,
            "fullname": fullname,
            "date": date,
            "item_name": item,
            "item_amount": amount,
            "item_type": item_type,
            "naming_series": naming_series,
            "company": company
        })
        donation.insert(ignore_permissions=True)
        return donation.name
    except Exception as e:
        frappe.log_error("Error in new_goods_donation: {0}".format(str(e)))
        return None
    
@frappe.whitelist(allow_guest=True)
def get_user_donations(user):
    try:
        if 'Non Profit Accounting' in user['data']['roles']:
            donations = frappe.get_list("Donation", fields=["name", "donation_type", "date", "amount", "item_name", "item_amount", "item_type", "mode_of_payment", "phone_number", "fullname", "docstatus", "company", "evidance_of_transfer"],
                                        order_by="date desc")
        else:
            donations = frappe.get_list("Donation", filters={"owner": user['data']['name']}, fields=["name", "donation_type", "date", "amount", "item_name", "item_amount", "item_type", "mode_of_payment", "phone_number", "fullname", "docstatus", "company", "evidance_of_transfer"],
                                        order_by="date desc")
        return donations
    except Exception as e:
        frappe.log_error("Error in get_user_donations: {0}".format(str(e)))
        return []
    
@frappe.whitelist()
def get_donation_by_id(donation_id):
    try:
        donation = frappe.get_doc("Donation", donation_id)
        return donation
    except Exception as e:
        frappe.log_error("Error in get_donation_by_id: {0}".format(str(e)))
        return None
    
@frappe.whitelist()
def submit_donation(donation_id):
    try:
        donation = frappe.get_doc("Donation", donation_id)
        donation.submit()
        return donation.name
    except Exception as e:
        frappe.log_error("Error in submit_donation: {0}".format(str(e)))
        return None
    
@frappe.whitelist(allow_guest=True)
def upload_evidence(donation_id, evidence):
    try:
        donation = frappe.get_doc("Donation", donation_id)
        donation.evidance_of_transfer = evidence
        donation.save(ignore_permissions=True)
        return donation.name
    except Exception as e:
        frappe.log_error("Error in upload_evidence: {0}".format(str(e)))
        return None

@frappe.whitelist()
def new_event(subject, event_category, event_type, starts_on, is_donation_event, thumbnail=None, description=None, status="open", ends_on=None):
    try:
        event = frappe.new_doc("Event")
        event.update({
            "subject": subject,
            "event_category": event_category,
            "event_type": event_type,
            "starts_on": starts_on,
            "ends_on": ends_on,
            "event_thumbnail": thumbnail,
            "status": status,
            "description": description,
            "is_donation_event": is_donation_event
        })
        event.insert(ignore_permissions=True)
        return event.name
    except Exception as e:
        frappe.log_error("Error in new_event: {0}".format(str(e)))
        print("ERROR : ", e)
        return None

@frappe.whitelist(allow_guest=True)
def upload_file(file):
    print("file: ", file)
    try:
        file_url = save_file("Donation", file, "files", is_private=0)
        return file_url
    except Exception as e:
        frappe.log_error("Error in upload_file: {0}".format(str(e)))
        return None
    
# Faker
@frappe.whitelist()
def populate_donation_data():
    fake = Faker(['id_ID'])
    for i in range(10):
        donation_type = "Zakat Mal"
        date = fake.date_this_month()
        amount = fake.random_int(min=10000, max=1000000)
        mode_of_payment = "Cash"
        phone = fake.phone_number()
        # donor = None
        fullname = fake.name()
        item_type = "Uang"
        naming_series = 'NPO-DTN-.YYYY.-'
        donation_event = None
        new_donation(donation_type=donation_type, date=date, amount=amount, mode_of_payment=mode_of_payment, phone=phone, fullname=fullname, item_type=item_type, naming_series=naming_series, donation_event=donation_event)

@frappe.whitelist()
def populate_event_data():
    fake = Faker(['id_ID'])
    for i in range(10):
        subject = fake.sentence(nb_words=5, variable_nb_words=True)
        event_category = "Event"
        event_type = "Public"
        starts_on = fake.date_this_month()
        is_donation_event = fake.random_int(min=0, max=1)
        thumbnail = None
        description = fake.text()
        status = "Open"

        if is_donation_event == 0:  
            ends_on = fake.date_between_dates(date_start=starts_on, date_end=starts_on + timedelta(days=30)) 
            if ends_on == starts_on:  
                ends_on = None
        else:  
            ends_on = fake.date_between_dates(date_start=starts_on + timedelta(days=1))

        new_event(subject=subject, event_category=event_category, event_type=event_type, starts_on=starts_on, is_donation_event=is_donation_event, thumbnail=thumbnail, description=description, status=status, ends_on=ends_on)

@frappe.whitelist()
def get_bank_list():
    try:
        banks = frappe.get_list("Bank", fields=["name", "swift_number"])
        return banks
    except Exception as e:
        frappe.log_error("Error in get_bank_list: {0}".format(str(e)))
        return []

@frappe.whitelist()
def get_bank_account_list():
    try:
        bank_accounts = frappe.get_list("Bank Account", fields=["name", "account_name", "bank", "bank_account_no"])
        return bank_accounts
    except Exception as e:
        frappe.log_error("Error in get_bank_account_list: {0}".format(str(e)))
        return []

@frappe.whitelist()
def new_bank_account(bank_name, account_name, account_number, coa_account = "Bank Masjid", is_company_account = 1 ):
    try:
        account = frappe.db.get_value("Account", {"account_name": coa_account}, "name")

        bank = frappe.new_doc("Bank Account")
        bank.update({
            "bank": bank_name,
            "bank_account_no": account_number,
            "account_name": account_name,
            "account": account,
            "is_company_account": is_company_account
        })
        bank.insert(ignore_permissions=True)
        return bank.name
    except Exception as e:
        frappe.log_error("Error in new_bank_account: {0}".format(str(e)))
        return None
    
@frappe.whitelist()
def get_bank_account_by_id(bank_account_id):
    try:
        bank_account = frappe.get_doc("Bank Account", bank_account_id)
        return bank_account
    except Exception as e:
        # Mengembalikan pesan kesalahan jika terjadi kesalahan
        frappe.log_error("Error in get_bank_account_by_id: {0}".format(str(e)))
        return {
            "error": "An error occurred while getting bank account."
        }

@frappe.whitelist()
def edit_bank_account(bank_account):
    try:
        bank_account = json.loads(bank_account)
        bank_account_doc = frappe.get_doc("Bank Account", bank_account["name"])
        bank_account_doc.update({
            "bank": bank_account["bank"],
            "bank_account_no": bank_account["bank_account_no"],
            "account_name": bank_account["account_name"]
        })
        bank_account_doc.save(ignore_permissions=True)
        return bank_account_doc.name
    except Exception as e:
        frappe.log_error("Error in edit_bank_account: {0}".format(str(e)))
        return None
    
@frappe.whitelist()
def delete_document(doctype, docname):
    try:
        frappe.delete_doc(doctype, docname, ignore_permissions=True)
        return True
    except Exception as e:
        frappe.log_error("Error in delete_document: {0}".format(str(e)))
        return False