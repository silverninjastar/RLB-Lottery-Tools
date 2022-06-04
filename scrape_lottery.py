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

def open_rollbit_sports():
    print("Opening Chrome to Rollbit Sportsbots Marketplace")   
    browser.get(verify)
    time.sleep(3)

    #Grab Data
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    more = browser.find_element_by_class_name("css-d9qtyc")
    more.click()
    print("clicked")
    time.sleep(2)
    elem = browser.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div[3]/pre[2]")
    #soup = BeautifulSoup(elem.text, 'html.parser')
    

        #Print all results to terminal window. Does not seem to function properly if not included.
    print(elem.text)
    out = elem.text
    output = out.replace("\"","\'")
    file1 = open("lottery_entries.json", "w",  encoding="utf-8") 
    file1.write(output)
    file1.close() 
    
#Use headless chromedriver for browser
browser = webdriver.Chrome("../chromedriver.exe",chrome_options=chrome_options)
#browser = webdriver.Chrome()

#Check if using VPN based on current IP
h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)

vpn = True

d0 = []
d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []
d9 = []
d10 = []
d11 = []

#Check if you are connected to a vpn
if vpn == True:
    if '192.168' in IP_address :
        print("VPN disconnected...")
    else:
        print("VPN active")
        open_rollbit_sports()
else:
    open_rollbit_sports()


'''
#Create .csv file and column headers
df = pd.DataFrame({'Name': d0, 'Rank': d1, 'Team?': d2, 'Leader ID': d3, 'Image': d4, 'Seed': d5, 'Staked': d6, 'Team Stake': d7, '# of Team Members': d8, 'User ID': d9, 'Team Leader?': d10, 'In Team?': d11})
#df.to_csv(str('sports_rollbots' + str(datetime.now().isoformat(timespec='minutes')) + '.csv'), index=False, encoding='utf-8')
df.to_csv('sports_rollbots.csv', index=False, encoding='utf-8')
'''

browser.quit()