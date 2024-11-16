from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("My Calculator App")
def add():
    number1=float(num1.get())
    number2=float(num2.get())
    result=number1+number2
    resultLabel.config(text="Your Result: "+str(result))
    
def sub():
    number1=float(num1.get())
    number2=float(num2.get())
    result=number1-number2
    resultLabel.config(text="Your Result: "+str(result))
def mul():
    number1=float(num1.get())
    number2=float(num2.get())
    result=number1*number2
    resultLabel.config(text="Your Result: "+str(result))
def div():
    number1=float(num1.get())
    number2=float(num2.get())
    result=number1/number2
    resultLabel.config(text="Your Result: "+str(result))
num1Label=Label(root,text="Enter Number 1")
num1Label.pack(pady=20)
num1=Entry(root,width=20)
num1.pack()

num2Label=Label(root,text="Enter Number 2")
num2Label.pack(pady=20)
num2=Entry(root,width=20)
num2.pack()
addBtn=Button(root,text="Add",command=add)
addBtn.pack()

subBtn=Button(root,text="Subtract",command=sub)
subBtn.pack()

mulBtn=Button(root,text="Multiply",command=mul)
mulBtn.pack()

divBtn=Button(root,text="Divide",command=div)
divBtn.pack()



resultLabel=Label(root,text="0")
resultLabel.pack()
root.mainloop()
