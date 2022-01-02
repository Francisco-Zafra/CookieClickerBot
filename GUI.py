import PySimpleGUI as sg
from selenium import webdriver
from SaveManager import SaveManager
from time import sleep
from Player import Player
import json

layout = [[sg.Text("Cookie Clicker")], [sg.Button("Play")], [sg.Button("Buy"), sg.Text('Next: '), sg.Text(key='Building')]]

# Create the window
window = sg.Window("Cookie Clicker", layout, margins=(100,20))

# Inicializar variables
play = True
DRIVER = webdriver.Chrome()

DRIVER.implicitly_wait(5)

DRIVER.get("https://orteil.dashnet.org/cookieclicker/")
sleep(1)

saveManager = SaveManager(DRIVER)
player = Player(DRIVER, saveManager)

saveManager.loadGame()

# Create an event loop
while True:
    event, values = window.read(timeout=0)
    #Botones
    if event == "Play":
        play = not play
    if event == sg.WIN_CLOSED:
        break
    if event == "Buy":
        player.autoBuy(0)

    #click de la cookie
    if play:
        player.play()

    #Autosave
    saveManager.autoSave(60)
    # Compra de upgrades y buildings
    idB = player.autoBuy(30)
    if idB != None and idB['bestId'] != -1:
        window['Building'].update(DRIVER.execute_script(f'return Game.ObjectsById[{idB["bestId"]}].name'))
    
saveManager.saveGame()
DRIVER.close()
window.close()