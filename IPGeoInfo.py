#Requires Pytho3
'''
Created by Lionel Faleiro
'''

import requests
import os

#Queries keycdn
url = "https://tools.keycdn.com/geo.json?host="

#input file needs  to  have each IP on a new line
filename =  'iplist.txt' 

#Output file will be autocreated
finalop =  'geolist.csv'
fw =  open(finalop,"w+")

#CSV delimiter  is |
fw.write("IP|Country|State|City|ISP\n")
fname = open(filename)
for line in fname:
    ip  = line.rstrip()
    #print(ip)
    try:
        r = requests.get(url=url+ip)
        data  = r.json()
        isp  = data['data']['geo']['isp']
        city  = data['data']['geo']['city']
        state  = data['data']['geo']['region_name']
        country  =  data['data']['geo']['country_name']
        print(str(ip)+","+str(country)+","+str(state)+","+str(city)+","+str(isp))
        fw.write(str(ip)+"|"+str(country)+"|"+str(state)+"|"+str(city)+"|"+str(isp)+"\n")
    except:
        print('Cannot find ip for',ip)

fname.close()
fw.close()     



