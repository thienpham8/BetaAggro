#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-16
# -------------------------- #

# TO DO: populate other related tables

import yelp
import dbConnector

if __name__ == "__main__":
	y = yelp.YelpAPI()
	c = dbConnector.Connector()
	
	searches = ["food", "restaurant", "mechanic", "Walgreens", "Walmart", "Gas Station", "Grocery Store", "Save Mart", "Fast Food", "Pool Service", "Landscaper", "Handyman"]
	
	for s in searches:
		results = y.search(term=s, location="San Fransisco, CA", limit=40)
		for i in xrange(0, len(results['businesses'])):
			businessListing = results['businesses'][i]
			business = y.business(id=businessListing['id'])

			c.addYelpBusiness(business)
			
	c.close()