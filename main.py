from selenium import webdriver
from SaveManager import SaveManager
from time import sleep
from Player import Player

DRIVER = webdriver.Chrome()
saveManager = SaveManager(DRIVER)
player = Player(DRIVER, saveManager)

DRIVER.implicitly_wait(5)

DRIVER.get("https://orteil.dashnet.org/cookieclicker/")
sleep(1)

saveManager.loadGame()
player.play()
saveManager.saveGame()

DRIVER.close()

