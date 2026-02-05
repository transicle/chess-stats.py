from art import *
from stats import user_stats_exists, write_stat, read_stat
from client import start_discord_client

print("\033[1;96m", end="") 
tprint("chess.py", space=1)
print("\033[0m", end="")

if not user_stats_exists():
    chess_username = input(" What is your Chess.com username? \033[1m>>\033[0m ")
    chess_mode = input(" What mode do you want to track Elo for (\033[1;96mRapid\033[0m/\033[1;96mBlitz\033[0m/\033[1;96mBullet\033[0m)? \033[1m>>\033[0m ").lower()
    discord_token = input(" What is your Discord token? (\033[1mUsed for auth\033[0m) \033[1m>>\033[0m ");
    
    write_stat("username", chess_username)
    write_stat("mode", chess_mode)
    write_stat("token", discord_token)
    
    print()

start_discord_client()