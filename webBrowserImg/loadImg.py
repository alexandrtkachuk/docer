#for loar in www
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import pycurl
from io import BytesIO
###################

import zmq
import time
import sys
import json
import datetime

#################################################
def loadImg(url):
    print("step1")

    service_args = [
        '--proxy=127.0.0.1:9050',
        '--proxy-type=socks5',
        ]

    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/39.0.2171.95 Safari/537.36'


    driver = webdriver.PhantomJS(desired_capabilities=desired_capabilities, service_args=service_args)
    driver.set_page_load_timeout(60*2) 
    driver.get(url)
    #save cookies
    mycookie = ''
    for item in driver.get_cookies():
        mycookie = mycookie +  item['name']+ '='+ item['value'] +  '; '

    #close driver
    driver.quit()

    #load img with curl
    header = ['User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
                                                                'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                                                'Chrome/39.0.2171.95 Safari/537.36',

                'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             ]

    #print(mycookie)
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(pycurl.HTTPHEADER, header)
    c.setopt(pycurl.PROXY, 'localhost')
    c.setopt(pycurl.PROXYPORT, 9050)
    c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    c.setopt(pycurl.COOKIE, mycookie)
    #c.setopt(pycurl.COOKIEJAR, 'cookie2.log')
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()
#################################################################################

context = zmq.Context()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

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
        url = message.decode()
        html = loadImg(url)
        #  Send reply back to client
    except Exception as ex:
        socket.send(b'none')
        print('Some Exeption:', ex)
    else:
        socket.send(html)
    print("waiting")
    print(datetime.datetime.now())


print("good\n")