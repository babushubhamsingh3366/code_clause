from tkinter import *
root = Tk()
root.title("simple calculator")
e= Entry(root,width=25,bg='white',fg='black',borderwidth=10,font=('Arial',15,'bold'))
e.grid(row=0,column=0,columnspan=5,rowspan=2,padx=27,pady=30,sticky='n')

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number= e.get()
    global f_num
    global math
    math= "add"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, f_num + int(second_number))

    if math == "sub":
        e.insert(0, f_num - int(second_number))

    if math == "mult":
        e.insert(0, f_num * int(second_number))

    if math == "div":
        e.insert(0, f_num / int(second_number))

    if math == "per":
        e.insert(0, f_num % int(second_number))

    if math == "point":
        e.insert(0, f_num . int(second_number))


#######function_____________________

def button_sub():
    first_number= e.get()
    global f_num
    global math
    math= "sub"
    f_num = int(first_number)
    e.delete(0,END)

def button_mult():
    first_number= e.get()
    global f_num
    global math
    math= "mult"
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    first_number= e.get()
    global f_num
    global math
    math= "div"
    f_num = int(first_number)
    e.delete(0,END)

def button_per():
    first_number= e.get()
    global f_num
    global math
    math= "per"
    f_num = int(first_number)
    e.delete(0,END)

def button_point():
    first_number = e.get()
    global f_num
    global math
    math = "point"
    f_num = int(first_number)
    e.delete(0, END)



## butooon______________________________________


button_1 = Button(root,text='1',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(1))
button_2 = Button(root,text='2',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(2))
button_3 = Button(root,text='3',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(3))
button_4 = Button(root,text='4',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(4))
button_5 = Button(root,text='5',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(5))
button_6 = Button(root,text='6',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(6))
button_7 = Button(root,text='7',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(7))
button_8 = Button(root,text='8',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(8))
button_9 = Button(root,text='9',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(9))
button_0 = Button(root,text='0',padx=20,pady=16,bg='grey',fg='white',command=lambda:button_click(0))
button_00= Button(root,text='00',padx=20,pady=16,bg='grey',fg='white',command=lambda :button_click(00))

button_point= Button(root,text='.',padx=20,pady=16,bg='grey',fg='white',command=button_point)
button_dollor= Button(root,text='$',padx=17,pady=15,bg='grey',fg='white',command=lambda:button_dollor())
button_div= Button(root,text='x^y',padx=13,pady=16,bg='grey',fg='white',command=button_div)
button_add = Button(root,text='+',padx=18,pady=15,bg='grey',fg='white',command=button_add)
button_sub = Button(root,text='-',padx=20,pady=16,bg='grey',fg='white',command=button_sub)
button_equal = Button(root,text='=',padx=19,pady=15,bg='orange',fg='white',command=button_equal)
button_clear= Button(root,text='C',padx=19,pady=16,bg='grey',fg='white',command=button_clear)
button_per= Button(root,text='%',padx=19,pady=16,bg='grey',fg='white',command=button_per)
button_mult= Button(root,text='x',padx=19,pady=16,bg='grey',fg='white',command=button_mult)

########## show on screen____________________


button_1.grid(row=5,column=0,pady=7,sticky='e')
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2,padx=2,sticky='w')
button_4.grid(row=4,column=0,pady=7,sticky='e')
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2,padx=2,sticky='w')
button_9.grid(row=3,column=2,padx=2,sticky='w')
button_8.grid(row=3,column=1)
button_7.grid(row=3,column=0,pady=7,sticky='e')
button_0.grid(row=6,column=1)
button_00.grid(row=6,column=0,pady=7,sticky='e')

button_add.grid(row=5,column=3,sticky='w')
button_sub.grid(row=4,column=3,sticky='w')
button_clear.grid(row=2,column=0,pady=7,sticky='e')
button_equal.grid(row=6,column=3,sticky='w')
button_mult.grid(row=3,column=3,padx=4,sticky='w')
button_per.grid(row=2,column=1)
button_point.grid(row=6,column=2,padx=2,sticky='w')
button_dollor.grid(row=2,column=2,padx=2,sticky='w')
button_div.grid(row=2,column=3,padx=2,sticky='w')

root.mainloop()