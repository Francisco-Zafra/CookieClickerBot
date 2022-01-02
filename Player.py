from time import time
from Building import Building
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
import datetime
from Upgrade import Upgrade

class Player:
    def __init__(self, driver, saveManager) -> None:
        self.DRIVER : WebDriver = driver
        self.saveManager = saveManager
        self.autoSave = 60
        self.cookies = driver.execute_script('return Game.cookies')
        self.lastAutoBuy = time()

    def play(self):
        user = self.DRIVER.find_element_by_xpath('//*[@id="bigCookie"]')
        try:
            user.click()
        except:
            return
    
    def buyDecider(self):
        bestValue = 0
        bestId = -1
        bestBuild = None
        upg = Upgrade(self.DRIVER)
        upg.buyUnlockedNotBought()
        for i in range(self.DRIVER.execute_script('return Game.ObjectsById.length')):
            build = Building(self.DRIVER, i)
            if build.getLocked() == 0:
                if build.buyValue() > bestValue:
                    bestValue = build.buyValue()
                    bestId = i
                    bestBuild = build
                else:
                    break

        if bestId != -1 and bestBuild.bulkPrice < self.getCookies():
            self.DRIVER.execute_script(f'Game.ObjectsById[{bestId}].buy()')
            return {'bestId':bestId, 'comprado':True}
        if bestId != -1:
            return {'bestId':bestId, 'comprado':False}
        return {'bestId':-1, 'comprado':False}
    
    def autoBuy(self, intervalo):
        idB = None
        if time() - self.lastAutoBuy >= intervalo:
            try:
                idB = self.buyDecider()
                while idB['comprado']:
                    print(f"Comprado: {idB} | {datetime.datetime.now()}")
                    idB = self.buyDecider()
            except:
                pass
            self.lastAutoBuy = time()
        return idB
    def getCookies(self):
        self.cookies = self.DRIVER.execute_script('return Game.cookies')
        return self.cookies