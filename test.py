import requests
import time
import sys
import tkinter as tk
from PIL import ImageTk, Image
from web_client import Import

##################### SET GUI ######################
window = tk.Tk()

counter = tk.IntVar()
img = None
date = None
input = ""

def onClick():
    retrieve_input()
    print('Textbox Input: ' + input)
    global img
    img = getImage()

def retrieve_input():
    global input
    input = 'http://' + myText_Box.get("1.0",'end-1c')
    print('Textbox Input: ' + input)

def getImage():
    novi = tk.Toplevel()
    canvas = tk.Canvas(novi, width = 1920, height = 1080)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    Import.get(input)

    global date
    date = time.strftime("%d_%m_%Y")
    png = tk.PhotoImage(file="images/comic_" + date + ".png")
                                #image not visual
    canvas.create_image(50, 10, image = png, anchor = tk.NW)
    #assigned the png to the canvas object
    canvas.png = png


window.title('ComicSnek')
#window.geometry('450x300')
window.configure(background='grey')

myText_Box = tk.Text(window, height=10, width=30)
myText_Box.pack()
btn = tk.Button(window, text="Get Image", fg='green', command=onClick)
btn.pack()
btn = tk.Button(window, text="Exit", fg='red', command=quit)
btn.pack()

#Start the GUI
window.mainloop()
####################################################

#######################################
#from run import Import

#url = 'https://xkcd.com/799/'
#Import.get(url)
#######################################
