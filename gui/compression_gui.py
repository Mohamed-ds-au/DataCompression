import tkinter as tk


class myApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Compressor")

        #--------BackGround------#
        self.config(bg="#000814")
        #--------Geometry--------#
        self.geometry("1260x720")

        #---------Side bar--------#
        # self.sidebar_shadow = tk.Frame(self, bg="#f1faee", height=1260, width=243)
        # self.sidebar_shadow.place(x=0)
        self.sidebar = tk.Frame(self, bg="#001d3d",height=1260, width=240, container=False)
        self.sidebar.place(x=0)
        self.sidebar.pack_propagate(False)
        self.homebutton = tk.Button(
            self.sidebar,
            bg="#003566",
            text="Home",
            font=("Arial",),
            fg="white",
            activebackground="#0077b6",
            activeforeground="white",
            highlightthickness=0,
            width=20)
        self.homebutton.place(x= 18,y=126)

        self.algobutton = tk.Button(
            self.sidebar,
            bg="#003566",
            text="Algorithms",
            font=("Arial",),
            fg="white",
            activebackground="#0077b6",
            activeforeground="white",
            highlightthickness=0,
            width=20)
        self.algobutton.place(x= 18,y=176)

        self.aboutbutton = tk.Button(
            self.sidebar,
            bg="#003566",
            text="About",
            font=("Arial",),
            fg="white",
            activebackground="#0077b6",
            activeforeground="white",
            highlightthickness=0,
            width=20)
        self.aboutbutton.place(x= 18,y=226)
        

app = myApp()

app.mainloop()