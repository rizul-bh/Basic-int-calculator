from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x350")

calc_heading = Label(root, text="INT CALCULATOR", bg="black", fg="red", font=("Arial", 18))
calc_heading.pack(side="top", fill="x")

input_text = Text(root, fg="white", bg="black", font=("Arial", 15))
input_text.place(x=0, y=30, height=30)


num1 = 0
num2 = 0
plus = False
minus = False
multiply = False
divide = False


def addition():
    global plus, minus, multiply, divide, num1, num2

    try:

        if num1 == 0:
            num1 = int((input_text.get('1.0', END)).strip())

        else:
            num2 = int((input_text.get('1.0', END)).strip())
            num1 = num1 + num2
            num2 = 0

        input_text.delete('1.0', END)
        print("num 1 -> " + str(num1) + "; num 2 -> " + str(num2))

        plus = True
        minus = False
        multiply = False
        divide = False

    except ValueError:
        messagebox.showerror("ERROR", "Invalid Argument/Operation \nPlease press correct Operand \nCheck your argument")


def subtraction():
    global plus, minus, multiply, divide, num1, num2

    try:

        if num1 == 0:
            num1 = int((input_text.get('1.0', END)).strip())

        else:
            num2 = int((input_text.get('1.0', END)).strip())
            num1 = num1 - num2
            num2 = 0

        input_text.delete('1.0', END)
        print("num 1 -> " + str(num1) + "; num 2 -> " + str(num2))

        plus = False
        minus = True
        multiply = False
        divide = False

    except ValueError:
        messagebox.showerror("ERROR", "Invalid Argument/Operation \nPlease press correct Operand \n check your argument")


def clear_button():
    global num1, num2
    input_text.delete('1.0', END)
    num1 = 0
    num2 = 0


def multiplication():
    global plus, minus, multiply, divide, num1, num2

    try:

        if num1 == 0:
            num1 = int((input_text.get('1.0', END)).strip())

        else:
            num2 = int((input_text.get('1.0', END)).strip())
            num1 = num1 * num2
            num2 = 0

        input_text.delete('1.0', END)
        print("num 1 -> " + str(num1) + "; num 2 -> " + str(num2))

        plus = False
        minus = False
        multiply = True
        divide = False

    except ValueError:
        messagebox.showerror("ERROR", "Invalid Argument/Operation \nPlease press correct Operand \n check your argument")


def division():
    global plus, minus, multiply, divide, num1, num2

    try:

        if num1 == 0:
            num1 = int((input_text.get('1.0', END)).strip())

        else:
            num2 = int((input_text.get('1.0', END)).strip())
            num1 = int(num1 / num2)
            num2 = 0

        input_text.delete('1.0', END)
        print("num 1 -> " + str(num1) + "; num 2 -> " + str(num2))

        plus = False
        minus = False
        multiply = False
        divide = True

    except ValueError:
        messagebox.showerror("ERROR", "Invalid Argument/Operation \nPlease press correct Operand \n check your argument")


def equals_operator():
    global num2, num1, plus, minus, multiply, divide

    try:
        num2 = int((input_text.get('1.0', END)).strip())
    except ValueError:
        messagebox.showerror("ERROR", "Invalid Argument/Operation \nPlease press correct Operand \n check your argument")

    input_text.delete('1.0', END)
    if plus:
        input_text.insert('1.0', num1 + num2)
    if minus:
        input_text.insert('1.0', num1 - num2)
    if multiply:
        input_text.insert('1.0', num1 * num2)
    if divide:
        input_text.insert('1.0', int(num1 / num2))
    num1 = 0
    num2 = 0
    plus = False
    minus = False
    multiply = False
    divide = False


class IsButton:

    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def set_new_input(self):

        if self.text == "C":
            clear_button()

        elif self.text == "=":
            equals_operator()

        elif self.text == "+":
            addition()

        elif self.text == "-":
            subtraction()

        elif self.text == "*":
            multiplication()

        elif self.text == "/":
            division()

        else:
            input_text.insert(END, self.text)

    def create_button(self, width=5, height=3, master=root, bg="White", fg="Black"):
        Button(master, text=self.text, height=height, width=width,
               command=self.set_new_input, bg=bg, fg=fg).place(x=self.x, y=self.y)


bt1 = IsButton("1", 20, 80)
bt1.create_button()

bt2 = IsButton("2", 100, 80)
bt2.create_button()

bt3 = IsButton("3", 180, 80)
bt3.create_button()

bt4 = IsButton("4", 20, 140)
bt4.create_button()

bt5 = IsButton("5", 100, 140)
bt5.create_button()

bt6 = IsButton("6", 180, 140)
bt6.create_button()

bt7 = IsButton("7", 20, 200)
bt7.create_button()

bt8 = IsButton("8", 100, 200)
bt8.create_button()

bt9 = IsButton("9", 180, 200)
bt9.create_button()

bt0 = IsButton("0", 20, 260)
bt0.create_button()

bt_clear = IsButton("C", 240, 80)
bt_clear.create_button(bg="Blue")

bt_add = IsButton("+", 240, 140)
bt_add.create_button(bg="green")

bt_sub = IsButton("-", 240, 200)
bt_sub.create_button(bg="green")

bt_mul = IsButton("*", 240, 260)
bt_mul.create_button(bg="green")

bt_div = IsButton("/", 180, 260)
bt_div.create_button(bg="Green")

bt_eq = IsButton("=", 100, 260)
bt_eq.create_button(bg="red")

root.mainloop()
