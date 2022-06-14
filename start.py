import time
import json, requests 
from colorama import Fore, Style

print(Fore.LIGHTBLUE_EX +"""
____    __    ____  ___       __       __      .______      ___      .______    _______ .______      
\   \  /  \  /   / /   \     |  |     |  |     |   _  \    /   \     |   _  \  |   ____||   _  \     
 \   \/    \/   / /  ^  \    |  |     |  |     |  |_)  |  /  ^  \    |  |_)  | |  |__   |  |_)  |    
  \            / /  /_\  \   |  |     |  |     |   ___/  /  /_\  \   |   ___/  |   __|  |      /     
   \    /\    / /  _____  \  |  `----.|  `----.|  |     /  _____  \  |  |      |  |____ |  |\  \----.
    \__/  \__/ /__/     \__\ |_______||_______|| _|    /__/     \__\ | _|      |_______|| _| `._____|
                                                                                                     
  _______  _______ .__   __.  _______ .______          ___   .___________.  ______   .______         
 /  _____||   ____||  \ |  | |   ____||   _  \        /   \  |           | /  __  \  |   _  \        
|  |  __  |  |__   |   \|  | |  |__   |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |_)  |       
|  | |_ | |   __|  |  . `  | |   __|  |      /      /  /_\  \    |  |     |  |  |  | |      /        
|  |__| | |  |____ |  |\   | |  |____ |  |\  \----./  _____  \   |  |     |  `--'  | |  |\  \----.   
 \______| |_______||__| \__| |_______|| _| `._____/__/     \__\  |__|      \______/  | _| `._____|   
""")

print(Fore.LIGHTYELLOW_EX +"""
= OPTIONS:

- ANIME
- CLEAN
- CARS
- RANDOM
""")

option = input(Fore.LIGHTRED_EX +"option name => ")
hookurl = input(Fore.LIGHTRED_EX +"webhook url => ")
webhook = f"{hookurl}"

while True:
    url = requests.get(f"https://wallhaven.cc/api/v1/search?q={option}&resolutions=1920x1080&sorting=random")
    text = url.text
    data = json.loads(text)
    hook = {
        "username" : "wallpaper generator",
        "content" : data['data'][0]['path']
    }
    print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
    time.sleep(5)
    result = requests.post(webhook, json = hook)

