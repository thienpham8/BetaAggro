#Author: K.Koltermann 2/something/2017
import os
import sys
import const #should have a constant file
import dbConnector
import datetime
import time
import sys

#should not store password in user object

class User(object):
	def __init__(self, unicodeID="None", authenticated=False, active=False, anonymous=True,
							email="None", firstname="Bob", lastname="Saget", dob=0, zipcode=0, gender="None"):
		self.id = unicode(unicodeID)
		self.is_authenticated = authenticated
		self.is_active = active
		self.is_anonymous = anonymous
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.dob = dob
		self.zipcode = zipcode
		self.gender = gender
		
	def get_id(self):
		"""Flask-Login session requirement. returns user ID/Primary Key"""
		return self.id
		
	@classmethod
	def get(cls, unicodeID):
	
		try:
			c = dbConnector.Connector()
			user = c.loginUser(unicodeID)
			
			if user != None:
				return User(unicodeID=unicode(user["id"]), authenticated=True, active=True, anonymous=False,
									email=user.get("email", ""), firstname=user.get("firstname", ""), lastname=user.get("lastname", ""),
									dob=user.get("dob", 0), zipcode=user.get("zipcode", ""), gender=user.get("gender", ""))
									
			else:
				return None
		except:
			return None
		finally:
			c.close()
		
	def login(self, dic, registered=False):	
		"""Use DB to verify login and build user attributes"""
	
		try:
			if registered == False:
				c = dbConnector.Connector()
				user = c.loginUser(dic["username"], dic["password"])
			else:
				user = dic
			
			if user != None:
				self.id = unicode(user["id"])
				self.is_authenticated = True
				self.is_active = True
				self.is_anonymous = False
				self.email = user.get("email", "")
				self.firstname = user.get("firstname", "Bob")
				self.lastname = user.get("lastname", "Saget")
				self.dob = user.get("dob", 0)
				self.zipcode = user.get("zipcode", 0)
				self.gender = user.get("gender", "None")
				return True
			else:
				return None
				
			c.close()
			return
		except:
			return None
		finally:
			if registered == False: c.close()
	
	def register(self,dic):
		"""Registers new user with the database"""
		
		# try:
		c = dbConnector.Connector()
		date = datetime.datetime.strptime("{} {} {}".format(dic["DOBMonth"], dic["DOBDay"], dic["DOBYear"]), "%B %d %Y").toordinal()
		print "Date: ", date
		data = c.registerUser(dic["Username"], dic["Password"], (dic["Username"], dic["Password"], dic["Email"], dic["First name"], dic["Last name"], date, dic["Zip code"], dic["gender"]))
		
		if data != None:
			return self.login(data, registered=True)
		else:
			print "User.register reporting here: data is none :("
			
		# except:
			# print "User.register FAIL " + "*"*20
			# print sys.exc_info()[0]
			# print sys.exc_info()[1]
			# print sys.exc_info()[2]
			# print "User.register FAIL " + "*"*20
			# return None
			
		# finally:
			# c.close()
	
		




# Older USER object -- replaced by Flask User Class specifications
# class User(object):
    # userCount = 0
    # def __init__(self,username):
        # self.username = username
        # self.zipcode = const.ZIPCODE
        # self.email = const.EMAIL
        # self.favorites = const.FAVORITES
        # self.phoneNumber = const.PHONENUMBER
        # self.lock = False
        # userCount += 1

    # def addFavorite(self,link):
        # self.favorites.append(link)

    # def resetDefault(self):
        # self.username = username
        # self.zipcode = const.ZIPCODE
        # self.email = const.EMAIL
        # self.favorites = const.FAVORITES
        # self.phoneNumber = const.PHONENUMBER

    # def changeUsername(self,newUsername):
        # self.username = newUsername

    # def lockAccount(self):
        # self.lock = True

    # def unlockAccount(self):
        # self.lock = False

    # def getAllInfo(self):
        # a = [self.username,self.zipcode,self.email,self.favorites,self.phoneNumber]
        # return a

        







        

#TODO: ADD MORE SHIT
