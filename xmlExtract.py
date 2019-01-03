import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = input("Enter URL: ")
if len(serviceurl) < 1:
    # serviceurl = "http://py4e-data.dr-chuck.net/comments_42.xml"
    serviceurl = "http://py4e-data.dr-chuck.net/comments_146682.xml"

from urllib.request import urlopen

with urlopen(serviceurl) as conn:
    # while True:
    print ("Retrieving", serviceurl)
    url = urllib.request.urlopen(serviceurl)

    data = url.read()

    print ("Retrieved",len(data), "characters")
    print(data.decode())
    tree = ET.fromstring(data)

    intTotalCount = int()
    intTotalCount = 0

    for elem in tree.iter():
        if elem.tag == "count":
            print (elem.tag, elem.text)
            intTotalCount = intTotalCount + int(elem.text)
    
    print ("Total Count is", intTotalCount)
    # comments = tree.findall('comments')
    # print(comments[0].find('comment').find('count').text)
    # mycount = comments[0].find('count').text
    # print(mycount)
    
""" 
tree = ET.parse(url)
root = tree.getroot()

counts = tree.findall ('.//count')

print("There are",len(counts), "counts")

for child in root:
    print (child.tag, child.attrib)

for count in root.findall('comments'):
    mynum = comments.find('count').text
    print (count)
    print (mynum)
 """
# print ("Retrieved", counts, "characters")