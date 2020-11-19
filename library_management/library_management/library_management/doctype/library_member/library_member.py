# -*- coding: utf-8 -*-
# Copyright (c) 2020, Parag and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
	def after_insert(self):
		frappe.msgprint("Document inserted")

	def after_delete(self):
		frappe.msgprint("Document Deleted")

	def on_update(self):
		frappe.msgprint("Document updated")

