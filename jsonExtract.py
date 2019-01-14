import json
import urllib.request, urllib.parse, urllib.error


serviceurl = input("Enter URL: ")
if len(serviceurl) < 1:
    serviceurl = "http://py4e-data.dr-chuck.net/comments_42.json"
    # serviceurl = "http://py4e-data.dr-chuck.net/comments_146683.json"

from urllib.request import urlopen

from urllib.request import urlopen

with urlopen(serviceurl) as conn:
    # while True:
    print ("Retrieving", serviceurl)
    url = urllib.request.urlopen(serviceurl)

    data = url.read()

    print ("Retrieved",len(data), "characters")
    # print(data.decode())

    info = json.loads(data.decode())
    print ('User count:', len(info['comments']))
    print(info['comments'])
    # print(info)

    for item in info['comments']:
        # print('Name',info['comments'][item])
        # print('Count',item["comments"][0]["count"])
        print(item)