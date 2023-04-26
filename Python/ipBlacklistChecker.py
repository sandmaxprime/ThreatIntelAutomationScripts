#Requires Python3
'''
Created by Lionel Faleiro
'''

import socket
import os
import requests as r
from bs4 import BeautifulSoup
import time
from tabulate import tabulate


filename = 'iplist.txt'
finalop = 'statuslist.txt'

print("\n Checking")

fname = open(filename)
fop = open(finalop,"a")
fop.write("IP,Blacklist\n")

for line in fname:
    wIP = line.strip()
    try:
        response = r.post('https://www.iplookuptools.com/ip-blacklist-check/',data={'ipaddress':wIP,'submit_ip':'Submit'}).text
        time.sleep(0.5)
        soup = BeautifulSoup(response,'lxml')
        table = soup.find("table")
        Status = str(table.find(text='IP ADDRESS IS BLACKLISTED'))
        print(wIP+","+Status)
        fop = open(finalop,"a")
        fop.write(wIP+","+Status+"\n")
        fop.close()
    except Exception as e:
        print(e)
        print(f"No response for {wIP}")
fname.close()
fop.close()
