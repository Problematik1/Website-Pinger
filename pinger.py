from colorama import Fore, init
import requests
import os
init()
os.system('title Pinger')
os.system('mode 55, 25')
color = Fore.LIGHTWHITE_EX
downed = Fore.RED
connected = Fore.LIGHTGREEN_EX
url = input(f'{color} Url: ')
os.system(f'title Pinging ~{url}~ ')
while True:
 r = requests.get(url)
 if r.status_code == 200:
     print(f'{connected} Connected: {r.status_code}')
 elif r.status_code != 200:
     print(f'{downed} Connection timed out: {r.status_code}')    

