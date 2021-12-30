import PySimpleGUI as sg
from selenium import webdriver
from SaveManager import SaveManager
from time import sleep
from Player import Player

layout = [[sg.Text("Cookie Clicker")], [sg.Button("Play")]]

# Create the window
window = sg.Window("Cookie Clicker", layout, margins=(100,20))

# Inicializar variables
play = True
DRIVER = webdriver.Chrome()
saveManager = SaveManager(DRIVER)
player = Player(DRIVER, saveManager)

DRIVER.implicitly_wait(5)

DRIVER.get("https://orteil.dashnet.org/cookieclicker/")
sleep(1)

saveManager.loadGame()

# Create an event loop
while True:
    event, values = window.read(timeout=0)
    if event == "Play":
        play = not play
    if event == sg.WIN_CLOSED:
        break

    if play:
        player.play()

saveManager.saveGame()
DRIVER.close()
window.close()