import time
import sys
from secondscree import *
HEIGHT=600
WIDTH=450
global root
def secscreen():
    Start.__des__()
    SecPage=secondscreen(canvas,root,Start)
    SecPage.start()
    #Start.start()

####  Main Gui  ###
class home:
    
    def __init__(self,root,canvas):
        self.root=root

    def start(self):
        self.frame=tk.Frame(canvas,bg='#0f0f0f')
        self.frame.place(rely=0.1,relx=0.1,relheight=0.8,relwidth=0.8)
        self.text=tk.Label(self.frame,text='Welcome',font=40,bg='#fff')
        self.text.place(rely=0.05,relx=0.1,relheight=0.1,relwidth=0.8)

        self.textshow=tk.Label(self.frame,text='Enter the url or ip',font=40)
        self.textshow.place(rely=0.25,relx=0.15,relheight=0.08,relwidth=0.7)
        self.Address = tk.Entry(self.frame,bd =0.4)
        self.Address.place(rely=0.38,relx=0.2,relheight=0.08,relwidth=0.6)


        self.Submit = tk.Button(self.frame,text='SUBMIT',bd=0,bg='green',command=secscreen)#call)
        self.Submit.place(rely=0.5,relx=0.2,relheight=0.08,relwidth=0.6)
        self.Submit.flash()
    def __des__(self):
        self.frame.destroy()
        self.text.destroy()
        self.textshow.destroy()
        self.Address.destroy()
        self.Submit.destroy()


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
Start=home(root,canvas)
Start.start()



root.mainloop()
