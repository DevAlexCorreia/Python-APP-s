# Complete Project

from lib2to3.pgen2.token import RIGHTSHIFT
from msilib.schema import TextStyle
from tkinter import *
from tkinter import ttk

color1="#878383" # mid gray - Something between white and black
color2="#000000" # Piano Black
color3="#495ec9" # mid Blue
color4="#d1deeb" # Bluer white
color5="#e0850d" #Common Orange
color6="#807c78" #Dark gray

#Step1 - Setting the window's screen
window = Tk()#Creating a window to the app
window.title("Calculator")#naming

window.geometry("350x480")#putting some measurements
window.config(bg=color1)
#Screen
frame_screen = Frame(window, width=350, height=70,bg=color6)
frame_screen.grid(row=0, column=0)
#Body background
frame_body = Frame(window, width=350, height=410,bg=color4)
frame_body.grid(row=1, column=0)
#_____________LOGIC______________
#ALL Values
all_values = ''

text_value=StringVar()#Instanciate the variable

#ALL Values Function
def Enter_value(event):
    global all_values
    all_values = all_values + str(event)
    
    text_value.set(all_values)
# FUNCTION TO CALCULATE

def calculate():
    global all_values
    result = eval(all_values)
    text_value.set(str(result))
    all_values=""
# SCREEN CLEANER

def clean():
    global all_values
    all_values=""
    text_value.set("")

        

#Creating Labels
app_label = Label(frame_screen, textvariable=text_value, width=20, height=2,padx=2, relief=FLAT,anchor="e",font=("ivy 20 bold"),justify=RIGHT,bg=color2,fg=color4)
app_label.place(x=4,y=2)

#TOP Buttons
b1 = Button(frame_body,command= clean, text="C", width=15, height=3,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b1.place(x=10,y=10)#Localization 
b2 = Button(frame_body,command= lambda: Enter_value('%'),text="%", width=7, height=3,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b2.place(x=180,y=10)
b3 = Button(frame_body,command= lambda: Enter_value('/'), text="÷", width=7, height=3,bg=color3,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b3.place(x=265,y=10) 


#ALPHA NUMERIC KEYBOARD
b4 = Button(frame_body,command= lambda: Enter_value('1'), text="1", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b4.place(x=10,y=90)#Localization 
b5 = Button(frame_body,command= lambda: Enter_value('2'), text="2", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b5.place(x=95,y=90)
b6 = Button(frame_body,command= lambda: Enter_value('3'), text="3", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b6.place(x=180,y=90)
b7 = Button(frame_body,command= lambda: Enter_value('*'), text="x", width=7, height=3,bg=color3,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b7.place(x=265,y=90)
b8 = Button(frame_body,command= lambda: Enter_value('4'), text="4", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b8.place(x=10,y=170)#Localization 
b9 = Button(frame_body, command= lambda: Enter_value('5'),text="5", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b9.place(x=95,y=170)
b10 = Button(frame_body,command= lambda: Enter_value('6'), text="6", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b10.place(x=180,y=170)
b11 = Button(frame_body,command= lambda: Enter_value('-'), text="-", width=7, height=3,bg=color3,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b11.place(x=265,y=170)
b12 = Button(frame_body,command= lambda: Enter_value('7'), text="7", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b12.place(x=10,y=250)#Localization 
b13 = Button(frame_body,command= lambda: Enter_value('8'), text="8", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b13.place(x=95,y=250)
b14 = Button(frame_body,command= lambda: Enter_value('9'), text="9", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b14.place(x=180,y=250)
b15 = Button(frame_body,command= lambda: Enter_value('+'), text="+", width=7, height=3,bg=color3,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b15.place(x=265,y=250)
b12 = Button(frame_body,command= lambda: Enter_value('+/-'), text="+/-", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b12.place(x=10,y=330)#Localization 
b13 = Button(frame_body,command= lambda: Enter_value('0'), text="0", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b13.place(x=95,y=330)
b14 = Button(frame_body,command= lambda: Enter_value(','), text=",", width=7, height=3,bg=color2,foreground=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b14.place(x=180,y=330)
b15 = Button(frame_body,command= calculate, text="=",width=7, height=3,bg=color5,fg=color4,font=('ivy 13 bold'),relief=RAISED,overrelief=RIDGE)
b15.place(x=265,y=330)











window.mainloop()
