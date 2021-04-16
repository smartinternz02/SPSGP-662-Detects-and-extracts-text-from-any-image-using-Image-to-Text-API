from tkinter import *
from PIL import Image,ImageTk
import os
import cv2
from tkinter import filedialog
from text_recognition import load

def open_image():
    x=openfilename()
    result=load(x)
def openfilename(): 
    filename = filedialog.askopenfilename(title ='open') 
    return filename 

window=Tk()
window.title("load image")
window.config(bg='skyblue')
window.geometry('300x300')
l1=Label(window,text="Please upload the photo by clicking the below button").pack()
l2=Label(window,text='the uploaded photo will be detected').pack(padx=20,pady=20)
b1=Button(window,text="open image",command=open_image)
b1.pack(padx=20,pady=20)
window.mainloop()
