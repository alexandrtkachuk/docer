
import zmq
import time
import sys
import json
import datetime

import subprocess 
#print()
from pprint import pprint
context = zmq.Context()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    if(message == b'done'):
        print("good - end work")
        break;
    #  Do some 'work'
    time.sleep(1)
    try:
        jsonData = message.decode()
        data = json.loads(jsonData)
        pprint(data['url'])
        pprint(data['js'])

        r = subprocess.Popen(["python3", "getUrl.py", data['url']], stdout=subprocess.PIPE)
        html = r.stdout.read()

        #  Send reply back to client
    except Exception as ex:
        socket.send(b'none')
        print('Some Exeption:', ex)
    else:
        socket.send(html)
    print("waiting")
    print(datetime.datetime.now())


print("good\n")
