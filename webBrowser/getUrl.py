import sys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver

'''
перевое нужно  подготовить чтоб легко распарсить, 
а затем результат отдавать в json формате
'''

def loadSite(url, js, waitId):

    #print("init browser")
    #print(url)
    service_args = [
            '--proxy=192.168.56.100:9100',
            '--proxy-type=socks5',
            ]
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' \
            'AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/39.0.2171.95 Safari/537.36'


    browser = webdriver.PhantomJS(desired_capabilities=desired_capabilities, service_args=service_args)

    #print("del cookie and geting page")
    browser.delete_all_cookies()
    browser.set_page_load_timeout(60*3)
    #TO DO: создать exeption чтоб браузер закрывался
    try:
        browser.get(url) 

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

    except Exception as ex:
        print('Exeption in load:', ex)

    html =  browser.page_source
    #
    browser.close()
    browser.quit()

    return newUrl +  html
#####################################
#main################################
try:
    print (sys.argv[1])
    print('load')
    print("##bodystart##", loadSite(sys.argv[1] , False, False), "##bodyend##")
except IndexError:
    print('not set')



