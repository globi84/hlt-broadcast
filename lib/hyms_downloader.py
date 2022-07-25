
import sys
import urllib3
from webbrowser import get
import requests
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

urllib3.disable_warnings()

def get_webversion( url, regex, wait_for_class_name):
    """Get webversion form specific website"""
    web_page = ""
    # Get webpage
    try:
        page = requests.get(url, timeout=5, verify=False)
        if page.status_code == 200:
            web_page = page.text
    except:
        pass

    # Get Webversion
    if web_page:
        re_word = re.compile(regex)
        webversion = re_word.search(web_page)
        if webversion:
            return webversion[1]
        else:
            if wait_for_class_name:
                
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                
                path = os.path.dirname(os.path.realpath(__file__)) + "\\bin\\chromedriver.exe"
                service = Service(path)
                
                try:
                    browser = webdriver.Chrome(service=service, options=chrome_options)
                except:
                    return str(sys.exc_info()[1])

                browser.implicitly_wait(2)
                browser.get(url)
                #test = browser.find_elements(by=By.CLASS_NAME, value=wait_for_class_name)
                delay = 30 #seconds
                try:
                    myClass = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, wait_for_class_name)))
                    print("Page is Ready!")
                except TimeoutException:
                    print("Loading took too much time!")
                webversion = re_word.search(browser.page_source)
                browser.close()
            if webversion:
                return webversion[1]
            else:
                return "not found"
    else:
        return "error on the page"


a = get_webversion("https://www.churchofjesuschrist.org/study/manual/hymns?lang=deu", "href=\"(.*)\" id=\"li3\"", "songNumber-vZmKj")
#a = get_webversion("https://www.jetbrains.com/edu-products/download/other-PCE.html", "pycharm-edu-([0-9._]*)\.exe", "wt-link")

print(a)
