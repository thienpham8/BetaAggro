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
	results = y.search(term="", location="San Fransisco, CA", limit=40)
	for i in xrange(0, len(results['businesses'])):
		businessListing = results['businesses'][i]
		business = y.business(id=businessListing['id'])

		c.addYelpBusiness(business)
	
	c.close()