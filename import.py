#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-16
# -------------------------- #

# TO DO: populate other related tables

import yelp
import dbConnector

if __name__ == "__main__":

	y = yelp.YelpAPI()
	c = dbConnector.Connector(verbose=True)
	
	searches = ["food", "restaurant", "mechanic", "Walgreens", "Walmart", "Gas Station", "Grocery Store", "Save Mart", "Fast Food", "Pool Service", "Landscaper", "Handyman", "pharmacy", "doctors", "dentist", "Chiropractor", "chinese", "italian", "pub", "american"]
	
	for s in searches:
		print s
		results = y.search(term=s, location="Hayward, CA", limit=40, addToDB=True, verbose=True)
		# for i in xrange(0, len(results['businesses'])):
			# businessListing = results['businesses'][i]
			# business = y._business(id=businessListing['id'])

			# print c.addYelpBusiness(business)
			
			# if businessListing.get("categories", "") is not "":
				# print c.addCategory(businessListing["id"], businessListing["categories"][0])
			
			# print c.addLocation(businessListing)

	c.close()