import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import socket
from datetime import datetime
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys, getopt

chrome_options = Options()
#chrome_options.add_argument("--headless")

verify = "https://rollbit.com/rlb/lottery/provably-fair"

def open_rollbit_lottery_entries():
    print("Opening Chrome to Rollbit Lottery Entries")   
    browser.get(verify)
    time.sleep(3)

    #Scroll down, does not work otherwise
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    #Show more button, can't be headless or does not work
    more = browser.find_element_by_class_name("css-d9qtyc")
    more.click()
    time.sleep(2)

    #Grab lottery entry data and write to file
    elem = browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div[3]/pre[2]")
    file1 = open("lottery_entries.json", "w",  encoding="utf-8") 
    file1.write(elem.text)
    file1.close() 
    
#Use headless chromedriver for browser
browser = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
#browser = webdriver.Chrome()

#Check if using VPN based on current IP
h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

vpn = True

#Check if you are connected to a vpn
if vpn == True:
    if '192.168' in IP_address :
        print("VPN disconnected...")
    else:
        print("VPN active")
        open_rollbit_lottery_entries()
else:
    open_rollbit_lottery_entries()

browser.quit()