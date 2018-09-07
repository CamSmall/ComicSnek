import requests
import webbrowser

r = requests.get('https://xkcd.com')

with open('test.html', 'w') as test:
    test.write(r.text)

with open('test.html') as f:
    read_data = f.read()

for word in read_data.split():
    if 'https://xkcd.com/' in word:
        address = word
        break

address = address[:-3]
print(address)

webbrowser.open(address)
