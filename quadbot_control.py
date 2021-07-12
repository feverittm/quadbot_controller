from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

def donothing():
    x = 0

def leg_buttons():
    lb_label = Label(master=legs_frame, text="Select Leg to Control:")
    lb_label.pack(side=TOP)
    lb_button = []
    for leg in range(4):
        lb_button.append(Radiobutton(master=legs_frame, text=str(leg), \
                value=str(leg), variable=selected_leg))
        lb_button[leg].pack(side=LEFT, padx=15, fill=X)

def build_sliders():
    # need 3 slider to control the position of each of the leg joints
    sl_dict = {0 : "coxa", 1 : "femur", 2: "tibia"}
    slider = []
    for item in range(3):
        slider.append(Scale(master=slider_frame, from_=0, to=100, variable=sl_dict[item]))
        slider[item].pack(side=LEFT, padx = 10)

def build_controls():
    controls_list = {
            "reset":"cmd_reset",
            "stand":"cmd_stand",
            "forward":"cmd_fwd",
            "back":"cmd_back"
            }
    ctl_label = Label(master=controls_frame, text="Controls", font=fontStyle)
    ctl_label.pack()
    ctl_button = []
    for ckey in controls_list.keys():
        ctl_button.append(Button(master=controls_frame, text=ckey, font=fontStyle))
        ctl_button[-1].pack(side=LEFT, fill=X)

def soft_buttons():
    sk_button = []
    for skey in range(5):
        text_string = "Soft Key " + str(skey)
        sk_button.append(Button(master=sk_frame, text=text_string, \
                command=lambda c=skey: onButtonClicked(c)))
        sk_button[skey].pack()

def onButtonClicked(button_id):
    print("Button" + str(button_id) + " is clicked!");

def build_menubar():
    menubar = Menu(window, background="#ff8000", foreground='black'
            , activebackground='white')
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)

# ------ main ------

selected_leg=0

# top level window stuff...
window = Tk()
window.title("Quadbot Controls")
window.geometry("350x350")
build_menubar()

fontStyle = tkFont.Font(family="Lucida Grande", size=18)

selected_leg = StringVar(window, "0")

# UI has two vertical frame and two horizontal frame
# top / bottom frame
#         bottom has just the list of control buttons across the window
# top frame is split horizontal to hold the softkeys on the right
#    and another frame on the left
#       left frame is split in two vertically to hold the leg selection on top
#       and the sliders below.  
#
#The size of the slider should drive the size of the main window.
#
# -- top frame has 3 sections...
top_frame = Frame()

legs_frame = Frame(master=top_frame)
leg_buttons()
legs_frame.pack(side=TOP, fill=X)

slider_frame = Frame(master=top_frame)
build_sliders()
slider_frame.pack(side=LEFT, fill=X)

sk_frame = Frame(master=top_frame)
soft_buttons()
sk_frame.pack(side=RIGHT, fill=Y)

top_frame.pack(side=TOP, fill=X)

# -- bottom frame for the controls
bot_frame = Frame()

controls_frame = Frame(master=bot_frame)
build_controls()
controls_frame.pack(side=BOTTOM, expand = True, fill=X)

bot_frame.pack(side=BOTTOM, fill=X)

# -- start the main UI loop...

window.mainloop()
