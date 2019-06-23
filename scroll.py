import tkinter as tk
import dbcon as con
import second as sc
def scroll(root,canvas):
    canvas2=canvas
    canvas.destroy()
    canvas = tk.Canvas(root,height=600,width=450)
    scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tk.Frame(canvas)
    def Back():
        frame.destroy()
        sc.secondscreen(canvas,root)
    # group of widgets
    att_List=con.showall()
    tk.Label(frame, text='Attandence',fg="white",bg="black",font=("Helvetica", 40)).pack() 
    tk.Label(frame).pack()
    for i in range(0,len(att_List)):
        #a=att_List[i][1]
        tk.Label(frame, text='name : {} , Batch :{},Time :{}'.format(att_List[i][1],att_List[i][2],att_List[i][3]),fg="white",bg="black",font=40).pack(fill="both")
        tk.Label(frame).pack()

    tk.Button(frame, text="Back",fg="white",bg="black",font=40,command=Back).pack(fill="both") 

    # put the frame in the canvas

    canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), 
                    yscrollcommand=scroll_y.set)
                    
    canvas.pack(fill='both', expand=True, side='left')
    scroll_y.pack(fill='y', side='right')
