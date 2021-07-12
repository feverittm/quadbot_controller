from tkinter import *
from tkinter import messagebox

def donothing():
    x = 0

def soft_buttons():
    sk_label = Label(master=sk_frame, text="Soft Keys")
    sk_label.pack()
    sk_button = []
    for skey in range(5):
        text_string = "Soft Key " + str(skey)
        print(text_string)
        sk_button.append(Button(master=sk_frame, text=text_string, \
                command=lambda c=skey: onButtonClicked(c)))
        sk_button[skey].pack()

def onButtonClicked(button_id):
    print("Button" + str(button_id) + " is clicked!");

def build_menubar():
    menubar = Menu(window, background="#ff8000", foreground='black', activebackground='white')
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

window = Tk()
window.title("Menu Test")
window.geometry("300x250")
build_menubar()

sk_frame = Frame()
soft_buttons()
sk_frame.pack()

window.mainloop()
