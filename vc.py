# Creator: x8g
# 7/8/22
# ily!

import requests, os, threading, random
from colorama import Fore
proxs = {
  "600",
  "700",
  "800",
  "900",
  "1000",
}
zt = Fore.MAGENTA
# ---
vanity = input(f"{zt}what vanity do you want to check?: ")
threads = input(f"{zt}Threads?: ")
proxytype = input(f"{zt}Proxy Type?: ")
# ---
prox = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxytype}&timeout={random.choice(list(proxs))}&country=all").text.splitlines()
# ---
os.system(f'title Vanity Checker ^| Threads: ' + threads)
proxysused = 0
proxyss = []
def proxys():
    global proxyss
    threading.Timer(1.05, proxys).start()
    proxyss = random.choice(prox)
# ---
def check():
    global proxysused
    while True:
        r = requests.get("https://discord.com/api/v9/invites/" + vanity)
        if r.status_code == 200:
            proxysused +=1
            print(Fore.RED + "invite link taken: " + vanity + " | Proxys Used: " +str(proxysused))
            os.system(f'title checking: ' + vanity + ' | Status: taken' + ' ^| github/x8g')
        if r.status_code == 401:
            proxysused +=1
            print(Fore.GREEN + "invite link claimable or termed: "+ vanity + " | Proxys Used: " +str(proxysused))
            os.system(f'title checking: ' + vanity + ' | Status: avail/termed' + ' ^| github/x8g')
        if r.status_code == 404:
            print(Fore.RED + "Rate limited!")
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
