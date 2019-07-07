'''import tkinter as tk
import second as sc
'''
import dbcon as con

import tkinter as tk

class scroll:
    def __init__(self,root,canvas):
        self.root=root
        self.canvas=canvas
    def start(self,parent):    
        self.scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)

        self.frame =tk.Frame(self.canvas)
        #self.frame.place(rely=0.1,relx=0.1,relwidth=0.8)
        def Back():
            self.frame.destroy()
            self.scroll_y.destroy()
            parent.start()
            #self.canvas.destroy()
            #sc.secondscreen(canvas,root)
        # group of widgets
        att_List=con.showall()
        #att_List=[[1,"somethhing","enything","enything"],[2,"somethhing","enything","enything"],[3,"somethhing","enything","enything"],[4,"somethhing","enything","enything"]]
        tk.Label(self.frame, text='Attandence',fg="white",bg="black",font=("Helvetica", 40)).pack(fill="both",pady=0) 
        tk.Button(self.frame, text="Back",fg="white",bg="green",font=40,command=Back).pack(fill="both")
        tk.Label(self.frame).pack()
        for i in range(0,len(att_List)):
            #a=att_List[i][1]
            tk.Label(self.frame, text='name : {} , Batch :{},Time :{}'.format(att_List[i][1],att_List[i][2],att_List[i][3]),fg="white",bg="black",font=40).pack(fill="both")
            tk.Label(self.frame).pack()
 

        # put the frame in the canvas

        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        # make sure everything is displayed before configuring the scrollregion
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),yscrollcommand=self.scroll_y.set)
                        
        self.canvas.pack(fill='both', expand=True, side='left')
        self.scroll_y.pack(fill='y', side='right')