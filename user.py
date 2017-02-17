#Author: K.Koltermann 2/something/2017
import os
import sys
import const #should have a constant file

#should not store password in user object
class User(Object):
    userCount = 0
    def __init__(self,username):
        self.username = username
        self.zipcode = const.ZIPCODE
        self.email = const.EMAIL
        self.favorites = const.FAVORITES
        self.phoneNumber = const.PHONENUMBER
        self.lock = False
        userCount += 1

    def addFavorite(self,link):
        self.favorites.append(link)

    def resetDefault(self):
        self.username = username
        self.zipcode = const.ZIPCODE
        self.email = const.EMAIL
        self.favorites = const.FAVORITES
        self.phoneNumber = const.PHONENUMBER

    def changeUsername(self,newUsername):
        self.username = newUsername

    def lockAccount(self):
        self.lock = True

    def unlockAccount(self):
        self.lock = False

    def getAllInfo(self):
        a = [self.username,self.zipcode,self.email,self.favorites,self.phoneNumber]
        return a

        







        

#TODO: ADD MORE SHIT
