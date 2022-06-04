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
chrome_options.add_argument("--headless")

rollbit_sports_by_price_low = "https://rollbit.com/rlb/lottery/current"

def open_rollbit_sports():
    print("Opening Chrome to Rollbit Lottery Results")   
    browser.get(rollbit_sports_by_price_low)
    time.sleep(10)

    #Grab Data
    elem = browser.find_elements_by_class_name("css-3p82s6")
    prizes = browser.find_elements_by_class_name("css-rc8k8e")

    x=len(elem)
    for i in range(x):
        el = elem[i]
        soup = BeautifulSoup(el.text, 'html.parser')
        lst = [0]
        var = []
        j = 0
        for pos,char in enumerate(str(soup)):
             if(char == '\n'):
                lst.append(pos)
                var.append(str(soup)[lst[j]+1:lst[j+1]])                
                j = j + 1

        #Print all results to terminal window. Does not seem to function properly if not included.
        print(var)
        print(prizes[i].text)
        
        d0.append(var[0])
        winner = var[1]
        if winner[:3] == "TEAM":
            d1.append(winner[7:])
        else:
            d1.append(winner)
        d2.append(prizes[i].text)        
        

#Use headless chromedriver for browser
browser = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
#browser = webdriver.Chrome()
d0 = []
d1 = []
d2 = []


#Sorting can be changed from "low" to "high"
sort = "low"

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
        open_rollbit_sports()
else:
    open_rollbit_sports()

#Create .csv file and column headers
df = pd.DataFrame({'Number': d0, 'Name': d1, 'Prize': d2})
#df.to_csv(str('sports_rollbots' + str(datetime.now().isoformat(timespec='minutes')) + '.csv'), index=False, encoding='utf-8')
df.to_csv('lottery_results.csv', index=False, encoding='utf-8')
browser.quit()