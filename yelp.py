#!/usr/bin/env python
# Created by: Zac Smith      
# 2017-1-31                        

# Use this line to set PATH to the virtual environment ---------- #
import runEnv
# --------------------------------------------------------------- #

# Need to take the business id and query https://api.yelp.com/v2/business/


import json
import requests
import urllib
import flask
from requests_oauthlib import OAuth1


class YelpAPI(object):
	"""This class handles everything with the Yelp API"""

	def __init__(self):
		"""Initialize some class attributes"""
		self.response = None
		self.searchURL = "https://api.yelp.com/v2/search/?"
		self.businessURL = "https://api.yelp.com/v2/business/"
		self.credentials = json.loads(open("credentials.json").read())
		self.auth = OAuth1(self.credentials["yelp"]["key"], self.credentials["yelp"]["kSecret"], 
													self.credentials["yelp"]["token"], self.credentials["yelp"]["tSecret"])

	def search(self, term="CSUEB", location="Hayward", limit=1):
		"""URL encodes search term and location of search and returns a JSON dictionary response"""
	
		encoded = urllib.urlencode({"term" : term, "location" : location, "limit" : limit})
		response = requests.get(self.searchURL+encoded, auth=self.auth)
		
		self.response = response.json()
		
		# returns a python dictionary of the JSON response
		return self.response
		
		
	def business(self, id="california-state-university-east-bay-hayward"):
	
		if self.response:
			print self.businessURL+id
			response = requests.get(self.businessURL+id, auth=self.auth)
			
		self.response = response.json()
		
		# returns a python dictionary of the JSON response
		return self.response
			
		
		
		

		
# ------ Script executed below ------ #
if __name__ == "__main__":
	yelp = YelpAPI()
	r = yelp.search()
	t = yelp.business(id=r['businesses'][0]['id'])
	
		
	
