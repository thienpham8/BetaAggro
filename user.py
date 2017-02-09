#K.Koltermann
import os
import sys
import const #should have a constant file

#should not store password in user object
class user(Object):
    userCount = 0
    def __init__(self,username):
        self.username = username
        self.zipcode = "00000" #no zipcode
        self.email = "NONE"
        self.favorites = []
        self.phoneNumber = "NONE"
        userCount += 1

    def addFavorite(self,link):
        self.favorites.append(link)

    def resetDefault(self):
        self.zipcode = "00000" #no zipcode
        self.email = "NONE"
        self.favorites = []
        self.phoneNumber = "NONE"

#TODO: ADD MORE SHIT
        
        
