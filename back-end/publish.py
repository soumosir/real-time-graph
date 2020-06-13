import json
import websocket

ws = websocket.WebSocket()

import random,time

ws.connect('ws://localhost:8000/ws/polData/')

for i in range(100):
    time.sleep(3)
    ws.send(json.dumps({'value':random.randint(1,100)}))
