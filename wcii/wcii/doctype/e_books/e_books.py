# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

from urllib.request import urlopen
import frappe
from frappe.model.document import Document
import urllib.request
from pdf2image import convert_from_path
from frappe.utils import get_site_path
class EBooks(Document):
	def validate(self):
		self.get_book_thumbnail()	
#download the file using urrlib
	def get_book_thumbnail(self, ignore_permissions=True):
			url = self.thumbnail_link
			urllib.request.urlretrieve(url, f'/home/khan/frappe-bench/sites/app.wcii.royalsmb.com/public/files/{self.name}.png')
			self.thumbnail_link = f'/files/{self.name}.png'
			self.image = f'/files/{self.name}.png'
			self.ignore_permissions=True

			# image = convert_from_path(f'/home/khan/frappe-bench/sites/wcii/public/files/{self.name}.pdf')
			# image[0].save(f'/home/khan/frappe-bench/sites/wcii/public/files/{self.name}.png', 'PNG')