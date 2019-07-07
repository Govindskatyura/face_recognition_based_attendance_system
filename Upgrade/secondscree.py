'''
import scroll as sc
'''
import sys
import Face_Capture as FaceAdd
import FaceDETECTOR as Video
import Face_Trainer as Trainer
from attendancepage import *
global tk
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

#Start Video Camera and quit with Q
def live():
    Video.liveVideo() 

def Add(name,batch):
    FaceAdd.capture(name,batch)

class secondscreen:
    def pop(self):
        Training(self.root)
    def attaendance(self):
        self.frame.destroy()
        Attpage=scroll(self.root,self.canvas)
        Attpage.start(self)
    def Training(self):
        Trainer.TrainData()
    def back(self):
        self.frame.destroy()
        self.Start.start()
    def entryValue(self,w):
        return w.value
    def popup(self):
        w=popupWindow(self.root)
        self.SecondButton["state"] = "disabled" 
        self.root.wait_window(w.top)
        self.SecondButton["state"] = "normal" 
        self.datalist=self.entryValue(w)
        print(self.datalist[0],self.datalist[1])
        Add(self.datalist[0],self.datalist[1])
    
    
    def __init__(self,canvas,root,Start):
        self.root=root
        self.canvas=canvas
        self.Start=Start
    def start(self):
        self.frame=tk.Frame(self.canvas,bg='#0f0f0f')
        self.frame.place(rely=0.1,relx=0.1,relheight=0.8,relwidth=0.8)
        
        self.FirstButton=tk.Button(self.frame,text='Start Live',font=40,bg='green',command=live)
        self.FirstButton.place(rely=0.05,relx=0.05,relheight=0.1,relwidth=0.9)
        
        self.SecondButton=tk.Button(self.frame,text='Add Face',font=40,bg='#aa0',command=self.popup)
        self.SecondButton.place(rely=0.25,relx=0.05,relheight=0.1,relwidth=0.9)
        
        self.ThirdButton=tk.Button(self.frame,text='Train',font=40,bg='#aa0',command=self.Training)
        self.ThirdButton.place(rely=0.40,relx=0.05,relheight=0.1,relwidth=0.9)
        
        self.FourthButton=tk.Button(self.frame,text='attaendance',font=40,bg='#aa0',command=self.attaendance)
        self.FourthButton.place(rely=0.55,relx=0.05,relheight=0.1,relwidth=0.9)
        
        self.FifthButton=tk.Button(self.frame,text='Back',font=40,bg='#0f9',command=self.back)
        self.FifthButton.place(rely=0.70,relx=0.05,relheight=0.1,relwidth=0.9)
        
        self.sixthButton=tk.Button(self.frame,text='exit',font=40,bg='red',command=self.root.destroy)
        self.sixthButton.place(rely=0.85,relx=0.05,relheight=0.1,relwidth=0.9)