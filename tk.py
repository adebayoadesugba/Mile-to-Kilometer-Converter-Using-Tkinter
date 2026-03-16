import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()







# Button
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=20)
input.pack()
input.get()

Text = tkinter.Text(height=5, width=30)
Text.focus()
Text.insert(tkinter.END, "Example of multi-line text entry.")
Text.pack()


#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = tkinter.Button(text="Click Me", command=action)
button.pack()

#Entries
entry = tkinter.Entry(width=30)
#Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = tkinter.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()






window.mainloop()

def add(*args):
    sum = 0
    for n in args:
        sum += n
        
    print(f"Sum: {sum}")

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    print(n)

calculate(2, add=3, multiply=5, divide=2)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.color = kwargs.get("color")

my_car = Car(make="Toyota")
print(my_car.make)