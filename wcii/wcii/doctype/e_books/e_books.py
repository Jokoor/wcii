# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

from urllib.request import urlopen
import frappe
from frappe.website.website_generator import WebsiteGenerator
import boto3
import requests
from frappe.utils import get_site_name
from botocore.exceptions import ClientError

class EBooks(Document):
	pass