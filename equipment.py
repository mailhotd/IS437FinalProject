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
        if len(self.data[n]['NatoStockNumber']) != 13:
            self.errorList.append("Nato Stock Number must be 13 characters long.")
        if len(self.errorList) > 0:
            return False
        else:
            return True
            
    def verifyChange(self,n=0):
        self.errorList = []
        
        eq = equipmentList()
        eq.getByField('EquipmentName',self.data[n]['EquipmentName'])
        if len(eq.data) > 0:
            print(self.data[n])
            print(eq.data[0])
            if str(self.data[n]['EquipmentID']) != str(eq.data[0]['EquipmentID']):
                self.errorList.append("Item already exists in inventory.")
        
        if  self.data[n]['NatoStockNumber'] == 0:
                self.errorList.append("Nato Stock Number is required.")
        if  len(self.data[n]['NatoStockNumber']) != 13:
                self.errorList.append("Nato Stock Number must be 13 characters long.")
        if len(self.errorList) > 0:
            return False
        else:
            return True