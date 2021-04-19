import random, string
import webbrowser
import time
import requests
import colorama
from colorama import Fore, init
import ctypes
from dhooks import Webhook, Embed
import dhooks
import sys
from datetime import datetime
init()
ctypes.windll.kernel32.SetConsoleTitleW("Hitler generator | by me <3")

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r'f"{Fore.GREEN}" +'[+]' + f"{Fore.RESET}" + f"{Fore.RED}" + 'Cargando... '+i + f"{Fore.RESET}")
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()


def clear():
    os.system('cls')
    return









print(f"{Fore.GREEN}" + """


██╗░░██╗██╗████████╗██╗░░░░░███████╗██████╗░
██║░░██║██║╚══██╔══╝██║░░░░░██╔════╝██╔══██╗
███████║██║░░░██║░░░██║░░░░░█████╗░░██████╔╝
██╔══██║██║░░░██║░░░██║░░░░░██╔══╝░░██╔══██╗
██║░░██║██║░░░██║░░░███████╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

""" + f"{Fore.RESET}")
print("Creado por mi <3")
print(f"{Fore.MAGENTA}" + "Ingresa la cantidad de codigos a crear y checkear" + f"{Fore.RESET}")
num=input(">")

f=open("Codigos.txt","w", encoding='utf-8')

print("Espera, creando " + num +" codigo/s")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()


with open("Codigos.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"{Fore.GREEN}" + "VALIDO | {} ".format(line.strip("\n")  + f"{Fore.RESET}"))
            break
        else:
        	print(f"{Fore.RED}" + "INVALIDO | {} ".format(line.strip("\n") + f"{Fore.RESET}"))
input("Presiona enter 5 veces para cerrar")
input("4")
input("3")
input("2")
input("1")


#si ves esto eres gay xd
