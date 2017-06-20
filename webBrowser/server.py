#!/usr/bin/python3

#zmq серевер который принимает url и вернет html , будет пока работать с tor

from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.proxy import *
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
#
import zmq
import time
import sys
import json
import datetime

from pprint import pprint


def loadSite(url, js, waitId):

    print("init browser")
    service_args = [
            '--proxy=127.0.0.1:9050',
            '--proxy-type=socks5',
            ]
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/39.0.2171.95 Safari/537.36'


    browser = webdriver.PhantomJS(desired_capabilities=desired_capabilities, service_args=service_args)

    print("del cookie and geting page")
    browser.delete_all_cookies()
    browser.set_page_load_timeout(60*3)
    #TO DO: создать exeption чтоб браузер закрывался
    try:
        browser.get(url)
    except Exception as ex:
        print('Exeption get url:', ex)

    if(js != False):
        print("run js")
        browser.execute_script(js)
    #print(browser.page_source)
    #infotab
    if(waitId != False ):
        print("wait")
        try:
            #может такого и не будет 
            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, waitId )))
        except Exception as ex:
            print("not found " + waitId)

    newUrl = browser.current_url
    print("we now:")
    print(browser.current_url)

    html =  browser.page_source
    #
    browser.close()
    browser.quit()

    return newUrl +  html 

#loadSite('http://myip.ru/')
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
        html = loadSite(data['url'], data['js'], data['waitId'])
        #  Send reply back to client
    except Exception as ex:
        socket.send(b'none')
        print('Some Exeption:', ex)
    else:
        socket.send(html.encode())
    print("waiting")
    print(datetime.datetime.now())


print("good\n")

