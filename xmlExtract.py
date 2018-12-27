import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = input("Enter URL: ")
if len(serviceurl) < 1:
    serviceurl = "http://py4e-data.dr-chuck.net/comments_42.xml"

from urllib.request import urlopen

with urlopen(serviceurl) as conn:
    print ("Retrieving", serviceurl)
    url = urllib.request.urlopen(serviceurl)

tree = ET.parse(url)
root = tree.getroot()

counts = tree.findall ('.//count')

print ("Retrieved", counts, "characters")