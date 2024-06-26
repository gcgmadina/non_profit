from frappe import _


app_name = "non_profit"
app_title = "Non Profit"
app_publisher = "Frappe"
app_description = "Non Profit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pandikunta@frappe.io"
app_license = "MIT"

required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/non_profit/css/non_profit.css"
# app_include_js = "/assets/non_profit/js/non_profit.js"

# include js, css files in header of web template
# web_include_css = "/assets/non_profit/css/non_profit.css"
# web_include_js = "/assets/non_profit/js/non_profit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "non_profit/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Sales Invoice": "public/js/payment_entry.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "non_profit.utils.jinja_methods",
# 	"filters": "non_profit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "non_profit.install.before_install"
after_install = "non_profit.setup.setup_non_profit"

# Uninstallation
# ------------

# before_uninstall = "non_profit.uninstall.before_uninstall"
# after_uninstall = "non_profit.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "non_profit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Payment Entry": "non_profit.non_profit.custom_doctype.payment_entry.NonProfitPaymentEntry",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": [
		"non_profit.non_profit.doctype.membership.membership.set_expired_status",
	],
}

# Testing
# -------

before_tests = "non_profit.non_profit.utils.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "non_profit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "non_profit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"non_profit.auth.validate"
# ]


global_search_doctypes = {
	"Non Profit": [
		{'doctype': 'Certified Consultant', 'index': 1},
		{'doctype': 'Certification Application', 'index': 2},
		{'doctype': 'Volunteer', 'index': 3},
		{'doctype': 'Membership', 'index': 4},
		{'doctype': 'Member', 'index': 5},
		{'doctype': 'Donor', 'index': 6},
		{'doctype': 'Chapter', 'index': 7},
		{'doctype': 'Grant Application', 'index': 8},
		{'doctype': 'Volunteer Type', 'index': 9},
		{'doctype': 'Donor Type', 'index': 10},
		{'doctype': 'Membership Type', 'index': 11}
	]
}

standard_portal_menu_items = [
	{"title": _("Certification"), "route": "/certification",
	 "reference_doctype": "Certification Application", "role": "Non Profit Portal User"},
]

website_route_rules = [{'from_route': '/fundraising/<path:app_path>', 'to_route': 'fundraising'}, {'from_route': '/Fundraising/<path:app_path>', 'to_route': 'Fundraising'},]

website_redirects = [
    {"source": "/", "target": "/fundraising/"},
]

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["name", "in", ("Event-custom_thumbnail", "Event-custom_is_donation_event", "Donation-custom_bank")]]
	},
    {
        "doctype": "Role",
        "filters": [["name", "in", ("Non Profit Accounting", "Non Profit Chief", "Non Profit Secretary")]]
	},
    {
        "doctype": "Custom DocPerm",
        "filters": [["role", "in", ("Non Profit Accounting", "Non Profit Chief", "Non Profit Secretary", "Guest", "Non Profit Manager")]]
	},
    {
        "doctype": "Item Group",
        "filters": [["name", "in", ("Aset Tetap", "Inventaris Umum")]]
	},
    {
        "doctype": "Supplier",
        "filters": [["name", "in", ("One Time Supplier")]]
	},
    {
        "doctype": "Donor",
        "filters": [["name", "in", ("hambaa@email.com")]]
	},
    {
        "doctype": "Donor Type",
        "filters": [["name", "in", ("Jamaah", "Donatur Tetap")]]
    },
    {
        "doctype": "Donation Type",
        "filters": [["name", "in", ("Fidyah", "Hibah", "Infaq", "Zakat Fitrah", "Zakat Mal", "Jumatan", "Wakaf", "Kaffarat", "Specific Donation")]]
    },
    {
        "doctype": "Bank",
        "filters": [["name", "in", ("Bank Central Asia", "Bank CIMB Niaga", "Bank Mandiri", "Bank Rakyat Indonesia", "Bank Negara Indonesia")]]
    },
    {
        "doctype": "Account",
        "filters": [["name", "in", ("1121.001 - Bank Masjid - Madina", 
                                    "4100.001 - Donasi Umum - Madina",
                                    "4100.002 - Donasi Khusus - Madina",
                                    "1132.002 - Penerimaan Zakat - Madina",
                                    "1132.003 - Penerimaan Infaq - Madina",
                                    "1132.004 - Penerimaan Fidyah - Madina",
                                    "5130.019 - Honorarium Penceramah - Madina",
                                    "5130.020 - Biaya Kebersihan - Madina",
                                    "1141.001 - Persediaan Barang - Madina",
                                    "1211.002 - Aset Belum Dibayar - Madina")]]
	},
]