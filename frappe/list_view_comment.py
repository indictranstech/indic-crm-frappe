# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.core.doctype.communication.comment import notify_mentions
import frappe
import os
import time
import redis
from frappe.utils import get_site_path
from frappe import conf


@frappe.whitelist()
def process_comment(dt, dn, comments=None):	
	comm_doc = frappe.new_doc("Communication")
	comm_doc.reference_doctype = dt
	comm_doc.reference_name = dn.strip()
	comm_doc.subject = comments
	comm_doc.content = comments
	comm_doc.save()


	