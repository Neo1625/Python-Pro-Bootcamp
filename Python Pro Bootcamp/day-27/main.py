from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
input.grid(column=3, row=3)

#New button
button_2 = Button(text="Click")
button_2.grid(column=2, row=0)



window.mainloop()
