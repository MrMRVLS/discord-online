#--GitHub.com/░█▀▄▀█ █▀▀█ ░█▀▄▀█ ░█▀▀█ ░█──░█ ░█─── ░█▀▀▀█--
#--------─────░█░█░█ █▄▄▀ ░█░█░█ ░█▄▄▀ ─░█░█─ ░█─── ─▀▀▀▄▄--
#---────---──-░█──░█ ▀─▀▀ ░█──░█ ░█─░█ ──▀▄▀─ ░█▄▄█ ░█▄▄▄█--
#--──-----──---------────-------──---──────-----------------

import config
import json
import time
import websocket
import requests

status = "online"
token = config.token

headers = {"Authorization": token, "Content-Type": "application/json"}
userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def keep_online(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 11","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    ws.send(json.dumps(auth))
    online = {"op":1,"d":"None"}
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps(online))

def run_keep_online():
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  while True:
    keep_online(token, status)
    time.sleep(30)

run_keep_online()