from tkinter import *
import globals
import matplotlib
import matplotlib.animation as animation
from matplotlib import style
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        #self.init_window()
    #Creation of init_window
    def init_coefbtn(self):
        # changing the title of our master widget
        self.master.title("GUI")
        self.pack(fill=BOTH)

        self.create_kp()
        self.create_kd()
        self.create_ki()
    """
    def init_graph(self, fig):
        self.pack(fill=BOTH)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

        #ani = animation.FuncAnimation(f, animate, interval=1000)
    """
    def init_velentry(self):
        self.pack(fill=BOTH)
        self.create_entry()

    def init_stateentry(self):
        self.pack(fill=BOTH)
        self.create_state()
    def create_entry(self, var=0, lbl_target_velocity=0):
        self.var = var
        self.var = IntVar()
        self.lbl_target_velocity = lbl_target_velocity
        # creating user input frame
        target_velEntry = Frame(self)
        ent_velocity = Entry(master=target_velEntry, width=10, textvariable=self.var)
        #globals.target_velocity = int(self.var.get())
        lbl_entry = Label(master=target_velEntry, text="rpm")
        updateButton = Button(self, text=u"\u2191", command=self.client_update)

        ent_velocity.grid(row=0, column=0, sticky="e")
        lbl_entry.grid(row=0, column=1, sticky="w")
        target_velEntry.grid(row=0, column=0, padx=10)
        updateButton.grid(row=0, column=1, pady=10)
        #create feedback label
        self.lbl_target_velocity = Label(master=self, text="rpm")
        self.lbl_target_velocity.grid(row=0, column=2, padx=10)
    def create_state(self):
        btn_backwards = Button(master=self, text=u"\u2190", command=self.backwards)
        btn_stop = Button(master=self, text="stop", command=self.stop)
        btn_forwards = Button(master=self, text=u"\u2192", command=self.forwards)

        btn_backwards.grid(row=0, column=0, sticky="nsew")
        btn_stop.grid(row=0, column=1, sticky="nsew")
        btn_forwards.grid(row=0, column=2, sticky="nsew")
    def backwards(self):
        globals.state = 1
        globals.state_event = True

    def forwards(self):
        globals.state = 2
        globals.state_event = True

    def stop(self):
        globals.state = 0
        globals.state_event = True

    def create_kp(self,lbl_value_kp=None):
        self.lbl_value_kp = lbl_value_kp
        # creating coefficient decreas and increase buttons
        btn_decrease = Button(master=self, text="-", command=self.decrease_kp)
        btn_increase = Button(master=self, text="+", command=self.increase_kp)
        self.lbl_value_kp = Label(master=self, text="{:d}".format(globals.kp))
        lbl_coef = Label(master=self, text="Kp")

        lbl_coef.grid(row=0, column=0)
        btn_decrease.grid(row=0, column=1, sticky="nsew")
        self.lbl_value_kp.grid(row=0, column=2)
        btn_increase.grid(row=0, column=3, sticky="nsew")

    def create_kd(self,lbl_value_kd=None):
        self.lbl_value_kd = lbl_value_kd
        # creating coefficient decreas and increase buttons
        btn_decrease = Button(master=self, text="-", command=self.decrease_kd)
        btn_increase = Button(master=self, text="+", command=self.increase_kd)
        self.lbl_value_kd = Label(master=self, text="{:d}".format(globals.kd))
        lbl_coef = Label(master=self, text="Kd")

        lbl_coef.grid(row=1, column=0)
        btn_decrease.grid(row=1, column=1, sticky="nsew")
        self.lbl_value_kd.grid(row=1, column=2)
        btn_increase.grid(row=1, column=3, sticky="nsew")

    def create_ki(self,lbl_value_ki=None):
        self.lbl_value_ki = lbl_value_ki
        # creating coefficient decreas and increase buttons
        btn_decrease = Button(master=self, text="-", command=self.decrease_ki)
        btn_increase = Button(master=self, text="+", command=self.increase_ki)
        self.lbl_value_ki = Label(master=self, text="{:d}".format(globals.ki))
        lbl_coef = Label(master=self, text="Ki")

        lbl_coef.grid(row=2, column=0)
        btn_decrease.grid(row=2, column=1, sticky="nsew")
        self.lbl_value_ki.grid(row=2, column=2)
        btn_increase.grid(row=2, column=3, sticky="nsew")

    def client_update(self):
        globals.target_velocity = int(self.var.get())
        self.lbl_target_velocity["text"] = "{:d} rpm".format(globals.target_velocity)
        globals.vel_event = True

    def increase_kp(self, value = 0):
        self.value = value
        self.value = int(self.lbl_value_kp["text"])
        self.lbl_value_kp["text"] = "{:d}".format(self.value+1)
        globals.kp+=1
        globals.kp_event = True

    def increase_kd(self, value = 0):
        self.value = value
        self.value = int(self.lbl_value_kd["text"])
        self.lbl_value_kd["text"] = "{:d}".format(self.value+1)
        globals.kd+=1
        globals.kd_event = True

    def increase_ki(self, value = 0):
        self.value = value
        self.value = int(self.lbl_value_ki["text"])
        self.lbl_value_ki["text"] = "{:d}".format(self.value+1)
        globals.ki+=1
        globals.ki_event = True

    def decrease_kp(self,value = 0):
        self.value = value
        self.value = int(self.lbl_value_kp["text"])
        self.lbl_value_kp["text"] = "{:d}".format(self.value-1)
        globals.kp+=-1
        globals.kp_event= True

    def decrease_kd(self,value = 0):
        self.value = value
        self.value = int(self.lbl_value_kd["text"])
        self.lbl_value_kd["text"] = "{:d}".format(self.value-1)
        globals.kd+=-1
        globals.kd_event = True

    def decrease_ki(self, value=0):
        self.value = value
        self.value = int(self.lbl_value_ki["text"])
        self.lbl_value_ki["text"] = "{:d}".format(self.value - 1)
        globals.ki += -1
        globals.ki_event = True