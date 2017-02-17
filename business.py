#K.Koltermann
import os
import sys
import const
import dbConnector


class BusinessFactory(Object):
	def __init__(self, criteria):
		self.criteria
		pass
		
	def buildBusiness(self, criteria):
		pass # return list of built businesses
		

class Business(Object):
    def __init__(self):
	
		self.baID = betaaggroID
		self.address = 
		self.phone = phone
		self.lattitude = lattitude
		self.longitude = longitude
		self.yID = yID # Not sure we would need this
		self.yRatingImage = yRatingImage
		self.yReviewCount = yReviewCount
		self.yRatingImageSmall = yRatingImageSmall
		self.yURL = yURL
		self.isClosed = isClosed
		self.ySnippet = ySnippet
		self.yImageURL = yImageURL
		self.ySnippetURL = ySnippetURL
		self.yUniqueName = yUniqueName # Not sure we would need this
		
		self.name = name
        self.userClaimed = None # <---- The value for this should be a User object
        self.yelpRating = 0
		self.googleRating = 0
		self.facebookRating = 0
		self.betaAggroRating = 0
        self.cost = const.COST # Z: What is this for?
		self.locked = False # Z: What is this for?

    def getInfo(self):
        a = [self.businessName,self.ID,self.address,self.zipcode,self.rating,self.cost]
        return a

    def allowClaimed(self,username):
        self.userClaimed.append(username)
        self.claimed = True

    def denyClaimed(self,username):
        if username in self.userClaimed():
            self.userClaimed.remove(username)
        #failsafe
        else:
            self.userClaimed = []
            self.claimed = False
        if not self.userClaimed:
            self.claimed = False

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True
	



        
        
