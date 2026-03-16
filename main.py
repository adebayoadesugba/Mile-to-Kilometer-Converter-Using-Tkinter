import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)



button2 = tkinter.Button(text="Click Me Next")
button2.grid(column=2, row=0)




# Button
def button_clicked():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=20)
input.grid(column=3, row=2)
input.get()

# Text = tkinter.Text(height=5, width=30)
# Text.pack()








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