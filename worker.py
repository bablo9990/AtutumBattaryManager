import json
import subprocess, os

from psutil import sensors_battery

battery = sensors_battery()
with open('config.json', 'r') as f:
   params_json = f.read()
   f.close()
params = json.loads(params_json)
developer_percent = 14
import keyboard

def developer():
    os.system('powershell Start-Process "shutdown /a" -Verb RunAs')

keyboard.add_hotkey('Ctrl + 1', developer)


while True:
    if battery.percent < int(params["Default EWP"]) or developer_percent < int(params["Default EWP"]):
        os.system('shutdown /s /t 60 /c "Atutum saves documents!"')
    keyboard.wait('Ctrl + Q')