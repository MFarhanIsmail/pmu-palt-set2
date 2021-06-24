#palt python set 2
#question4
#Mohamad farhan bin ismail (20ddt19f1085)
from tkinter import *
change = True

def change_text():
    global change
    if change:
        lbl_text["text"] = "I have been changed"
        change = False
    else:
        lbl_text["text"] = "Change Text"
        change = True 
         

window = Tk()
#title
window.title("Palt-Question4") 
#size
window.geometry("300x150")
#padding
window.config(padx=90,pady=100)

#lable and button gui 
lbl_text = Label(text="Changed Text")
btnChgText = Button(text="Change Text",command=change_text)
#position
lbl_text.grid(row=5,column=1)
btnChgText.grid(row=4,column=1)

window.mainloop()