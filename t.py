#!/usr/bin/python3
from tkinter import *
from turtle import onclick

root = Tk()
root.title("CASIO mX900")
# def padd(r,s,e):
#     for i in range(s,e):
#         l = Label(root,text="")
#         l.grid(row=r,column=i)
#         del l

# def onclick(num):
#     print(f"you clicked {num}")


# l1 = Label(root,text="one").grid(row=0,column=0)
# padd(1,1,30)
# l2 = Label(root,text="twwwwwo").grid(row=1,column=30)
# padd(3,0,5)
n1 = 0
def ins(n):
    # global n1
    # n1+=1
    # print(inp1.get())
    inp1.insert(len(inp1.get()),n)
def clear():
    curr = inp1.get()
    inp1.delete(0,len(curr))

inp1 = Entry(root,width=25,border=10,font=20)
inp1.grid(row=0,column=0,columnspan=4)

def equal():
    res = eval(inp1.get())
    inp1.delete(0,len(inp1.get()))
    inp1.insert(0,str(res))

def backspace():
    curr = list(inp1.get())
    curr[-1] = ""
    curr = "".join(curr)
    inp1.delete(0,len(inp1.get()))
    inp1.insert(0,curr)


bt1 = Button(root,text="1",command=lambda:ins("1"),border=3,width=9,height=3).grid(row=1,column=0)
bt2 = Button(root,text="2",command=lambda:ins("2"),border=3,width=9,height=3).grid(row=1,column=1)
bt3 = Button(root,text="3",command=lambda:ins("3"),border=3,width=9,height=3).grid(row=1,column=2)
bts = Button(root,text="*",command=lambda:ins("*"),border=3,width=9,height=3).grid(row=1,column=3)
bt4 = Button(root,text="4",command=lambda:ins("4"),border=3,width=9,height=3).grid(row=2,column=0)
bt5 = Button(root,text="5",command=lambda:ins("5"),border=3,width=9,height=3).grid(row=2,column=1)
bt6 = Button(root,text="6",command=lambda:ins("6"),border=3,width=9,height=3).grid(row=2,column=2)
btd = Button(root,text="/",command=lambda:ins("/"),border=3,width=9,height=3).grid(row=2,column=3)
bt7 = Button(root,text="7",command=lambda:ins("7"),border=3,width=9,height=3).grid(row=3,column=0)
bt8 = Button(root,text="8",command=lambda:ins("8"),border=3,width=9,height=3).grid(row=3,column=1)
bt9 = Button(root,text="9",command=lambda:ins("9"),border=3,width=9,height=3).grid(row=3,column=2)
eq = Button(root,text="=",command=lambda:equal(),border=3,width=9,height=3).grid(row=3,column=3)
btp = Button(root,text="+",command=lambda:ins("+"),border=3,width=9,height=3).grid(row=4,column=0)
bt0 = Button(root,text="0",command=lambda:ins("0"),border=3,width=9,height=3).grid(row=4,column=1)
btm = Button(root,text="-",command=lambda:ins("-"),border=3,width=9,height=3).grid(row=4,column=2)
back = Button(root,text="X",command=lambda:backspace(),border=3,width=9,height=3).grid(row=4,column=3)
btclear = Button(root,text="clear",pady=10,padx=10,command=lambda:clear(),width=30,height=2).grid(row=6,column=0,columnspan=3)
dot = Button(root,text=".",command=lambda:ins("."),border=3,width=9,height=3).grid(row=6,column=3)

root.mainloop()
