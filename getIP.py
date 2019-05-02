#Requires Python3
'''
Created by Lionel Faleiro

2-May-2019
Added Error Handling
Added Copy to Clipboard functionality

'''


import socket
import os
import pyperclip

filename = 'urllist.txt'
filenameo = 'extractedips.txt'
finalop = ''

#Checks if the OP File exists and recreates
if os.path.exists(filenameo):
    print('Recreating OP File')
    os.remove(filenameo)

fname = open(filename)

#Extracted IPs will be appended to this file
fout = open(filenameo,'a')

#Iterates over the input url list
for line in fname:
    # Strips trailing whitespaces
    url = line.rstrip()
    #splits the URL on the basis of the /
    urltoken = url.split('/')
    #domain stores the part after :// to /
    domain = urltoken[2]
    # Checks the presence of www in the domain name
    if domain.find('www') == -1:
        domain = domain
    else:
        # If www is present in Domain name, it extracts it.
        domain = urltoken[2].split('www.')
        domain = domain[1]
    print('Domain Name: ',domain)
    try:
        iptuple = socket.gethostbyname_ex(domain)
        #iptuple is a tuple where [2] is a list of ips
        for i in iptuple[2]:
            print(i)
            finalop = finalop + '\n' + i
            fout.write(i + '\n')
    except:
        print('Can not fetch IP for ',domain)
    
fname.close()
fout.close()

pyperclip.copy(finalop)
