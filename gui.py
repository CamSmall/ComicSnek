import requests
import tkinter as tk

##################### GET URL ######################
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
####################################################

##################### SET GUI ######################
root = tk.Tk()
# Code to add widgets will go here...

var = tk.StringVar()
label = tk.Label( root, textvariable=var, relief=tk.RAISED )

var.set(address)
label.pack()

root.mainloop()
####################################################
