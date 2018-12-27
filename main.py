import json
import websocket

WS_URL = 'YOUR_URL'


def fizzbuzzmoi(n):
    ret = ''
    if n % 3 == 0:
        ret += 'Fizz'
    if n % 5 == 0:
        ret += 'Buzz'
    if n % 7 == 0:
        ret += 'Moi'
    if n % 3 > 0 and n % 5 > 0 and n % 7 > 0:
        ret = str(n)
    return ret

websocket.enableTrace(True)
ws = websocket.create_connection(
    WS_URL
)
ws.send('{"signal":"start"}')

while True:
    message = ws.recv()
    jsondic = json.loads(message)
    print(message)
    moi = fizzbuzzmoi(jsondic['number'])
    print(moi)
    ws.send('{"answer":"%s"}' % (moi,))
