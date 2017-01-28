# http://stackoverflow.com/questions/20211990/sending-data-curl-json-in-python

import requests            #pip install requests
import simplejson as json  #pip install simplejson
import time
import random

def executeSomething():
    #code here
    #tfile = open("/sys/bus/w1/devices/10-000802824e58/w1_slave")
    #text = tfile.read()
    #tfile.close()
    #temperature_data = text.split()[-1]
    #temperature = float(temperature_data[2:])
    #temperature = temperature / 1000

    url = "http://localhost:3030"
    widget = "synergy1"
    temp = random.randint(0,100)
    #print(temp)
    data = {"auth_token": "YOUR_AUTH_TOKEN", "value": temp}

    fullUrl = "%s/widgets/%s" % (url, widget)
    headers = {'Content-type': 'application/json'}
    requests.post(fullUrl, data=json.dumps(data), headers=headers)
    time.sleep(1)

while True:
    executeSomething()