import tkinter

# Mile to Kilometer Converter

window = tkinter.Tk()
window.title("Kilometer to Mile Converter")
window.minsize(width=500, height=300)

# Entry
input = tkinter.Entry(width=20)
input.grid(column=1, row=0)
input.get()
# Label
my_label_mile = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
my_label_mile.grid(column=2, row=0)


my_label_equal = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
my_label_equal.grid(column=0, row=1)

my_label_result = tkinter.Label(text="0", font=("Arial", 14, "normal"))
my_label_result.grid(column=1, row=1)

my_label_kilo = tkinter.Label(text="Kilometer", font=("Arial", 14, "normal"))
my_label_kilo.grid(column=2, row=1)


# Button
def button_clicked():
   
    my_label_result.config(text=round(int(input.get()) * 1.6, 1))

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)












window.mainloop()
