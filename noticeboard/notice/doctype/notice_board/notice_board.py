# Copyright (c) 2022, SDC and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import today

class NoticeBoard(WebsiteGenerator):
	def before_save(self):
		self.date=today()
		# mail=frappe.user_info(user_name)
		self.username=frappe.db.get_value("User",{"name":frappe.session.user},"full_name")

		# sql(f"""SELECT username from tabUser where email={frappe.session.user}""")
