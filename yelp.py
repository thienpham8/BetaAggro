#!/usr/bin/env python
# Created by: Zac Smith      
# 2017-1-31                        

# Use this line to set PATH to the virtual environment
import runEnv
# --------------------------------------------------------------- #

import json
import requests
import urllib
import flask
from requests_oauthlib import OAuth1


class YelpAPI(object):
	"""This class handles everything with the Yelp API"""

	def __init__(self):
		"""Initialize some class attributes"""
		self.searchURL = "https://api.yelp.com/v2/search/?"
		self.credentials = json.loads(open("credentials.json").read())
		self.auth = OAuth1(self.credentials["key"], self.credentials["kSecret"], 
													self.credentials["token"], self.credentials["tSecret"])

	def search(self, term="CSUEB", location="Hayward", limit=10):
		"""URL encodes search term and location of search and returns a JSON dictionary response"""
	
		encoded = urllib.urlencode({"term" : term, "location" : location, "limit" : limit})
		response = requests.get(self.searchURL+encoded, auth=self.auth)
		
		rJSON = response.json()
		print json.dumps(rJSON, indent=4)
		
		return response
		

		
# ------ Script executed below ------ #
if __name__ == "__main__":
	yelp = YelpAPI()
	yelp.search(limit=1)
		
	
