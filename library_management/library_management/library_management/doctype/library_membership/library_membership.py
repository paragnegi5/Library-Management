# -*- coding: utf-8 -*-
# Copyright (c) 2020, Parag and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def after_insert(self):
		frappe.msgprint("New Membership Created")

	def after_delete(self):
		frappe.msgprint("Membership Deleted")

	def on_update(self):
		frappe.msgprint("Membership updated")

