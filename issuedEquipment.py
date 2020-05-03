import pymysql
from baseObject import baseObject
from user import userList
from equipment import equipmentList
from datetime import datetime
class issuedEquipmentList(baseObject):
    def __init__(self):
        self.setupObject('IssuedEquipmentTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        eq = equipmentList()
        EquipmentID = self.data[n]['EquipmentID']
        eq.getById(EquipmentID)
        EquipmentName = eq.data[0]['EquipmentName']
        
        u = userList()
        UserID = self.data[n]['UserID']
        u.getById(UserID)
        UserFName = u.data[0]['UserFName']
        UserLName = u.data[0]['UserLName']
        
        if len(self.data[n]['EquipmentStatus']) == 0:
            self.errorList.append("Equipment Status Required.")
        else:
            self.data[n]['EquipmentStatus'] = self.data[n]['EquipmentStatus']

        if len(self.errorList) > 0:
            return False
        else:
            return True