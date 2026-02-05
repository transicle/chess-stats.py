from stats import read_stat
from art import *
from discord import CustomActivity
from chess import get_elo
import discord
import os
import time
import logging

# https://github.com/dolfies/discord.py-self#quick-example
class MyClient(discord.Client):
    async def on_ready(self):
        os.system("cls || clear")
        print("\033[1;96m", end="") 
        tprint("chess.py", space=1)
        print("\033[0m", end="")
        print(" \033[1;96m[*]\033[0m Now managing your Discord account's status with your elo.")
        print(" \033[1;96m[*]\033[0m Press \"CTRL + C\" to stop the script.")
        
        mode = read_stat('mode')
        while True:
            time.sleep(1)
            await self.change_presence(activity=CustomActivity(emoji="♟️", name=f"{mode.title()}: {get_elo(read_stat("username"), mode)} • Chess.com"))

def start_discord_client():
    logging.getLogger('discord').disabled = True
    client = MyClient()
    client.run(read_stat("token"))