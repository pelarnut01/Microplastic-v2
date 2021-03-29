import tkinter as tk
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
import threading
fillNum = ""
r1=0
g1=0
b1=0
r2=0
g2=0
b2=0
r3=0
g3=0
b3=0
r4=0
g4=0
b4=0
number1=0
databox=0
my_str=0


## X-axis and Y-axis Position sample##
ydl1=0
xdl1=0

## X-axis and Y-axis Position blank##
ydl2=0
xdl2=0


## data for formula ##

reds=0
greens=0
blues=0

redb=0
greenb=0
blueb=0

answer=0

camera = picamera.PiCamera()

camera.resolution = (1920, 1080)
camera.preview_fullscreen=False

camera.preview_window=(270,60, 350, 300)
camera.rotation = 270
camera.start_preview()
camera.awb_mode = 'cloudy'
camera.brightness = 50
def quit():
    
    global root
    root.destroy()
    camera.stop_preview()
    
def capture():
    global camera
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    camera.capture('/home/pi/Desktop/backup/Cam/photo/image2.jpg')
    camera.capture('/home/pi/Desktop/Image sample microplastic/'+'(Sample)'+date+'.jpg')
    
def capturebank():
    global camera
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    camera.capture('/home/pi/Desktop/backup/Cam/photo/blank.jpg')
    camera.capture('/home/pi/Desktop/Image sample microplastic/'+'(Blank)'+date+'.jpg')
    
    
def blank():
    global xdl2,ydl2
    sumred = 0
    sumgreen = 0
    sumblue = 0
    global r1,g1,b1
    global r2,g2,b2
    global r3,g3,b3
    global r4,g4,b4
    global redb,greenb,blueb
    image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/blank.jpg')
    
    xdl=xdl2
    ydl=ydl2
    #cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
    #cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)
    print("Top left")


    ##move dot up
    for i in range(10):
        
        b, g, r = image[xdl, ydl]
        ydl-=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot down   
    for i in range(10):
        
        b, g, r = image[xdl, ydl]
        ydl+=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot left
    for i in range(10):
        b, g, r = image[xdl, ydl]
        xdl-=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot right
    for i in range(10):
        b, g, r = image[xdl, ydl]
        xdl+=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
        
    redb = meanred1=(sumred/40)
    greenb = meangreen1=(sumgreen/40)
    blueb = meanblue1=(sumblue/40)

    r1 = meanred1=(sumred/40)
    g1 = meangreen1=(sumgreen/40)
    b1 = meanblue1=(sumblue/40)

    print("Meanred",redb)
    print("Meangreen",greenb)
    print("Meanblue",blueb)


   


    sumred=0 
    sumgreen=0
    sumblue=0
 
    
    
    display_time4()
    display_time5()
    display_time6()
    

    
    

    
def clear():
    global r1,g1,b1
    global r2,g2,b2
    global r3,g3,b3
    global r4,g4,b4
    r1=0
    g1=0
    b1=0
    r2=0
    g2=0
    b2=0
    r3=0
    g3=0
    b3=0
    r4=0
    g4=0
    b4=0
    

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

def streamon():
    camera.start_preview()
def streamoff():
    camera.stop_preview()
    
    

def check1():

    global ydl1,xdl1
    camera.stop_preview()
    image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/image2.jpg')
   
    cv2.circle(image,(ydl1,xdl1),2,(0,0,255),3)
    cv2.circle(image,(ydl1+10,xdl1),2,(0,0,255),3)
    cv2.circle(image,(ydl1-10,xdl1),2,(0,0,255),3)
    cv2.circle(image,(ydl1,xdl1+10),2,(0,0,255),3)
    cv2.circle(image,(ydl1,xdl1-10),2,(0,0,255),3)
        


    resize = ResizeWithAspectRatio(image, width=520) # Resize by width OR
    #resize = ResizeWithAspectRatio(image, height=250) # Resize by height 

    
    winname = "Position check rgb"
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, 150,60)  # Move it to (40,30)
    cv2.imshow(winname, resize)
    cv2.waitKey()
    camera.start_preview()
    
    

##Blank position move and check ##
    
def check2():
    global ydl2,xdl2
    camera.stop_preview()
    image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/blank.jpg')
   
    cv2.circle(image,(ydl2,xdl2),2,(0,0,255),3)
    cv2.circle(image,(ydl2+10,xdl2),2,(0,0,255),3)
    cv2.circle(image,(ydl2-10,xdl2),2,(0,0,255),3)
    cv2.circle(image,(ydl2,xdl2+10),2,(0,0,255),3)
    cv2.circle(image,(ydl2,xdl2-10),2,(0,0,255),3)
        


    resize = ResizeWithAspectRatio(image, width=520) # Resize by width OR
    #resize = ResizeWithAspectRatio(image, height=250) # Resize by height 

    
    winname = "Position check rgb"
    cv2.namedWindow(winname)        # Create a named window
    cv2.moveWindow(winname, 150,60)  # Move it to (40,30)
    cv2.imshow(winname, resize)
    cv2.waitKey()
    camera.start_preview()
    


    
    

    
    

def upb (x1):
    global ydl2,xdl2
    x1 = int(x1)
    xdl2 = xdl2+(-x1)
    print("X axis",xdl2,"Y axis",ydl2)
    
def downb(x1):
    global ydl2,xdl2
    x1 = int(x1)
    xdl2 = xdl2+x1
    print("X axis",xdl2,"Y axis",ydl2)
    
def leftb(x1):
    global ydl2,xdl2
    x1 = int(x1)
    ydl2 = ydl2+(-x1)
    print("X axis",xdl2,"Y axis",ydl2)

def rightb(x1):
    global ydl2,xdl2
    x1 = int(x1)
    ydl2 = ydl2+x1
    print("X axis",xdl2 ,"Y axis",ydl2)
    
#def showpreview():
    


def checkblank():
    
   
    my_w_child=Toplevel(root) # Child window 
    my_w_child.geometry("265x230")  # Size of the window 
    

    l1 = tk.Label(my_w_child,  text='Pixel', width=11 ) 
    l1.grid(row=1,column=1) 

    #e1 = tk.Entry(my_w_child, width=20,bg='white') 
    #e1.grid(row=1,column=2)
    
    e1 = Scale(my_w_child, from_=0,to=1000, orient=HORIZONTAL)
    e1.grid(row=1,column=2)
    
    b2 = tk.Button(my_w_child, text='↑',bg='white',width=3,height=2,command=lambda:[upb(e1.get()),check2()]).place(x=125,y=56)
    
    
    b3 = tk.Button(my_w_child, text='↓',bg='white',width=3,height=2,command=lambda:[downb(e1.get()),check2()]).place(x=125,y=104)
    
    
    b4 = tk.Button(my_w_child, text='←',bg='white',width=3,height=2,command=lambda:[leftb(e1.get()),check2()]).place(x=72,y=80)
    
    
    b5 = tk.Button(my_w_child, text='→',bg='white',width=3,height=2,command=lambda:[rightb(e1.get()),check2()]).place(x=179,y=80)
    
    
    b3 = tk.Button(my_w_child, text=' Close ',bg='#FF4957',height=2,command=my_w_child.destroy).place(x=180,y=170)
    
    
    b6 = tk.Button(my_w_child, text=' Position' ,bg='#E4EF3C',height=2,command=check2).place(x=10,y=170)
    
     
    b7 = tk.Button(my_w_child, text=' Submit ' ,bg='#31BF00',height=2,command=blank).place(x=95,y=170)
    
def intensity():
    global reds,greens,blues
    global redb,greenb,blueb
    global answer
    
    red = reds-redb
    green = greens-greenb
    blue = blues-blueb
    
    answer = math.sqrt(red**2 + green**2 +blue**2)
    
    answer = '%.2f'% answer
    
    print(answer)
    
    display_time7()


    
def measurement1():
    global xdl1,ydl1
    sumred = 0
    sumgreen = 0
    sumblue = 0
    global r1,g1,b1
    global r2,g2,b2
    global r3,g3,b3
    global r4,g4,b4
    global reds,greens,blues
    image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/image2.jpg')
    
    xdl=xdl1
    ydl=ydl1
    #cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
    #cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
    #cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)
    print("Top left")


    ##move dot up
    for i in range(10):
        
        b, g, r = image[xdl, ydl]
        ydl-=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot down   
    for i in range(10):
        
        b, g, r = image[xdl, ydl]
        ydl+=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot left
    for i in range(10):
        b, g, r = image[xdl, ydl]
        xdl-=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
    ##move dot right
    for i in range(10):
        b, g, r = image[xdl, ydl]
        xdl+=1
        sumred+=r
        sumgreen+=g
        sumblue+=b
        
        
    reds = meanred1=(sumred/40)
    greens = meangreen1=(sumgreen/40)
    blues = meanblue1=(sumblue/40)

    r1 = meanred1=(sumred/40)
    g1 = meangreen1=(sumgreen/40)
    b1 = meanblue1=(sumblue/40)

    print("Meanred",reds)
    print("Meangreen",greens)
    print("Meanblue",blues)


    

    sumred=0 
    sumgreen=0
    sumblue=0
 
    
    display_time()
    display_time2()
    display_time3()
    


# def measurement():
#     
#     sumred = 0
#     sumgreen = 0
#     sumblue = 0
#     global r1,g1,b1
#     global r2,g2,b2
#     global r3,g3,b3
#     global r4,g4,b4
#     image = cv2.imread('/home/pi/Desktop/backup/Cam/photo/img.jpg')
#     
#     xdl=460
#     ydl=770
#     #cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
#     #cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)
#     print("Top left")
# 
# 
#     ##move dot up
#     for i in range(10):
#         
#         b, g, r = image[xdl, ydl]
#         ydl-=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot down   
#     for i in range(10):
#         
#         b, g, r = image[xdl, ydl]
#         ydl+=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot left
#     for i in range(10):
#         b, g, r = image[xdl, ydl]
#         xdl-=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot right
#     for i in range(10):
#         b, g, r = image[xdl, ydl]
#         xdl+=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#         
#         
# 
#     r1 = meanred1=(sumred/40)
#     g1 = meangreen1=(sumgreen/40)
#     b1 = meanblue1=(sumblue/40)
# 
#     print("Meanred",meanred1)
#     print("Meangreen",meangreen1)
#     print("Meanblue",meanblue1)
# 
# 
#     red = meanred1 - 2           #Blank2_254nm = 7, 7, 7  Blank2_365nm = 130, 177, 255
#     green = meangreen1 - 2         #Blank1_254nm = 2, 2, 10 Blank1_365nm = 2, 2, 12
#     blue = meanblue1 - 12
# 
#     result = math.sqrt(red ** 2 + green ** 2 + blue ** 2)
#     print ("Sum top left",result)
# 
# 
#     sumred=0 
#     sumgreen=0
#     sumblue=0
# 
#     #############################################################################################top right
#     #### check 40 pixel length
#     
#     xdl=460
#     ydl=1200
# 
#     #cv2.circle(image,(ydl,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl+10,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl-10,xdl),2,(0,0,255),3)
#     #cv2.circle(image,(ydl,xdl+10),2,(0,0,255),3)
#     #cv2.circle(image,(ydl,xdl-10),2,(0,0,255),3)
# 
#     print("Top right")
# 
# 
#     ##move dot up
#     for i in range(10):
#         
#         b, g, r = image[xdl, ydl]
#         ydl-=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot down   
#     for i in range(10):
#         
#         b, g, r = image[xdl, ydl]
#         ydl+=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot left
#     for i in range(10):
#         b, g, r = image[xdl, ydl]
#         xdl-=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#     ##move dot right
#     for i in range(10):
#         b, g, r = image[xdl, ydl]
#         xdl+=1
#         sumred+=r
#         sumgreen+=g
#         sumblue+=b
#         
#         
#     r2 = meanred2=(sumred/40)
#     g2 = meangreen2=(sumgreen/40)
#     b2 = meanblue2=(sumblue/40)
# 
#     print("Meanred",meanred2)
#     print("Meangreen",meangreen2)
#     print("Meanblue",meanblue2)
# 
# 
#     red = meanred2 - 2           #Blank2_254nm = 7, 7, 7  Blank2_365nm = 130, 177, 255
#     green = meangreen2 - 2         #Blank1_254nm = 2, 2, 10 Blank1_365nm = 2, 2, 12
#     blue = meanblue2 - 12
# 
#     result = math.sqrt(red ** 2 + green ** 2 + blue ** 2)
#     print ("Sum top right",result)
# 
#     sumred=0 
#     sumgreen=0
#     sumblue=0    
#     
#     display_time()
#     display_time2()
#     display_time3()
#     display_time4()
#     display_time5()
#     display_time6()
#     display_time7()
#     display_time8()
#     display_time9()
#     display_time10()
#     display_time11()
#     display_time12()

def press(num):
    global fillNum
    fillNum = str(num)
    if fillNum == '4':
        number.set('Error')
    else:
        number.set(fillNum)
        
        
        
        
### Display show data ##

def display_time():
    global r1,g1,b1
    global reds
    clock_label['text'] = reds
    root.after(1000,display_time)
    
def display_time2():
    global r1,g1,b1
    global greens
    clock_label2['text'] = greens
    
    root.after(1000,display_time2)

def display_time3():
    global r1,g1,b1
    global blues
    clock_label3['text'] = blues
    root.after(1000,display_time3)
    
def display_time4():
    global r2,g2,b2
    global redb
    clock_label4['text'] = redb
    root.after(1000,display_time4)
    
def display_time5():
    global r2,g2,b2
    global greenb
    clock_label5['text'] = greenb
    root.after(1000,display_time5)

def display_time6():
    global r2,g2,b2
    global blueb
    clock_label6['text'] = blueb
    root.after(1000,display_time6)

def display_time7():
    global r3,g3,b3
    global answer
    clock_label7['text'] = answer
    root.after(1000,display_time7)
    
# def display_time8():
#     global r3,g3,b3
#     clock_label8['text'] = ''
#     root.after(1000,display_time8)
# 
# def display_time9():
#     global r3,g3,b3
#     clock_label9['text'] = ''
#     root.after(1000,display_time9)
#     
# def display_time10():
#     global r4,g4,b4
#     clock_label10['text'] = ''
#     root.after(1000,display_time10)
#     
# def display_time11():
#     global r4,g4,b4
#     clock_label11['text'] = ''
#     root.after(1000,display_time11)
# 
# def display_time12():
#     global r4,g4,b4
#     clock_label12['text'] = ''
#     root.after(1000,display_time12)


##Sample position move and check ##   

def up (x1):
    global ydl1,xdl1
    x1 = int(x1)
    xdl1 = xdl1+(-x1)
    print("X axis",xdl1,"Y axis",ydl1)
    
def down(x1):
    global ydl1,xdl1
    x1 = int(x1)
    xdl1 = xdl1+x1
    print("X axis",xdl1,"Y axis",ydl1)
    
def left(x1):
    global ydl1,xdl1
    x1 = int(x1)
    ydl1 = ydl1+(-x1)
    print("X axis",xdl1,"Y axis",ydl1)

def right(x1):
    global ydl1,xdl1
    x1 = int(x1)
    ydl1 = ydl1+x1
    print("X axis",xdl1 ,"Y axis",ydl1)
    
def clicker():
    
   
    my_w_child=Toplevel(root) # Child window 
    my_w_child.geometry("265x230")  # Size of the window 
    

    l1 = tk.Label(my_w_child,  text='Pixel', width=11 ) 
    l1.grid(row=1,column=1) 

    #e1 = tk.Entry(my_w_child, width=20,bg='white') 
    #e1.grid(row=1,column=2)
    
    e1 = Scale(my_w_child, from_=0,to=1000, orient=HORIZONTAL)
    e1.grid(row=1,column=2)
                                                                            
    b2 = tk.Button(my_w_child, text='↑',bg='white',width=3,height=2,command=lambda:[up(e1.get()),check1()]).place(x=125,y=56)
    
    
    b3 = tk.Button(my_w_child, text='↓',bg='white',width=3,height=2,command=lambda:[down(e1.get()),check1()]).place(x=125,y=104)
    
    
    b4 = tk.Button(my_w_child, text='←',bg='white',width=3,height=2,command=lambda:[left(e1.get()),check1()]).place(x=72,y=80)
    
    
    b5 = tk.Button(my_w_child, text='→',bg='white',width=3,height=2,command=lambda:[right(e1.get()),check1()]).place(x=179,y=80)
    
    
    b3 = tk.Button(my_w_child, text=' Close ',bg='#FF4957',height=2,command=my_w_child.destroy).place(x=180,y=170)
    
    
    b6 = tk.Button(my_w_child, text=' Position' ,bg='#E4EF3C',height=2,command=check1).place(x=10,y=170)
    
     
    b7 = tk.Button(my_w_child, text=' Submit ' ,bg='#31BF00',height=2,command=measurement1).place(x=95,y=170)
    
    

  


root= Tk()

root.wm_title("Color Image Measure by GPERD")
root.configure(bg='#FFFFCC')

root.geometry('800x500+1+0')



# add one button 



button1 = Button(root, text="Exit", fg="red",font=("Helvetica", 20), command=quit,bg='#7F93B5',borderwidth=5).place(x=-1,y=400)

button2 = Button(root, text=" Sample ", fg="black",font=("Helvetica", 12),bg='#CCFFCC', command=capture,borderwidth=3).place(x=10,y=100)


button4 = Button(root, text="Measure", fg="white",font=("Helvetica", 12), bg='green',command=intensity,borderwidth=3).place(x=10,y=180)







button6 = Button(root, text=" Position", fg="black",font=("Helvetica", 12), bg='#CCFFCC',command=lambda:[clicker(),streamoff()] ,borderwidth=3).place(x=120,y=100)

button7 = Button(root, text="   Clear   ", fg="white",font=("Helvetica", 12), bg='#606060',command=clear,borderwidth=3).place(x=10,y=220)

button10 = Button(root, text="   Blank  ",fg="white",font=("Helvetica", 12), bg='blue',command=capturebank,borderwidth=3).place(x=10,y=140)

button12 = Button(root, text=" Position",fg="white",font=("Helvetica", 12), bg='blue',command=lambda:[checkblank(),streamoff()],borderwidth=3).place(x=120,y=140)





button8 = Button(root, text=" Stream ON ", fg="black",font=("Helvetica", 12), bg='white',command=streamon,borderwidth=3).place(x=665,y=160)

button9 = Button(root, text="Stream OFF", fg="white",font=("Helvetica", 12), bg='black',command=streamoff,borderwidth=3).place(x=665,y=200)



label_1 = Label(root, text="R",bg='red',font=("Helvetica", 12)).place(x=230,y=340)
clock_label=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label.place(x=250,y=340)


label_2 = Label(root, text="G",bg='green',font=("Helvetica", 12)).place(x=230,y=380)
clock_label2=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label2.place(x=250,y=380)


label_3 = Label(root, text="B",bg='blue',font=("Helvetica", 12)).place(x=230,y=420)
clock_label3=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label3.place(x=250,y=420)

label_4 = Label(root, text="R",bg='red',font=("Helvetica", 12)).place(x=430,y=340)
clock_label4=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label4.place(x=450,y=340)


label_5 = Label(root, text="G",bg='green',font=("Helvetica", 12)).place(x=430,y=380)
clock_label5=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label5.place(x=450,y=380)


label_6 = Label(root, text="B",bg='blue',font=("Helvetica", 12)).place(x=430,y=420)
clock_label6=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label6.place(x=450,y=420)

label_7 = Label(root, text="",bg='#FFFFCC',font=("Helvetica", 12)).place(x=630,y=340)
clock_label7=Label(root,font=("Helvetica", 12),bg='#FFFFCC')
clock_label7.place(x=630,y=340)









label_3 = Label(root, text="Live Picture of Sample", font=("Helvetica", 16),bd=8,bg='#3BAED3') .place(x=330,y=20)


# label_4 = Label(root, text="Simple 1", bd=8,font=("Helvetica", 12),bg='#FFFFCC') .place(x=150,y=100)
# 
# label_4 = Label(root, text="Simple 3", bd=8,font=("Helvetica", 12),bg='#FFFFCC') .place(x=150,y=230)
# 
# label_4 = Label(root, text="Simple 2", bd=8,font=("Helvetica", 12),bg='#FFFFCC') .place(x=580,y=100)
# 
# label_4 = Label(root, text="Simple 4", bd=8,font=("Helvetica", 12),bg='#FFFFCC') .place(x=580,y=230)


label_5 = Label(root, text="Simple", bd=4,font=("Helvetica", 16),bg='#FAFF8F',borderwidth=5) .place(x=230,y=300)

label_5 = Label(root, text="Blank", bd=4,font=("Helvetica", 16),bg='#FAFF8F',borderwidth=5) .place(x=430,y=300)

label_5 = Label(root, text="Intensity", bd=4,font=("Helvetica", 16),bg='#FAFF8F',borderwidth=5) .place(x=630,y=300)




root.mainloop()


