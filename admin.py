#author K.Koltermann 2/14/17
import os
import sys
import const
import utils
import database as db

class admin(Object):
    def __init__(self,name,adminCode):
        self.name = name
        self.adminCode = adminCode

        def getInfo(self,code):
            if db.checkAdminCode(code):
                info = [self.name, self.adminCode]
                return info

        def deleteBusiness(self,ID):
            db.removeBusiness(ID)

#Do we want admins?
