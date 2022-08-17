from tkinter import*
import random
import time;

root = Tk()
# root.geometry("1600x800")
root.attributes('-fullscreen', True)
root.title("Gestione Bar")
global text_input
text_input = StringVar()
operator =""

Tops = Frame(root, width = 1600, height = 50,bg="light blue", relief=SUNKEN)
Tops.pack(side=TOP)


f1 = Frame(root, width = 800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700, bg="light blue", relief=SUNKEN)
f2.pack(side=RIGHT)
#=====================TIME===========================
localtime = time.asctime(time.localtime(time.time()))


#=======================INFO==========================
#Restaurant Management System
lblInfo = Label(Tops, font=('arial',50, 'bold'), text = "Gestione Bar", fg = "steel blue", bd = 10,anchor ='w')
lblInfo.grid(row=0, column=0)



#=======================CALCULATION===========================================================================================================
def btnClick(numbers):
        global operator
        operator=operator + str(numbers)
        text_input.set(operator)
        
def btnClearDisplay():
        global operator
        operator=""
        text_input.set("")
        
def btnEqualsInput():
        global operator
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator=""
def Ref():
        x = random.randint(12000, 50098)
        randomRef = str(x)
        rand.set(randomRef)
        '''Coca_Cola = StringVar()
Sprix = StringVar()
Crodino = StringVar()
Panino = StringVar()
Patatine = StringVar()
Pizza = StringVar()'''

        CoCoca_Cola = float(Coca_Cola.get())
        CoSprix = float(Sprix.get())
        CoCrodino = float(Crodino.get())
        CoPanino= float(Panino.get())
        CoPatatine = float (Patatine.get())
        CoPizza =  float(Pizza.get())
        
        CostofCoca_Cola = CoCoca_Cola * 1.50
        CostofSprix = CoSprix  * 1.75
        CostofCrodino = CoCrodino * 1.00 
        CostofPanino = CoPanino * 4.50
        CostofPatatine = CoPatatine * 3.50
        CostofPizza = CoPizza * 5.90

        CostofMeal = "EUR", str('%.2f' %( CostofCoca_Cola + CostofSprix + CostofCrodino + CostofPanino + CostofPatatine + CostofPizza ))
        
        PayTax = ((CostofCoca_Cola + CostofSprix + CostofCrodino + CostofPanino + 
                                                                CostofPatatine + CostofPizza )* 0.2)
                                                                
        TotalCost = (CostofCoca_Cola + CostofSprix + CostofCrodino + CostofPanino + 
                                                                CostofPatatine + CostofPizza )
                                                                
        Ser_Charge =(( CostofCoca_Cola + CostofSprix + CostofCrodino + CostofPanino + 
                                                                CostofPatatine + CostofPizza )/99)

        Service = "EUR", str('%.2f' % Ser_Charge)
        
        OverAllCost = "EUR", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

        PaidTax = "EUR",str('%.2f' %PayTax)

        service_Charge.set(Service)
        Cost.set(CostofMeal)
        Tax.set(PaidTax)
        SubTotal.set(CostofMeal)
        Total.set(OverAllCost)
        
def qExit():
        root.destroy()

def Reset():
        rand.set("")
        Coca_Cola.set("")
        Sprix.set("")
        Crodino.set("")
        Panino.set("")
        Patatine.set("")
        Pizza.set("")
        service_Charge.set("")
        Tax.set("")
        Cost.set("")
        SubTotal.set("")
        Total.set("")


        
txtDisplay = Entry(f2, font=('arial',20, 'bold'), textvariable=text_input, bd = 30, insertwidth=4, bg = "powder blue", justify = 'right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="7", bg="powder blue", command=lambda:btnClick(7))
btn7.grid(row=2, column = 0)

btn8 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="8", bg="powder blue", command=lambda:btnClick(8))
btn8.grid(row=2, column = 1)

btn9 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="9", bg="powder blue", command=lambda:btnClick(9))
btn9.grid(row=2, column = 2)

Addition = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="+", bg="powder blue", command=lambda:btnClick("+"))
Addition.grid(row=2, column = 3)

#=============================================================================================================================================
btn4 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="4", bg="powder blue", command=lambda:btnClick(4))
btn4.grid(row=3, column = 0)

btn5 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="5", bg="powder blue", command=lambda:btnClick(5))
btn5.grid(row=3, column = 1)

btn6 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="6", bg="powder blue", command=lambda:btnClick(6))
btn6.grid(row=3, column = 2)

Subtraction = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="-", bg="powder blue", command=lambda:btnClick("-"))
Subtraction.grid(row=3, column = 3)
#=============================================================================================================================================
btn1 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="1", bg="powder blue", command=lambda:btnClick(1))
btn1.grid(row=4, column = 0)

btn2 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="2", bg="powder blue", command=lambda:btnClick(2))
btn2.grid(row=4, column = 1)

btn3 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="3", bg="powder blue", command=lambda:btnClick(3))
btn3.grid(row=4, column = 2)

Multiplication = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="*", bg="powder blue", command=lambda:btnClick("*"))
Multiplication.grid(row=4, column = 3)

#================================================================================================================================================
btn0 = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="0", bg="powder blue", command=lambda:btnClick(0))
btn0.grid(row=5,column = 0)

Del = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="Del", bg="powder blue", command=btnClearDisplay)
Del.grid(row=5, column = 3)

Equal = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="=", bg="powder blue", command=btnEqualsInput)
Equal.grid(row=5, column = 2)

Division = Button(f2, padx=16,pady=16,bd=8,fg="black", font=('arial', 20, 'bold'),text="/", bg="powder blue", command=lambda:btnClick("/"))
Division.grid(row=5, column = 1)
#===============================================================================================================================================
rand =StringVar()
Coca_Cola = StringVar()
Sprix = StringVar()
Crodino = StringVar()
Panino = StringVar()
Patatine = StringVar()
Pizza = StringVar()
service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
SubTotal = StringVar()
Total = StringVar()



lblReference = Label(f1,font=('arial',12, 'bold'),text = "Numero Ordine",bd = 16,anchor='w')
lblReference.grid(row=0,column=0)

txtReference = Entry(f1,font=('arial',12, 'bold'),textvariable = rand,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtReference.grid(row=0,column=1)

lblCoca_Cola = Label(f1,font=('arial',12, 'bold'),text = "Coca Cola (1.50 EUR)",bd = 16,anchor='w')
lblCoca_Cola.grid(row=1,column=0)

txtCoca_Cola = Entry(f1,font=('arial',12, 'bold'),textvariable = Coca_Cola,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtCoca_Cola.grid(row=1,column=1)

#===============================================================================================================================

lblSprix = Label(f1,font=('arial',12, 'bold'),text = "Sprix (1.75 EUR)",bd = 16,anchor='w')
lblSprix.grid(row=2,column=0)

txtSprix = Entry(f1,font=('arial',12, 'bold'),textvariable = Sprix,insertwidth = 3, bg = 'powder blue',bd =4,justify ='right')
txtSprix.grid(row=2,column=1)

lblCrodino = Label(f1,font=('arial',12, 'bold'),text = "Crodino (1.00 EUR)",bd = 16,anchor='w')
lblCrodino.grid(row=3,column=0)

txtFilet = Entry(f1,font=('arial',12, 'bold'),textvariable = Crodino,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtFilet.grid(row=3,column=1)

lblSubTotal = Label(f1,font=('arial',12, 'bold'),text = "SubTotale",bd = 16,anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal = Entry(f1,font=('arial',12, 'bold'),textvariable = SubTotal,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtSubTotal.grid(row=4,column=3)

lblTotal = Label(f1,font=('arial',12, 'bold'),text = "Totale",bd = 16,anchor='w')
lblTotal.grid(row=5,column=2)

txtTotal = Entry(f1,font=('arial',12, 'bold'),textvariable = Total,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtTotal.grid(row=5,column=3)

lblservice_Charge = Label(f1,font=('arial',12, 'bold'),text = "Servizio",bd = 16,anchor='w')
lblservice_Charge.grid(row=3,column=2)

txtservice_Charge = Entry(f1,font=('arial',12, 'bold'),textvariable = service_Charge,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtservice_Charge.grid(row=3,column=3)

lblTax = Label(f1,font=('arial',12, 'bold'),text = "Tasse",bd = 16,anchor='w')
lblTax.grid(row=1,column=2)

txtTax = Entry(f1,font=('arial',12, 'bold'),textvariable = Tax,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtTax.grid(row=1,column=3)

lblCost = Label(f1,font=('arial',12, 'bold'),text = "Costo",bd = 16,anchor='w')
lblCost.grid(row=2,column=2)

txtCost = Entry(f1,font=('arial',12, 'bold'),textvariable = Cost,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtCost.grid(row=2,column=3)

lblPanino = Label(f1,font=('arial',12, 'bold'),text = "Panino (4.50 EUR)",bd = 16,anchor='w')
lblPanino.grid(row=0,column=2)

txtPanino = Entry(f1,font=('arial',12, 'bold'),textvariable = Panino,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtPanino.grid(row=0,column=3)

lblPatatine = Label(f1,font=('arial',12, 'bold'),text = "Patatine (3.50 EUR)",bd = 16,anchor='w')
lblPatatine.grid(row=4,column=0)

txtPatatine = Entry(f1,font=('arial',12, 'bold'),textvariable = Patatine,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtPatatine.grid(row=4,column=1)

lblPizza = Label(f1,font=('arial',12, 'bold'),text = "Pizza (5.90 EUR)",bd = 16,anchor='w')
lblPizza.grid(row=5,column=0)

txtPizza = Entry(f1,font=('arial',12, 'bold'),textvariable = Pizza,insertwidth = 4, bg = 'powder blue',bd =4,justify ='right')
txtPizza.grid(row=5,column=1)
#=================================================================================================================================================================
btnTotal= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Totale", bg = "powder blue",  command = Ref ).grid(row= 7,column = 1)

btnReset= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Resetta", bg = "powder blue",  command = Reset ).grid(row= 7,column = 2)

btnExit= Button(f1,padx=16,pady = 16,bd= 16,fg= "black",font = ('arial',16,'bold'),width = 10,text= "Esci", bg = "powder blue",  command = qExit ).grid(row= 7,column = 3)


	
root.mainloop()