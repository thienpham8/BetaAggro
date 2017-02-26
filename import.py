#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-16
# -------------------------- #

# TO DO: populate other related tables

import yelp
import dbConnector

if __name__ == "__main__":

	y = yelp.YelpAPI()
	print "yelp connected"
	c = dbConnector.Connector(verbose=True)
	print "connector connected"
	
	searches = ["food", "restaurant", "mechanic", "Walgreens", "Walmart", "Gas Station", "Grocery Store", "Save Mart", "Fast Food", "Pool Service", "Landscaper", "Handyman"]
	
	for s in searches:
		results = y.search(term=s, location="Santa Clarita, CA", limit=40, addToDB=False)
		for i in xrange(0, len(results['businesses'])):
			businessListing = results['businesses'][i]
			business = y._business(id=businessListing['id'])

			print c.addYelpBusiness(business)
			print c.addCategory(businessListing["id"], businessListing["categories"][0])
			print c.addLocation(businessListing)

	c.close()