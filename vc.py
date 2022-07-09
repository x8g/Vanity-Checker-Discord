# Creator: x8g
# 7/8/22
# ily!

import requests, os, threading, random
from colorama import Fore
zt = Fore.MAGENTA
# ---
vanity = input(f"{zt}what vanity do you want to check?: ")
threads = input(f"{zt}Threads?: ")
# ---
os.system(f'title Vanity Checker ^| Threads: ' + threads)
reqsent = 0
url = f'https://discord.com/api/v9/invites/{vanity}'

    

# ---
def check():
    global reqsent
    while True:
        r = requests.get(url)
        if 'vanity_url_code' in (r.text):
            reqsent +=1
            print(Fore.RED + "invite link taken: " + vanity + " | Requests Sent: " +str(reqsent))
            os.system(f'title checking: ' + vanity + ' ^| Status: taken' + ' ^| github/x8g')
        if 'Unknown Invite' in (r.text):
            reqsent +=1
            print(Fore.GREEN + "invite link claimable or termed: "+ vanity + " | Requests Sent: " +str(reqsent))
            os.system(f'title checking: ' + vanity + ' ^| Status: avail/termed' + ' ^| github/x8g')
        if 'retry_after' in (r.text):
            print(Fore.RED + f"Rate limited please wait.")
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
