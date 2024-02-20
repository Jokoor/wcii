# Copyright (c) 2024, Royalsmb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import boto3
import requests
from frappe.utils import get_site_name
from botocore.exceptions import ClientError

class EBooks(Document):
	def validate(self):
		self.upload_thumbnail('thumbnails', f'{self.file_name}.png')
		self.image = f'https://eu2.contabostorage.com/3865f68baca2410e80d810b5335edf7c:thumbnails/{self.file_name}.png'
		self.thumbnail_link = f'https://eu2.contabostorage.com/3865f68baca2410e80d810b5335edf7c:thumbnails/{self.file_name}.png'
	#download the thumbnail from using requests
	def download_thumbnail(self):
		res = requests.get(self.thumbnail_link)
		return res.content
		
	#upload the thumbnail to s3 and return the public url
	def upload_thumbnail(self, bucket, object_name=None):
		api_key = ''
		s3 = boto3.client('s3',endpoint_url='https://eu2.contabostorage.com',
                  aws_access_key_id='f1d127835b35923410038ceeb4eb2028',
                  aws_secret_access_key='9fa030b98ad6c2576f2c75949e830204')

		thumbnail=self.download_thumbnail()
		if object_name is None:
			object_name = 'no-name.png'

		try:
			response = s3.upload_fileobj(thumbnail, bucket, object_name)
		except ClientError as e:
			frappe.msgprint(e)
			return False
		return True
	
	
	#get the thumnail public url
	def get_thumnail_path(self):
		return f'/home/khan/frappe-bench/thumbnails/{self.file_name}.png'