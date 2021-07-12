from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

def donothing():
    x = 0

def build_sliders():
    sl_label = Label(master=slider_frame, text="Sliders", font=fontStyle)
    sl_label.pack()

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
    sk_label = Label(master=sk_frame, text="Soft Keys", font=fontStyle)
    sk_label.pack()
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

window = Tk()
window.title("Quadbot Controls")
window.geometry("300x250")
build_menubar()

fontStyle = tkFont.Font(family="Lucida Grande", size=18)

top_frame = Frame()

sk_frame = Frame(master=top_frame)
soft_buttons()
sk_frame.pack(side=RIGHT, fill=Y)

slider_frame = Frame(master=top_frame)
build_sliders()
slider_frame.pack(side=LEFT, fill=X)

top_frame.pack(side=TOP, fill=X)

bot_frame = Frame()

controls_frame = Frame(master=bot_frame)
build_controls()
controls_frame.pack(side=BOTTOM, expand = True, fill=X)

bot_frame.pack(side=BOTTOM, fill=X)

window.mainloop()
