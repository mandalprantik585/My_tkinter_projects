from tkinter import *
from tkinter import font, messagebox

r = Tk()
r.geometry("700x800")

#Backend
def calculate():
    try:
        buying_price = int(buying_price_entry.get())
        quantity = int(quantity_entry.get())
        profit_margin = int(profit_margin_entry.get())
        profit_lose_ratio = profit_lose_ratio_entry.get()
        x = profit_lose_ratio.split(":")
        lose_margin = profit_margin*(int(x[-1])/int(x[0]))

        target_price = buying_price*(1+0.01*profit_margin)
        stop_lose = buying_price*(1-0.01*lose_margin)
        BEP = (buying_price*quantity+40)/(0.9995*quantity)

        target_price_entry.delete(0, END)
        stop_lose_entry.delete(0, END)
        BEP_entry.delete(0, END)   

        target_price_entry.insert(0, round(target_price, 2))
        stop_lose_entry.insert(0, round(stop_lose, 2))
        BEP_entry.insert(0, round(BEP, 2))
    except:
        messagebox.showerror("Error", "Something went wrong!!")

#Quantity
Label(r, text = "Quantity : ", font = font.Font(size = 20)).grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
quantity_entry = Entry(r, font = font.Font(size = 20), border = 5)
quantity_entry.grid(row = 0, column = 1)

#Buying price
Label(r, text = "Buying price : ", font = font.Font(size = 20)).grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
buying_price_entry = Entry(r, font = font.Font(size = 20), border = 5)
buying_price_entry.grid(row = 1, column = 1)

#Profit margin
Label(r, text = "Profit margin(in %) : ", font = font.Font(size = 20)).grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
profit_margin_entry = Entry(r, font = font.Font(size = 20), border = 5)
profit_margin_entry.grid(row = 2, column = 1)
profit_margin_entry.insert(0, 1)

#Profit and lose ratio
Label(r, text = "Profit : Lose ", font = font.Font(size = 20)).grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
profit_lose_ratio_entry = Entry(r, font = font.Font(size = 20), border = 5)
profit_lose_ratio_entry.grid(row = 3, column = 1)
profit_lose_ratio_entry.insert(0, "2:1")

#Go button
go = Button(r, text = "GO", border = 5, font = font.Font(size = 20), command = calculate)
go.grid(row = 4, column = 1, pady = 40)

#Target price
Label(r, text = "Target price : ", font = font.Font(size = 20)).grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)
target_price_entry = Entry(r, font = font.Font(size = 20), border = 5)
target_price_entry.grid(row = 5, column = 1)

#Stop lose
Label(r, text = "Stop lose : ", font = font.Font(size = 20)).grid(row = 6, column = 0, padx = 10, pady = 10, sticky = W)
stop_lose_entry = Entry(r, font = font.Font(size = 20), border = 5)
stop_lose_entry.grid(row = 6, column = 1)

#BEP
Label(r, text = "BEP : ", font = font.Font(size = 20)).grid(row = 7, column = 0, padx = 10, pady = 10, sticky = W)
BEP_entry = Entry(r, font = font.Font(size = 20), border = 5)
BEP_entry.grid(row = 7, column = 1)

r.mainloop()