from time import time
import msvcrt
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver

class Player:
    def __init__(self, driver, saveManager) -> None:
        self.DRIVER : WebDriver = driver
        self.saveManager = saveManager
        self.autoSave = 60

    # def play(self):
    #     user = self.DRIVER.find_element_by_xpath('//*[@id="bigCookie"]')
    #     done = False
    #     end = False
    #     startTime = time()
    #     while not end:
    #         if msvcrt.kbhit():
    #             if msvcrt.getch() == b' ':
    #                 done = False
    #             if msvcrt.getch() == b'q':
    #                 end = True
    #         while not done:
    #             if time() - startTime > self.autoSave:
    #                 self.saveManager.saveGame()
    #                 startTime = time()
    #             try:
    #                 user.click()
    #             except:
    #                 break
    #             if msvcrt.kbhit():
    #                 if msvcrt.getch() == b' ':
    #                     done = True
    #                 if msvcrt.getch() == b'q':
    #                     end = True
    #                     done = True
    def play(self):
        user = self.DRIVER.find_element_by_xpath('//*[@id="bigCookie"]')
        try:
            user.click()
        except:
            return