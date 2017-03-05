#!/usr/bin/env python
# Created by: Zac Smith      
# 2017-1-31                        

# Use this line to set PATH to the virtual environment ---------- #
import runEnv
# --------------------------------------------------------------- #

import json
import sys
import requests
import urllib
import flask
from requests_oauthlib import OAuth1

import dbConnector


class YelpAPI(object):
	"""This class handles the Yelp API"""

	def __init__(self):
		"""Initialize some class attributes"""
		self.response = None
		self.searchURL = "https://api.yelp.com/v2/search/?"
		self.businessURL = "https://api.yelp.com/v2/business/"
		self.credentials = json.loads(open("credentials.json").read())
		self.auth = OAuth1(self.credentials["yelp"]["key"], self.credentials["yelp"]["kSecret"], 
													self.credentials["yelp"]["token"], self.credentials["yelp"]["tSecret"])

	def search(self, term="CSUEB", location="Hayward", limit=40, addToDB=True, verbose=False):
		"""URL encodes search term and location of search and returns a JSON dictionary response"""
	
		encoded = urllib.urlencode({"term" : term, "location" : location, "limit" : limit}) # maximum limit allowed by Yelp is 40
		response = requests.get(self.searchURL+encoded, auth=self.auth)
		
		self.response = response.json()
		
		if addToDB:
			try:
				c = dbConnector.Connector()
				for x in xrange(0, len(self.response["businesses"])):
					r = c.addYelpBusiness(self.response["businesses"][x])
					if verbose: print r
					
					if self.response["businesses"][x].get("categories", "") is not "":
						r = c.addCategory(self.response["businesses"][x]["id"], 
								self.response['businesses'][x]["categories"][0])
						if verbose: print r
					
					if self.response["businesses"][x].get("location", "") is not "":
						r = c.addLocation(self.response["businesses"][x])
						if verbose: print r
					
					if self.response["businesses"][x].get("id", "") is not "":
						r = c.addReview(self._business(self.response["businesses"][x]["id"]), site="yelp")
						if verbose: print r
					
			except:
				print "Error during yelpAPI.search()'s addToDB logic."
				print "Error: ", sys.exc_info()[0]
			
			finally:
				c.close()
		
		# returns a python dictionary of the JSON response
		return self.response
		
		
	def _business(self, id="california-state-university-east-bay-hayward"):
	
		try:
			response = requests.get(self.businessURL+id, auth=self.auth).json()		
		except requests.exceptions.ConnectionError as e:
			response = "error"
			
		finally:
			return response

		
		
# ------ Script executed below ------ #
if __name__ == "__main__":
	yelp = YelpAPI()
	r = yelp.search(term="", location="Hayward,  CA", limit=40)
	
