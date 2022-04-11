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
OPTIONS:

[1] CARS WALLPAPERS
[2] CLEAN WALLPAPERS
[3] ANIME WALLPAPERS
[4] RANDOM WALLPAPERS
[5] RANDOM WALLPAPERS

""")

option = input(Fore.LIGHTRED_EX +"option => ")
hookurl = input(Fore.LIGHTRED_EX +"webhook url => ")

webhook = f"{hookurl}"


if option == "1" :
    while True:

        url = requests.get("https://wallhaven.cc/api/v1/search?q=cars&resolutions=1920x1080&sorting=random")

        text = url.text

        data = json.loads(text)

        hook = {
            "username" : "wallpaper generator",
            "content" : data['data'][0]['path']
        }
        print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
        time.sleep(5.0)
        result = requests.post(webhook, json = hook)

if option == "2" :
    while True:

        url = requests.get("https://wallhaven.cc/api/v1/search?q=clean&resolutions=1920x1080&sorting=random")

        text = url.text

        data = json.loads(text)

        hook = {
            "username" : "wallpaper generator",
            "content" : data['data'][0]['path']
        }
        print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
        time.sleep(5.0)
        result = requests.post(webhook, json = hook)

if option == "3" :
    while True:

        url = requests.get("https://wallhaven.cc/api/v1/search?categories=010&purity=110&resolutions=1920x1080&sorting=random")

        text = url.text

        data = json.loads(text)

        hook = {
            "username" : "wallpaper generator",
            "content" : data['data'][0]['path']
        }
        print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
        time.sleep(5.0)
        result = requests.post(webhook, json = hook)

if option == "4" :
    while True:

        url = requests.get("https://tokyo.tokyocity.repl.co/wallpaper")

        text = url.text

        data = json.loads(text)

        hook = {
            "username" : "wallpaper generator",
            "content" : data['wpp']
        }
        print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
        time.sleep(5.0)
        result = requests.post(webhook, json = hook)

if option == "5" :
    while True:

        url = requests.get("https://wallhaven.cc/api/v1/search?sorting=random&resolutions=1920x1080")

        text = url.text

        data = json.loads(text)

        hook = {
            "username" : "wallpaper generator",
            "content" : data['data'][0]['path']
        }
        print(Fore.LIGHTGREEN_EX +"[!] GENERATING... PLEASE WAIT!")
        time.sleep(5.0)
        result = requests.post(webhook, json = hook)  
