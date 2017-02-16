#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-15                   
# -------------------------- #

import mysql.connector
from functools import wraps


class Connector(object):
	"""This class handles the connection between back-end scripts and the database"""
	
	def __init__(self, db="betaaggro"):
		self.connection = mysql.connector.connect(user="root", password="1q2w3e4r", host="localhost", database=db)
		self.cursor = self.connection.cursor()
		
		
	def commit(func):
		"""Decorator to commit after wrapped function"""
		def _decorator(self, *args, **kwargs):
			r = func(self, *args, **kwargs)
			self.connection.commit()
			print "Committed."
			return r
		return wraps(func)(_decorator)
		
		
	def close(self):
		"""Closes connection nicely"""
		self.connection.commit()
		self.cursor.close()
		self.connection.close()
		
		
	@commit
	def addYelpBusiness(self, dic):
		"""This makes an entry into the 'yelp' table and related tables"""
		
		business = ("INSERT INTO yelp "
							"(claimed, rating, ratingImage, reviewCount, name, ratingImageSmall, "
							"url, isClosed, phone, snippet, imageURL, snippetURL, uniqueName) "
							"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		
		businessData = (dic["is_claimed"], dic["rating"], dic["rating_img_url"], dic["review_count"], 
									dic["name"], dic["rating_img_url_small"], dic["url"], dic["is_closed"], dic["phone"],
									dic["snippet_text"], dic["image_url"], dic["snippet_image_url"], dic["id"])
									
		self.cursor.execute(business, businessData)
		
	

		
	
			
	