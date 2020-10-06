# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1:
    #url = "http://py4e-data.dr-chuck.net/known_by_Elyssa.html"
     url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

intcount = int(input ("Enter Count: "))
intposition = int(input ("Enter Position: "))

# Retrieve all of the anchor tags
tags = soup('a')

    # print(tag.get('href', None))

counter = 0

print (url)
while counter < intcount:
    poscounter = 0
    counter = counter +1
    for tag in tags:
        poscounter = poscounter + 1
        if poscounter == intposition:
            #print("Poscounter",poscounter, "Intposition",intposition)
            print(tag.get('href', None))
            url = tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            urlsaved = tag.get('href', None)


print("URL Saved",urlsaved)
print(re.findall('by_(.+).html',urlsaved))
