from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=50,borderwidth=5)

class calc():
    def __init__(self):
        self.f_num = 0
        self.i=0
        self.sign=""

    def add(self):
        firstnumber=e.get()
        e.delete(0,END)
        if(self.i is 0):
            self.i=self.i+1
            print(self.i)
            self.f_num=int(firstnumber)
            print(self.f_num)
            
        elif (self.i is 1):
            self.f_num=self.f_num+int(firstnumber)
            e.insert(0,self.f_num)
            print(self.f_num)
            self.i=0
            print(self.i)
            print(self.f_num)
            self.sign=2
            
        elif (self.i is 2):
            self.sign=0
            e.delete(0,END)
            sw.myfunc(self.sign)
    
    def subtract(self):
        firstnumber=e.get()
        e.delete(0,END)
        if(self.i is 0):
            self.i=self.i+1
            print(self.i)
            self.f_num=int(firstnumber)
            print(self.f_num)
            
        elif (self.i is 1):
            self.f_num=self.f_num-int(firstnumber)
            e.insert(0,self.f_num)
            print(self.f_num)
            self.i=0
            print(self.i)
            print(self.f_num)
            
        elif (self.i is 2):
            self.sign=1
            sw.myfunc(self.sign)

    def multiply(self):
        firstnumber=e.get()
        e.delete(0,END)
        if(self.i is 0):
            self.i=self.i+1
            print(self.i)
            self.f_num=int(firstnumber)
            print(self.f_num)
            
        elif (self.i is 1):
            self.f_num=self.f_num/int(firstnumber)
            e.insert(0,self.f_num)
            print(self.f_num)
            self.i=0
            print(self.i)
            print(self.f_num)
            
        elif (self.i is 2):
            self.sign=2
            sw.myfunc(self.sign)

    def divide(self):
        
        firstnumber=e.get()
        e.delete(0,END)
        if(self.i is 0):
            self.i=self.i+1
            print(self.i)
            self.f_num=int(firstnumber)
            print(self.f_num)
            
        elif (self.i is 1):
            self.f_num=self.f_num/int(firstnumber)
            e.insert(0,self.f_num)
            print(self.f_num)
            self.i=0
            print(self.i)
            print(self.f_num)
            
        elif (self.i is 2):
            self.sign=3
            sw.myfunc(self.sign)

    def clear(self):
        e.delete(0,END)
        self.f_num=0
        self.i=0
        self.sign=""

    def equal(self):
        print(self.f_num)
        e.insert(0,str(self.f_num))
        self.i=2

    def numbersentry(self,number):
        current=e.get()
        e.delete(0,END) 
        st=str(current)+str(number)
        e.insert(0,st)

    def decimal(self,number):
        self.sign=6

    def myfunc(self,o):
        if (self.i is 2):
            self.i=1
        switcher={0:sw.add,1:sw.subtract,2:sw.multiply,3:sw.divide,4:sw.equal,5:sw.clear,6:sw.decimal}
        func=switcher.get(0,lambda :'Invalid')
        return func

sw=calc()


mybuttonequal=Button(root,text="=",command=sw.myfunc(4),padx=40,pady=52)
mybuttonadd=Button(root,text="+",command=sw.myfunc(0),padx=40,pady=52)
mybuttonsub=Button(root,text="-",command=sw.myfunc(1),padx=40,pady=20)
mybuttondiv=Button(root,text="/",command=sw.myfunc(3),padx=40,pady=20)
mybuttonmulti=Button(root,text="*",command=sw.myfunc(2),padx=40,pady=20)
mybuttonclr=Button(root,text="C",command=sw.myfunc(5),padx=40,pady=20)
mybuttonpoint=Button(root,text=".",command=sw.myfunc(6),padx=42,pady=20)

mybutton9=Button(root,text="9",command=lambda:sw.numbersentry(9),padx=40,pady=20)
mybutton8=Button(root,text="8",command=lambda:sw.numbersentry(8),padx=40,pady=20)
mybutton7=Button(root,text="7",command=lambda:sw.numbersentry(7),padx=40,pady=20)
mybutton6=Button(root,text="6",command=lambda:sw.numbersentry(6),padx=40,pady=20)
mybutton5=Button(root,text="5",command=lambda:sw.numbersentry(5),padx=40,pady=20)
mybutton4=Button(root,text="4",command=lambda:sw.numbersentry(4),padx=40,pady=20)
mybutton3=Button(root,text="3",command=lambda:sw.numbersentry(3),padx=40,pady=20)
mybutton2=Button(root,text="2",command=lambda:sw.numbersentry(2),padx=40,pady=20)
mybutton1=Button(root,text="1",command=lambda:sw.numbersentry(1),padx=40,pady=20)
mybutton0=Button(root,text="0",command=lambda:sw.numbersentry(0),padx=89,pady=20)


e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

mybutton9.grid(row=2,column=2)
mybutton8.grid(row=2,column=1)
mybutton7.grid(row=2,column=0)
mybutton6.grid(row=3,column=2)
mybutton5.grid(row=3,column=1)
mybutton4.grid(row=3,column=0)
mybutton3.grid(row=4,column=2)
mybutton2.grid(row=4,column=1)
mybutton1.grid(row=4,column=0)
mybutton0.grid(row=5,column=0,columnspan=2)
mybuttonpoint.grid(row=5,column=2)
mybuttonequal.grid(row=4,column=3,rowspan=2)
mybuttonadd.grid(row=2,column=3,rowspan=2)
mybuttonsub.grid(row=1,column=3)
mybuttondiv.grid(row=1,column=1)
mybuttonmulti.grid(row=1,column=2)
mybuttonclr.grid(row=1,column=0)


root.mainloop()