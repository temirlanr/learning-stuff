from tkinter import *

root = Tk()

#####
# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My name is TemirlaN!!!")
# myLabel3 = Label(root, text="       ")

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=2, column=2)
#####

#####
# def Click():
#     clickLabel = Label(root, text="ClickED!!")
#     clickLabel.pack()

# def entryClick():
#     entryLabel = Label(root, text="Hi "+entry.get())
#     entryLabel.pack()

# entryLabel = Label(root, text="Enter your name: ").pack()

# entry = Entry(root, width=100, borderwidth=3)
# entry.pack()
# # entry.insert(0, "Enter your name...")

# myButton = Button(root, text="Click", padx=50, command=entryClick, fg="white", bg="grey")
# myButton.pack()
#####

root.title("CalculatOR!!!!")

entry = Entry(root, width=40, borderwidth=3)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))

def clearButton():
    entry.delete(0, END)

def addButton():
    first_number = entry.get()
    global first
    first = int(first_number)
    entry.delete(0, END)

def equalButton():
    second_number = entry.get()
    entry.delete(0, END)
    entry.insert(0, first + int(second_number))



button_0 = Button(root, width=9, text=str(0), pady=10, command=lambda: button_click(0))
button_1 = Button(root, width=9, text=str(1), pady=10, command=lambda: button_click(1))
button_2 = Button(root, width=9, text=str(2), pady=10, command=lambda: button_click(2))
button_3 = Button(root, width=9, text=str(3), pady=10, command=lambda: button_click(3))
button_4 = Button(root, width=9, text=str(4), pady=10, command=lambda: button_click(4))
button_5 = Button(root, width=9, text=str(5), pady=10, command=lambda: button_click(5))
button_6 = Button(root, width=9, text=str(6), pady=10, command=lambda: button_click(6))
button_7 = Button(root, width=9, text=str(7), pady=10, command=lambda: button_click(7))
button_8 = Button(root, width=9, text=str(8), pady=10, command=lambda: button_click(8))
button_9 = Button(root, width=9, text=str(9), pady=10, command=lambda: button_click(9))
button_clear = Button(root, width=9, text="clear", pady=10, command=clearButton).grid(row=1, column=3)
button_add = Button(root, width=9, text="+", pady=10, command=addButton).grid(row=2, column=3)
button_equal = Button(root, width=9, text="=", pady=10, command=equalButton).grid(row=3, column=3)



# don't judge me...
for i in range(10):
    
    if(i==0):
        globals()["button_"+str(i)].grid(row=4, column=1)
    elif(i==1):
        globals()["button_"+str(i)].grid(row=3, column=0)
    elif(i==2):
        globals()["button_"+str(i)].grid(row=3, column=1)
    elif(i==3):
        globals()["button_"+str(i)].grid(row=3, column=2)
    elif(i==4):
        globals()["button_"+str(i)].grid(row=2, column=0)
    elif(i==5):
        globals()["button_"+str(i)].grid(row=2, column=1)
    elif(i==6):
        globals()["button_"+str(i)].grid(row=2, column=2)
    elif(i==7):
        globals()["button_"+str(i)].grid(row=1, column=0)
    elif(i==8):
        globals()["button_"+str(i)].grid(row=1, column=1)
    elif(i==9):
        globals()["button_"+str(i)].grid(row=1, column=2)




root.mainloop()