import requests
import time
import sys
import tkinter as tk
from PIL import ImageTk, Image
from web_client import Import


url = 'https://xkcd.com/799/'

##################### SET GUI ######################
window = tk.Tk()
window.title("XKCD")
window.attributes("-fullscreen", True)
window.configure(background='grey')

date = time.strftime("%d_%m_%Y")
path = "images/comic_" + date + ".png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

button = tk.Button(window, text="Show Comic", fg="Green", command=Import.get(url))
button.pack(side=tk.TOP)

exit = tk.Button(window, text="Exit", fg="Red", command=quit)
exit.pack(side=tk.TOP)

#Start the GUI
window.mainloop()
####################################################
