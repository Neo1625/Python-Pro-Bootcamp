from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def miles_to_km():
    print("I got clicked")
    miles_str = input.get()
    miles_int = int(miles_str) * 1.6
    miles = str(miles_int)
    default_value.config(text=miles)

#miles_input
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

#Miles_label
miles_label = Label(text="Miles")
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

#is_equal_to_label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.config(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

#0_label
default_value = Label(text="0")
default_value.config(text="0")
default_value.grid(column=1, row=1)

#km_label
km_label = Label(text="Km")
km_label.config(text="Km")
km_label.grid(column=2, row=1)

#Button_label
button_label = Button(text="Calculate", command=miles_to_km)
button_label.grid(column=1, row=2)








window.mainloop()



