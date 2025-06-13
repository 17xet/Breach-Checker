import hashlib
import requests
import os
from colorama import Fore, Style, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

logo = [
    (Fore.WHITE + "  _                         _            _               _             " + Style.RESET_ALL),
    (Fore.WHITE + " | |                       | |          | |             | |            " + Style.RESET_ALL),
    (Fore.WHITE + " | |__  _ __ ___  __ _  ___| |__     ___| |__   ___  ___| | _____ _ __ " + Style.RESET_ALL),
    (Fore.WHITE + " | '_ \\| '__/ _ \\/ _` |/ __| '_ \\   / __| '_ \\ / _ \\/ __| |/ / _ \\ '__| " + Style.RESET_ALL),
    (Fore.WHITE + " | |_) | | |  __/ (_| | (__| | | | | (__| | | |  __/ (__|   <  __/ |   " + Style.RESET_ALL),
    (Fore.WHITE + " |_.__/|_|  \\___|\\__,_|\\___|_| |_|  \\___|_| |_|\\___|\\___|_|\\_\\___|_|   " + Style.RESET_ALL),
    (Fore.WHITE + " ┌─────────────────────────────────────────────────────────────┐ " + Style.RESET_ALL),
    (Fore.WHITE + " │ Discord User           " + Fore.RED + ":   " + Fore.WHITE + Fore.RED + "@" + Fore.WHITE + "17xet                           │ " + Style.RESET_ALL),
    (Fore.WHITE + " │ Discord Server         " + Fore.RED + ":   " + Fore.WHITE + Fore.RED + "@" + Fore.WHITE + "https://discord.gg/hKNW6wvyg3   │ " + Style.RESET_ALL),
    (Fore.WHITE + " │ Youtube                " + Fore.RED + ":   " + Fore.WHITE + Fore.RED + "@" + Fore.WHITE + "17xet                           │ " + Style.RESET_ALL),
    (Fore.WHITE + " └─────────────────────────────────────────────────────────────┘ " + Style.RESET_ALL),
]

for line in logo:
    print(line)

password = input(Fore.WHITE + "                   Enter a password (: " + Style.RESET_ALL)

hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
prefix = hashed_password[:5]
suffix = hashed_password[5:]

url = f"https://api.pwnedpasswords.com/range/{prefix}"

try:
    response = requests.get(url)
    response.raise_for_status()

    breached_passwords = response.text.splitlines()
    breach_info = {}

    for line in breached_passwords:
        hash_suffix, count = line.split(':')
        if hash_suffix == suffix:
            breach_info['count'] = int(count)
            break

    if 'count' in breach_info:
        print(Fore.RED + f"This password has been breached {breach_info['count']} times. It is not secure." + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "This password has not been breached. It is secure." + Style.RESET_ALL)

except requests.exceptions.RequestException as e:
    print(Fore.RED + f"An error occurred while checking the password {e}" + Style.RESET_ALL)

input(Fore.WHITE + "enter to exit" + Style.RESET_ALL)
