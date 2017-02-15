#K.Koltermann
import os
import sys
import const

class business(Object):
    def __init__(self,businessName,ID,address,zipcode):
        self.businessName = businessName
        self.description = "NONE"
        #ID = "0123456789 etc"
        self.ID = ID
        #Address = "STRING"
        self.address = address
        self.zipcode = zipcode
        self.userClaimed = ""
        self.claimed = False
        self.locked = False
        self.rating = const.RATING
        self.cost = const.COST

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



        
        
