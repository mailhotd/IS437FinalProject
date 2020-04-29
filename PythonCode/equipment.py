import pymysql
from baseObject import baseObject
class equipmentList(baseObject):
    def __init__(self):
        self.setupObject('EquipmentTable')
        
    def verifyNew(self,n=0):
        self.errorList = []
        
        eq = equipmentList()
        eq.getByField('EquipmentName',self.data[n]['EquipmentName'])
        if len(eq.data) > 0:
            self.errorList.append("Item already exists in inventory.")
        
        if self.data[n]['NatoStockNumber'] == 0:
            self.errorList.append("Nato Stock Number is required.")
        if self.data[n]['NatoStockNumber'] < 13:
            self.errorList.append("Nato Stock Number must be 13 characters long.")
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def verifyChange(self,n=0):
        self.errorList = []
        
        eq = equipmentList()
        eq.getByField('EquipmentName',self.data[n]['EquipmentName'])
        #print(eq.data)
        if len(eq.data) > 0:
            print(self.data[n])
            print(eq.data[0])
            if str(self.data[n]['id']) != str(eq.data[0]['id']):
                self.errorList.append("Item already exists in inventory.")
        
        
        if self.data[n]['NatoStockNumber'] == 0:
            self.errorList.append("Nato Stock Number is required.")
        if self.data[n]['NatoStockNumber'] < 13:
            self.errorList.append("Nato Stock Number must be 13 characters long.")
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
        
    def tryLogin(self,email,pw):    
        #SELECT * FROM `EquipmentTable` WHERE `NatoStockNumber` = 1234567890000
        sql = 'SELECT * FROM `' + self.tn + '` WHERE `EquipmentName` = %s AND `NatoStockNumber` = %s;'
        tokens = (email,pw)
        self.connect()
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        #print(sql)
        #print(tokens)
        cur.execute(sql,tokens)
        self.data = []
        n=0
        for row in cur:
            self.data.append(row)
            n+=1
        if n > 0:
            return True
        else:
            return False
    