import requests

r = requests.get('https://xkcd.com')

with open('test.html', 'w') as test:
    test.write(r.text)

# Permanent link to this comic: 
# GET THIS LINE ^ FOR THE LINK TO THE COMIC.


