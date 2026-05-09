from tkinter import *
from tkinter import font, messagebox

r = Tk()
r.geometry("700x500")
s = 30

nums = ["Decimal", "Binary", "Octal", "Hexadecimal"]

#Backebd
def conversion():
    try:
        input_type = type_of_number.get()
        num = number_entry.get()
        output_type = conversion_type.get()
        x = 0
        match input_type:
            case 1:
                match output_type:
                    case 1:
                        x = int(num)
                    case 2:
                        x = bin(int(num))[2:]
                    case 3:
                        x = oct(int(num))[2:]
                    case 4:
                        x = hex(int(num))[2:].upper()
            case 2:
                match output_type:
                    case 1:
                        x = int(num, 2)
                    case 2:
                        x = bin(int(num, 2))[2:]
                    case 3:
                        x = oct(int(num, 2))[2:]
                    case 4:
                        x = hex(int(num, 2))[2:].upper()
            case 3:
                match output_type:
                    case 1:
                        x = int(num, 8)
                    case 2:
                        x = bin(int(num, 8))[2:]
                    case 3:
                        x = oct(int(num, 8))[2:]
                    case 4:
                        x = hex(int(num, 8))[2:].upper()
            case 4:
                match output_type:
                    case 1:
                        x = int(num, 16)
                    case 2:
                        x = bin(int(num, 16))[2:]
                    case 3:
                        x = oct(int(num, 16))[2:]
                    case 4:
                        x = hex(int(num, 16))[2:].upper()
    except:
        messagebox.showerror("Error", "Something went wrong!")                
    Label(r, text = "Output : ", font = font.Font(size = s)).grid(row = 5, sticky = W, padx = 5)
    Output = Entry(r, font = font.Font(size = s), width = 27, border = 5)
    Output.grid(row = 5, sticky = W, pady = 5, padx = 171)                
    Output.delete(0, END)
    Output.insert(0, x)                                                                                            

#Frontend
Label(r, text = "Input in : ", font = font.Font(size = s)).grid(row = 0, sticky = W, padx = 5, pady = 5)
type_of_number = IntVar(value = 1)
for i in range(4):
    Radiobutton(r, text = nums[i], variable = type_of_number, value = i+1, font = font.Font(size = 25)).grid(row = 0, sticky = W, padx = 170 + 155*i, pady = 5)
Label(r, text = "Enter a number : ", font = font.Font(size = s)).grid(row = 2, padx = 5, pady = 5, sticky = W)
number_entry = Entry(r, font = font.Font(size = s), border = 5)
number_entry.grid(row = 2, sticky = W, pady = 5, padx = 320)
Label(r, text = "Covert to : ", font = font.Font(size = s)).grid(row = 3, sticky = W, padx = 5, pady = 50)
conversion_type = IntVar(value = 1)
for i in range(4):
    Radiobutton(r, text = nums[i], variable = conversion_type, value = i+1, font = font.Font(size = 25)).grid(row = 3, sticky = W, padx = 205 + 155*i, pady = 50)
Convert = Button(r, text = "Convert", font = font.Font(size = 30), border = 5, command = conversion).grid(row = 4, sticky = W, padx = 520, pady = 5)
r.mainloop()