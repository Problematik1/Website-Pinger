from colorama import Fore, init
from requests.exceptions import Timeout
import requests
import os


init()
os.system('title Web Pinger')
os.system('mode 70, 30')
color = Fore.LIGHTWHITE_EX
downed = Fore.RED
connected = Fore.LIGHTGREEN_EX
url = input(f'{color} Url: ')
timeo = input(' Timeout: ')
succ = 0
errs = 0

while True:
 try:
     r = requests.get(url, timeo)
     if r.status_code == 200:
         succ += 1
         print(f'{connected} Connected')
     if r.status_code != 200:
         errs += 1
         print(f'{downed} Connection timed out')       
 except Timeout:
     print(f'{downed} Connection timed out') 
 os.system(f'title Success: {succ} │ Errors: {errs} │ ~{url}~')
     