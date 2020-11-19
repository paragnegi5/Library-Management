# -*- coding: utf-8 -*-
# Copyright (c) 2020, Parag and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Articles(Document):

	def after_insert(self):
		frappe.msgprint("Article inserted")

	def after_delete(self):
		frappe.msgprint("Article Deleted")

	def on_update(self):
		frappe.msgprint("Article updated")
