import pymysql
from baseObject import baseObject
from user import userList
from equipment import equipmentList
from datetime import datetime
from user import userList
from equipment import equipmentList
from datetime import datetime
class issuedEquipmentList(baseObject):
    def __init__(self):
        self.setupObject('IssuedEquipmentTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        EquipmentID = self.data[n]['EquipmentID']
        UserID = self.data[n]['UserID']
        eq = equipmentList()
        eq.getById(EquipmentID)
        EquipmentName = eq.data[0]['EquipmentName']
        
        u = userList()
        u.getById(UserID)
        UserFName = u.data[0]['UserFName']
        
        now = datetime.now()
       
        prefix_text = UserFName + '\'s review of "' + EquipmentName + '".  Reviwed on ' + str(now) + ' '
        
        if len(self.data[n]['review']) == 0:
            self.errorList.append("Review body cannot be blank.")
        else:
            self.data[n]['review'] = prefix_text + self.data[n]['review']

        if len(self.errorList) > 0:
            return False
        else:
            return True
    def getByUser(self,id):
    
        sql = '''SELECT * FROM `IssuedEquipmentTable` 
        LEFT JOIN `equipmentTable` ON `equipmentTable`.`EquipmentID` = `IssuedEquipmentTable`.`EquipmentID`
        WHERE  `IssuedEquipmentTable`.`UserID` = %s'''
        tokens = (id)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        self.log(sql,tokens)
        cur.execute(sql,tokens)
        self.data = []
        for row in cur:
            self.data.append(row)