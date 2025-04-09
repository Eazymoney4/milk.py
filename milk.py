# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#deefff")

# Add widgets
# Add Label
l1 = Label(frame, text="Full Name", bg="#3850D3", fg='white', width=12)
l2 = Label(frame, text="Email Id", bg="#3850D3", fg='white', width=12)
l3 = Label(frame, text="Enter Password", bg="#3850D3", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function to display message
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations for your new account"
    textbox.insert(END, greet)
    textbox.insert(END, message)

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text="Create Account", command=display, bg='red')

# Arrange all widgets
frame.place(x=20, y=20)
l1.place(x=20, y=20)
name_entry.place(x=150, y=20)
l2.place(x=20, y=80)
email_entry.place(x=150, y=80)
l3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(x=20, y=250)

root.mainloop()