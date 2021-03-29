
from tkinter import *
import picamera
from time import sleep
import time
from PIL import ImageTk, Image
import picamera
import cv2
import numpy as np
import argparse
import math
from tkinter import BOTH, LEFT,FLAT,SUNKEN,RAISED,GROOVE,RIDGE
from tkinter import filedialog
import calendar
import datetime

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
       # Create window with freedom of dimensions
       
def check():
    image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/image2.jpg')
    xdl=460
    ydl=770
    cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
    cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)
        
    xdl=460
    ydl=1200

    cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
    cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
    cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)# Read image

    resize = ResizeWithAspectRatio(image, width=300) # Resize by width OR
    #resize = ResizeWithAspectRatio(image, height=300) # Resize by height 

    
    winname = "Test"
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, 40,30)  # Move it to (40,30)
    cv2.imshow(winname, resize)
    cv2.waitKey()
    cv2.destroyAllWindows()


root= Tk()

root.wm_title("Color Image Measure by GPERD")
root.configure(bg='LightSteelBlue3')
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

button4 = Button(root, text="CHECK", fg="purple",font=("Helvetica", 12), bg='green',command=check,borderwidth=3).place(x=10,y=10)


root.mainloop()