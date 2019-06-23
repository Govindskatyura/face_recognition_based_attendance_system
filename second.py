import tkinter as tk
import face_D as FaceAdd
import faceDETECTOR as Video
import faceR as Trainer
import scroll as sc
import sys


class popupWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        self.l=tk.Label(top,text="Fill details")
        self.l.pack()
        
        self.l=tk.Label(top,text="UserName")
        self.l.pack()
        self.e=tk.Entry(top)
        self.e.pack()
        
        self.l=tk.Label(top,text="Batch")
        self.l.pack()
        self.e2=tk.Entry(top)
        self.e2.pack()
        
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=(self.e.get(),self.e2.get())
        self.top.destroy()


def live():
    Video.liveVideo() 
def Add(name,batch):
    FaceAdd.capture(name,batch)

def secondscreen(canvas,root):
    def pop():
        Training(root)
    def attaendance():
        frame.destroy
        sc.scroll(root,canvas)
    def Training():
        Trainer.TrainData()
    def popup():
        w=popupWindow(root)
        SecondButton["state"] = "disabled" 
        root.wait_window(w.top)
        SecondButton["state"] = "normal" 
        datalist=entryValue(w)
        print(datalist[0],datalist[1])
        Add(datalist[0],datalist[1])
    def entryValue(w):
        return w.value

    frame=tk.Frame(canvas,bg='#0f0f0f')
    frame.place(rely=0.1,relx=0.1,relheight=0.8,relwidth=0.8)
    
    FirstButton=tk.Button(frame,text='Start Live',font=40,bg='green',command=live)
    FirstButton.place(rely=0.05,relx=0.05,relheight=0.1,relwidth=0.9)
    
    SecondButton=tk.Button(frame,text='Add Face',font=40,bg='#aa0',command=popup)
    SecondButton.place(rely=0.25,relx=0.05,relheight=0.1,relwidth=0.9)
    
    ThirdButton=tk.Button(frame,text='Train',font=40,bg='#aa0',command=Training)
    ThirdButton.place(rely=0.40,relx=0.05,relheight=0.1,relwidth=0.9)
    
    FourthButton=tk.Button(frame,text='attaendance',font=40,bg='#aa0',command=attaendance)
    FourthButton.place(rely=0.55,relx=0.05,relheight=0.1,relwidth=0.9)
    '''
    FifthButton=tk.Button(frame,text='about',font=40,bg='#aa0')
    FifthButton.place(rely=0.70,relx=0.05,relheight=0.1,relwidth=0.9)
    '''
    sixthButton=tk.Button(frame,text='exit',font=40,bg='red',command=root.destroy)
    sixthButton.place(rely=0.70,relx=0.05,relheight=0.1,relwidth=0.9)