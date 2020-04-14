from tkinter import *
from PIL import ImageTk 
from PIL import Image as Img
import time
import os
import threading





root = Tk()


#Show the original image on left hand side  
originalImage = ImageTk.PhotoImage(
                Img.open('/home/escanor/Documents/DSP/Facial-Recognition/database/1.jpeg'))
originalSection = Label(root , image=originalImage ,  width=600 , height=600)
originalSection.grid(row=0,column=0)


#Get all the images from 'database'
relDatabasePath = 'database'

currentDir = os.getcwd()
images = os.listdir(os.path.join(currentDir,relDatabasePath))
dbImages = [os.path.join(currentDir ,relDatabasePath, image) for image in images]

#Show the comparable image on right hand side
# comparingImage = ImageTk.PhotoImage(
#                 Img.open('/home/escanor/Documents/DSP/Facial-Recognition/database/1.jpeg'))
comparingSection = Label(root, width=600 , height=600)
comparingSection.grid(row=0,column=1)


def changeImage():
    for i in dbImages:
        time.sleep(0.1)
        changedImage = ImageTk.PhotoImage(
                    Img.open(i))
        print(i)
        comparingSection.configure(image=changedImage)
   

thread = threading.Thread(target=changeImage)
thread.start()



def on_closing():
    root.destroy()
    thread._stop()
    

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()