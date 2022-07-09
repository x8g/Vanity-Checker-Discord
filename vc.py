# Creator: x8g
# 7/8/22
# ily!

import requests, os, threading, random
from colorama import Fore

ips = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text.splitlines()
def proxys():
    global proxyss
    threading.Timer(3.05, proxys).start()
    proxyss = random.choice(ips)
# proxys!
vanity = input(f"What vanity do you want to check?: ")
threads = input(f"Threads?: ")
os.system(f'title Vanity Checker ^| Threads: ' + threads)
reqsent = 0

    

# ---
def check():
    global reqsent
    global proxyss
    while True:
        r = requests.get(f'https://discord.com/api/v9/invites/{vanity}', proxies={"http":proxyss})
        if 'vanity_url_code' in (r.text):
            reqsent +=1
            print(Fore.RED + "invite link taken: " + vanity + " | Requests Sent: " +str(reqsent))
            os.system(f'title checking: ' + vanity + ' ^| Status: taken' + ' ^| github/x8g')
        if 'Unknown Invite' in (r.text):
            reqsent +=1
            print(Fore.GREEN + "invite link claimable or termed: "+ vanity + " | Requests Sent: " +str(reqsent))
            os.system(f'title checking: ' + vanity + ' ^| Status: avail/termed' + ' ^| github/x8g')
        if 'Access denied' in (r.text):
            print(Fore.RED + f"Cloudfare has blocked this IP.")
        if 'retry_after' in (r.text):
            print(Fore.RED + f"Rate limited please wait.")
proxys()

while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
