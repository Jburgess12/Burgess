from tkinter import Tk, StringVar, ttk
from tkinter import *
import time
import datetime

root = Tk()
root.title("Currency Converter")
root.geometry('1000x300+0+0')
root.configure(background='black')

LeftMainFrame = Frame(root, width =660, height=400, bd=8, relief="raise")
LeftMainFrame.pack(side=LEFT)
RightMainFrame = Frame(root, width =200, height=400, bd=8, relief="raise")
RightMainFrame.pack(side=RIGHT)

DateofOrder = StringVar()
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()
#----------------------------------------------------------------
def ConCurrency():
    if value0.get() == "Japan":
        convert1 = float(convert.get() * 113.39)
        convert2 = "Japan Tokyo", str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "USA":
        convert1 = float(convert.get() * .0088)
        convert2 = "USA Dallas", str('%.2f' %(convert1))
        currency.set(convert2)
    if value0.get() == "Japan":
        convert1 = float(convert.get() * 113.39)
        convert2 = "Japan Tokyo", str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "USA":
        convert1 = float(convert.get() * .0088)
        convert2 = "USA Dallas", str('%.2f' %(convert1))
        currency.set(convert2)
#--------------------------------Exit----------------------------


def Reset():
    value0.set("")
    convert.set("0.0")
    currency.set("0.0")

#--------------------------------Date-----------------------------
DateofOrder.set(time.strftime("%d/%m/%Y"))
#-----------------------------------------------------------------

EntCurrency= Entry(LeftMainFrame, font=('arial',20,'bold'), textvariable=convert, bd=2,width=28, justify='center')
EntCurrency.grid(row=0,column=1)

JpyUSDollar= Label(LeftMainFrame,font=('arial',20,'bold'), text='USA Dollar equals', padx=2, pady=2, bd=2, fg="black", width=18)
JpyUSDollar.grid(row=0,column=2, sticky=W)

box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly',font=('arial', 20, 'bold'),width=20)
box['values'] = (' ','Japan','USA')
box.current(0)
box.grid(row=4, column=2)

UsdCurrency= Label(LeftMainFrame,font=('arial',20,'bold'),  textvariable=currency, bd=2,width=25,bg='white', pady=2,padx=2, relief='sunken')
UsdCurrency.grid(row=4,column=1)
#------------------------------------------------------------------------------------------------------------------------------------------

UsdDateofOrder = Label(RightMainFrame,font=('arial',20,'bold'), textvariable=DateofOrder, padx=2, pady=2, bd=2, fg="black", width=12, justify='center')
UsdDateofOrder.grid(row=0,column=0, sticky=W)

btnConvert = Button(RightMainFrame, text='Convert', padx=2, pady=2, bd=2, fg="black", font=('arial', 20, 'bold'), width= 12, height=1, command = ConCurrency).grid(row=1,column=0)

btnReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg="black", font=('arial', 20, 'bold'), width= 12, height=1, command = Reset).grid(row=2,column=0)

btnExit = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg="black", font=('arial', 20, 'bold'), width= 12, height=1, command = exit).grid(row=3,column=0)





root.mainloop()
