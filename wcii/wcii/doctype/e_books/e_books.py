# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import file_manager
import urllib.request
from pdf2image import convert_from_path
class EBooks(Document):
	def validate(self):
		self.get_book_thumbnail()	
#download the file using urrlib
	def get_book_thumbnail(self):
			url = self.thumbnail_link
			urllib.request.urlretrieve(url, f'/home/khan/frappe-bench/sites/wcii/public/files/{self.name}.pdf')
			image = convert_from_path(f'/home/khan/frappe-bench/sites/wcii/public/files/{self.name}.pdf')
			image[0].save(f'/home/khan/frappe-bench/sites/wcii/public/files/{self.name}.png', 'PNG')
			self.image = f'/files/{self.name}.png'