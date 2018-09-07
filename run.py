import requests
import webbrowser
from io import open as iopen
import urllib.request as request
import time


r = requests.get('https://xkcd.com')


# get website html
with open('test.html', 'w') as test:
    test.write(r.text)

with open('test.html') as f:
    read_data = f.read()


# get html tags with comic url
block = ""

for chunk in read_data.split("</"):
    if '<div id="comic">' in chunk:
        block = chunk
        break


# get source block for image url
image = ""

for tag in block.split(">"):
    if '<img src=' in tag:
        image = tag
        break

# get image url
image_url = ""

for tag in image.split("\""):
    if '//imgs.xkcd.com/comics/' in tag:
        image_url = tag
        break

image_url = "https://" + image_url[2:]


# get title block for comic
title = ""

for tag in block.split(">"):
    if 'title=' in tag:
        title = tag
        break

for tag in image.split("\""):
    if 'title=' in tag:
        title = tag
        break

print(title)


date = time.strftime("%d_%m_%Y")

# pull image and name it with the date
request.urlretrieve(image_url, "images/comic_" + date + ".png")
