from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from time import time

class SaveManager:
    def __init__(self, driver) -> None:
        self.saveFileName : str = 'save'
        self.DRIVER = driver
        self.lastAutoSave = time()

    def loadGame(self):
        ActionChains(self.DRIVER).key_down(Keys.CONTROL).send_keys('o').key_up(Keys.CONTROL).perform()
        user = self.DRIVER.find_element_by_xpath('//*[@id="textareaPrompt"]')
        f = open("save", "r")
        user.send_keys(f.read())
        #open and read the file
        user = self.DRIVER.find_element_by_link_text('Load')
        user.click()
    
    def saveGame(self):
        #open save menu
        user : WebElement
        user = self.DRIVER.find_element_by_xpath('//*[@id="prefsButton"]')
        user.click()
        user = self.DRIVER.find_element_by_link_text('Export save')
        user.click()
        user = self.DRIVER.find_element_by_xpath('//*[@id="textareaPrompt"]')
        #write on file
        f = open("save", "w")
        f.write(user.text)
        f.close()
        #close menu
        user = self.DRIVER.find_element_by_xpath('//*[@id="prompt"]/div[2]')
        user.click()
        user = self.DRIVER.find_element_by_class_name('menuClose')
        user.click()
    
    def autoSave(self, intervalo):
        if time() - self.lastAutoSave >= intervalo:
            self.lastAutoSave = time()
            try:
                self.saveGame()
            except:
                pass
                