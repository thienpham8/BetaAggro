#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-15                   
# -------------------------- #

import mysql.connector
from functools import wraps

class Connector(object):
	"""This class handles the connection between back-end scripts and the database"""
	
	def __init__(self, usr="root", pw="1q2w3e4r", hosted="localhost", db="betaaggro", verbose=False):
		self.connection = mysql.connector.connect(user=usr, password=pw, host=hosted, database=db)
		self.cursor = self.connection.cursor(dictionary=True)
		self.response = None
		self.errors = None
		self.verbose = verbose
		
	def commit(func):
		"""Decorator to commit entries to database after wrapped function executes"""
		def _decorator(self, *args, **kwargs):
			r = func(self, *args, **kwargs)
			self.connection.commit()
			if self.verbose: 
				print "Committed."
			return r
		return wraps(func)(_decorator)
		
		
	def close(self):
		"""Closes connection nicely"""
		self.connection.commit()
		self.cursor.close()
		self.connection.close()
		
	@commit
	def addYelpReview(self, dic):
		"""This takes a yelp review and inserts it into the review table"""
		pass
		
		
	@commit
	def addYelpBusiness(self, dic):
		"""This makes an entry into the 'yelp' table and related tables"""
		business = ("INSERT INTO yelp "
							"(claimed, rating, ratingImage, reviewCount, name, ratingImageSmall, "
							"url, isClosed, phone, snippet, imageURL, snippetURL, uniqueName) "
							"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
							
		businessData = (dic.get("is_claimed", ""), dic.get("rating", ""), dic.get("rating_img_url", ""), dic.get("review_count", ""), 
									dic.get("name", ""), dic.get("rating_img_url_small", ""), dic.get("url", ""), dic.get("is_closed", ""), dic.get("phone", ""),
									dic.get("snippet_text", ""), dic.get("image_url", ""), dic.get("snippet_image_url", ""), dic.get("id", ""))										
		try:
			self.cursor.execute(business, businessData)
			return dic.get("id", "No id").encode("ascii", "ignore")
		except mysql.connector.errors.IntegrityError as e:
			try:
				return "Duplicate entry: {}".format(dic["name"])
			except:
				return "Duplicate entry."
		
	@commit
	def addLocation(self, dic):
		"""Adds location to location table in DB using YelpAPI.search dictionary results"""
		
		insert = ("INSERT INTO location VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
		
		data = (dic.get("id","No id"), dic["location"].get("city", ""), dic["location"].get("postal_code", ""), dic["location"].get("country_code", ""),
					" ".join(dic["location"]["display_address"]), float(dic["location"]["coordinate"].get("latitude", 0)), 
					float(dic["location"]["coordinate"].get("longitude", 0)), dic["location"].get("state_code", "No State"))
					
		try:
			self.cursor.execute(insert, data)
			return dic.get("id", "No id").encode("ascii", "ignore")
		except mysql.connector.errors.IntegrityError as e:
				try:
					return "Duplicate entry: {}".format(businessName + " location")
				except:
					return "Duplicate category entry."
		
		
	@commit
	def addCategory(self,businessName, categories):
		"""This associates a category with a business. This requires the businessName rendered from YelpAPI.business()"""
		
		for category in categories:
			
			insert = ("INSERT INTO categories VALUES (%s, %s)")
			
			try:
				self.cursor.execute(insert, (category, businessName))
				return "{} category: {}".format(businessName.encode("ascii", "ignore"), category.encode("ascii", "ignore"))
			except mysql.connector.errors.IntegrityError as e:
				try:
					return "Duplicate entry: {}".format(businessName + " category " + category)
				except:
					return "Duplicate category entry."
	
		
	@commit
	def addGoogleBusiness(self, dic):
		"""This makes an entry into the 'google' table and related tables"""
		pass
		
		
	@commit
	def addFacebookBusiness(self, dic):
		"""This makes an entry into the 'facebook' table and related tables"""
		pass
		
		
	@commit
	def addUser(self, dic):
		"""This adds a user to the 'user' table and related tables"""
		pass
		
		
	def select(self, criteria, table="yelp", limit=1):
		"""This will select from table WHERE criteria[0] LIKE criteria[1]"""
		
		query = ("SELECT * FROM {} WHERE {} LIKE %s LIMIT {}".format(table, criteria[0], limit))
		self.cursor.execute(query, ("%" + criteria[1] + "%",))
		results = self.cursor.fetchall()
		return results
	
	@commit
	def update(self, table, dic, criteria):
		"""This will update a specific table using Key, Value pairs in dic"""
		pass
		
		
	@commit
	def delete(self, table, criteria):
		"""This will delete a database entry based on criteria"""
		pass
		
		
if __name__ == "__main__":
	print "Hi! Don't run this script. It is intended for import only!"