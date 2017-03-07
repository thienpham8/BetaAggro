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

class GoogleAPI(object):
	"""This class handles the Google Places API"""		
	
	def __init__(self):
		self.key = json.loads(open("credentials.json").read())["google"]["key"]
		
		
	def _getPlaceID(self, search):
	
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
		query = urllib.urlencode({"query" : search, "key" : self.key})
		response = requests.get(url+query)

		try:
			return response.json()["results"][0]["place_id"]
		except:
			print sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
			return 0
		
	def getRating(self, search):
		
		id = self._getPlaceID(search)
		if id == 0:
			return 0
		url = "https://maps.googleapis.com/maps/api/place/details/json?"
		query = urllib.urlencode({"placeid" : id, "key" : self.key})
		response = requests.get(url+query).json()
		return (response["result"].get("rating", 0), response["result"]["reviews"])
		
	
# ------------------------------------- #
	
if __name__ == "__main__":

	print "Do not run this script! This is a class for import only."