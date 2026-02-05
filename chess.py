from typing import Literal
import requests

api_url = "https://api.chess.com/pub/player/"

def get_user_info(username: str):
    headers = {
        "User-Agent": "ChessStatTracker/1.0 (contact: transicle@duck.com)"   
    }
    resp = requests.get(f"{api_url}{username}/stats", headers=headers)
    if resp.status_code != 200:
        print(f"\n \033[91m\033[1m[!] \033[0mFailed to send request. (\033[93mError: {resp.status_code}\033[0m)")
        return None
    return resp.json()

def get_elo(username: str, mode: Literal["rapid", "blitz", "bullet"]):
    allowed = ["rapid", "blitz", "bullet"]
    if mode not in allowed:
        print(f"\n \033[91m\033[1m[!] \033[0mNot a valid mode! (\033[93mError\033[0m)")
        return None
    user_info = get_user_info(username)
    if not user_info:
        return None
    mode_key = f"chess_{mode}"
    if mode_key not in user_info:
        print(f"\n \033[91m\033[1m[!] \033[0mNo {mode} data for {username}! (\033[93mError\033[0m)")
        return None
    return user_info[mode_key]["last"]["rating"]