import json

class Building:
    def __init__(self, DRIVER, id) -> None:
        self.id = DRIVER.execute_script(f'return Game.ObjectsById[{id}].id')
        self.bulkPrice = DRIVER.execute_script(f'return Game.ObjectsById[{id}].bulkPrice')
        self.amount = DRIVER.execute_script(f'return Game.ObjectsById[{id}].amount')
        self.storedCps = DRIVER.execute_script(f'return Game.ObjectsById[{id}].storedCps')
        self.globalCpsMult = DRIVER.execute_script(f'return Game.globalCpsMult')
        self.locked = DRIVER.execute_script(f'return Game.ObjectsById[{id}].locked')
        self.DRIVER = DRIVER
    
    def cps(self):
        return (self.getStoredCps())*self.getGlobalCpsMult()
    
    def buyValue(self):
        return self.cps() / self.bulkPrice

    def getId(self):
        self.id = self.DRIVER.execute_script(f'return Game.ObjectsById[{self.id}].id')
        return self.id
    
    def getBulkPrice(self):
        self.bulkPrice = self.DRIVER.execute_script(f'return Game.ObjectsById[{self.id}].bulkPrice')
        return self.bulkPrice
    
    def getAmount(self):
        self.amount = self.DRIVER.execute_script(f'return Game.ObjectsById[{self.id}].amount')
        return self.amount

    def getStoredCps(self):
        self.storedCps = self.DRIVER.execute_script(f'return Game.ObjectsById[{self.id}].storedCps')
        return self.storedCps

    def getGlobalCpsMult(self):
        self.globalCpsMult = self.DRIVER.execute_script('return Game.globalCpsMult')
        return self.globalCpsMult

    def getLocked(self):
        self.locked = self.DRIVER.execute_script(f'return Game.ObjectsById[{self.id}].locked')
        return self.locked