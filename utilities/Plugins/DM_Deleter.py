# Coded / Dev / Owner: https://github.com/mukitan | https://github.com/mukitan/GANG-Nuker
# GANG Discord Nuker / Multi Tool ©
# Copyright © GANG-Nuker
#########################################################


import requests
from colorama import Fore

from utilities.Settings.common import *

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies=proxy(),
            headers=getheaders(token))
            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"\nERROR | {e}")
