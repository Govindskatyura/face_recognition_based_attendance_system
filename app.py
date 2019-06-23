import time
import sys
#sys.path.append('../')
import tkinter as tk
#from mine.copy import *
from face_D import *
import second as Feat
#from authpage import *
#main start
HEIGHT=600
WIDTH=450
global tk
global root
root =tk.Tk()
root.title("ipCam")
#canvas
global canvas
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
#image background
filename = tk.PhotoImage(file ='me.png')
image = canvas.create_image(0,-100,anchor='nw',image=filename)
canvas.grid(row=0, sticky='w'+'e'+'n'+'s')
canvas.pack(fill='both', expand=1)
canvas.bind("<Configure>", 'resize')

frame=tk.Frame(canvas,bg='#0f0f0f')
frame.place(rely=0.1,relx=0.1,relheight=0.8,relwidth=0.8)
def getframe():
    return frame
#signin(tk,root,canvas)
def call():
    frame.destroy()
    frame2=tk.Frame(canvas,bg='#0f0f0f')
    frame2.place(rely=0.1,relx=0.1,relheight=0.8,relwidth=0.8)
    fun(frame2)

def secscreen():
     frame.destroy()
     Feat.secondscreen(canvas,root)
#frame

#form section
text=tk.Label(frame,text='Welcome',font=40,bg='#fff')
text.place(rely=0.05,relx=0.1,relheight=0.1,relwidth=0.8)

textshow=tk.Label(frame,text='Enter the url or ip',font=40)
textshow.place(rely=0.25,relx=0.15,relheight=0.08,relwidth=0.7)

Address = tk.Entry(frame,bd =0.4)
Address.place(rely=0.38,relx=0.2,relheight=0.08,relwidth=0.6)

Submit = tk.Button(frame,text='SUBMIT',bd=0,bg='green',command=secscreen)#call)
Submit.place(rely=0.5,relx=0.2,relheight=0.08,relwidth=0.6)
Submit.flash()
#end

root.mainloop()