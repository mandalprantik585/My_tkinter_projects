from tkinter import *
from tkinter import font, messagebox

r = Tk()
r.geometry("500x400")
s = 17

#Backend
def two_variable_solver(equation_1_entry, equation_2_entry):
    try:
        equation_1 = equation_1_entry.get()
        equation_2 = equation_2_entry.get()
        unknowns = []
        coefficients = []
        ks = []
        i = 0
        temp = []
        for j in range(len(equation_1)):
            if equation_1[j] in "abxyABXY":
                unknowns.append(equation_1[j])
                temp.append(int(equation_1[i:j]))
                i = j+1
            elif equation_1[j] == "=":
                ks.append(int(equation_1[j+1:]))
        coefficients.append(temp)
        temp = []
        i = 0
        for j in range(len(equation_2)):
            if equation_2[j] in "abxyABXY":
                temp.append(int(equation_2[i:j]))
                i = j+1
            elif equation_2[j] == "=":
                ks.append(int(equation_2[j+1:]))
        coefficients.append(temp)
        a1, a2 = coefficients[0][0], coefficients[1][0]
        b1, b2 = coefficients[0][1], coefficients[1][1]
        k1, k2 = ks[0], ks[1]
        x = (b2*k1 - b1*k2)/(a1*b2 - a2*b1)
        y = (k1 - a1*x)/b1
        Label(r, text = "Solutions : ", font = font.Font(size = s)).grid(row = 5, sticky = W, padx = 5, pady = 5)
        Solutions = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        Solutions.grid(row = 5, padx = 210, pady = 5)
        Solutions.delete(0, END)
        Solutions.insert(0, f"{unknowns[0]} = {round(x, 4)}, {unknowns[1]} = {round(y, 4)}")
    except:
        messagebox.showerror("Error", "Something went wrong!")
def three_variable_solver(equation_1_entry, equation_2_entry, equation_3_entry):
    try:    
        equation_1 = equation_1_entry.get()
        equation_2 = equation_2_entry.get()
        equation_3 = equation_3_entry.get()
        unknowns = []
        coefficients = []
        ks = []
        i = 0
        temp = []
        for j in range(len(equation_1)):
            if equation_1[j] in "abcxyzABCDXYZ":
                unknowns.append(equation_1[j])
                temp.append(int(equation_1[i:j]))
                i = j+1
            elif equation_1[j] == "=":
                ks.append(int(equation_1[j+1:]))
        coefficients.append(temp)
        temp = []
        i = 0
        for j in range(len(equation_2)):
            if equation_2[j] in "abcxyzABCDXYZ":
                temp.append(int(equation_2[i:j]))
                i = j+1
            elif equation_2[j] == "=":
                ks.append(int(equation_2[j+1:]))
        coefficients.append(temp)
        temp = []        
        i = 0
        for j in range(len(equation_3)):
            if equation_3[j] in "abcxyzABCDXYZ":
                temp.append(int(equation_3[i:j]))
                i = j+1
            elif equation_3[j] == "=":
                ks.append(int(equation_3[j+1:]))        
        coefficients.append(temp)
        a1, a2, a3 = coefficients[0][0], coefficients[1][0], coefficients[2][0]
        b1, b2, b3 = coefficients[0][1], coefficients[1][1], coefficients[2][1]
        c1, c2, c3 = coefficients[0][2], coefficients[1][2], coefficients[2][2]
        k1, k2, k3 = ks[0], ks[1], ks[2]
        z = (((a1*k2 - a2*k1)/(a1*b2 - a2*b1)) - ((a1*k3 - a3*k1) / (a1*b3 - a3*b1))) / (((a1*c2 - a2*c1) / (a1*b2 - a2*b1)) - ((a1*c3 - a3*c1) / (a1*b3 - a3*b1)))
        y = ((a1*k3 - a3*k1) - ((a1*c3 - a3*c1)*z)) / (a1*b3 - a3*b1)
        x = (k1 - b1*y - c1*z) / a1
        Label(r, text = "Solutions : ", font = font.Font(size = s)).grid(row = 6, sticky = W, padx = 5, pady = 5)
        Solutions = Entry(r, font = font.Font(size = s), border = 5, width = 50)
        Solutions.grid(row = 6, padx = 210, pady = 5)
        Solutions.delete(0, END)
        Solutions.insert(0, f"{unknowns[0]} = {round(x, 4)}, {unknowns[1]} = {round(y, 4)}, {unknowns[2]} = {round(z, 4)}")
    except:
        messagebox.showerror("Error", "Something went wrong!")    
def goto():
    type_eq = type_eq_entry.get()
    if type_eq == 2:
        Label(r, text = "Enter 1st equation : ", font = font.Font(size = s)).grid(row = 2, sticky = W, padx = 5, pady = 5)
        equation_1_entry = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        equation_1_entry.grid(row = 2, padx = 210, pady = 5)
        Label(r, text = "Enter 2nd equation : ", font = font.Font(size = s)).grid(row = 3, sticky = W, padx = 5, pady = 5)
        equation_2_entry = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        equation_2_entry.grid(row = 3, padx = 210, pady = 5)
        Solve = Button(r, text = "Solve", font = font.Font(size = 20), border = 5, command = lambda : two_variable_solver(equation_1_entry, equation_2_entry))
        Solve.grid(row = 4, padx = 210, pady = 5)
    else:
        Label(r, text = "Enter 1st equation : ", font = font.Font(size = s)).grid(row = 2, sticky = W, padx = 5, pady = 5)
        equation_1_entry = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        equation_1_entry.grid(row = 2, padx = 210, pady = 5)
        Label(r, text = "Enter 2nd equation : ", font = font.Font(size = s)).grid(row = 3, sticky = W, padx = 5, pady = 5)
        equation_2_entry = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        equation_2_entry.grid(row = 3, padx = 210, pady = 5)
        Label(r, text = "Enter 3rd equation : ", font = font.Font(size = s)).grid(row = 4, sticky = W, padx = 5, pady = 5)
        equation_3_entry = Entry(r, font = font.Font(size = s), border = 5, width = 35)
        equation_3_entry.grid(row = 4, padx = 210, pady = 5)
        Solve = Button(r, text = "Solve", font = font.Font(size = 20), border = 5, command = lambda : three_variable_solver(equation_1_entry, equation_2_entry, equation_3_entry))
        Solve.grid(row = 5, padx = 210, pady = 5)
           
#Frontend
Label(r, text = "Choose the type equation : ", font = font.Font(size = s)).grid(row = 0, sticky = W, padx = 5, pady = 5)
type_eq_entry = IntVar(value = 2)
Radiobutton(r, text = "2 variable", font = font.Font(size = s), variable = type_eq_entry, value = 2).grid(row = 0, sticky = W, padx = 280, pady = 5)
Radiobutton(r, text = "3 variable", font = font.Font(size = s), variable = type_eq_entry, value = 3).grid(row = 0, sticky = W, padx = 420, pady = 5)
next_button = Button(r, text = "Next", font = font.Font(size = 20), border = 5, command = goto)
next_button.grid(row = 1, sticky = W, padx = 420, pady = 20)

r.mainloop()