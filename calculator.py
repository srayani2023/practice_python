import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
window=tk.Tk()
window.title('Calculator')
frame=tk.Frame(master=window,bg='cyan',padx=50,pady=50)
frame.pack()
entry=tk.Entry(master=frame,relief='groove',borderwidth=4,width=38)
entry.grid(row=0,column=0,columnspan=4,pady=3)
def myclick(number):
    entry.insert(tk.END,number)
def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo('Error','Syntax Error')
def clear():
    entry.delete(0,tk.END)
bt_1=tk.Button(master=frame,text='1',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(1))
bt_1.grid(column=0,row=1)
bt_2=tk.Button(master=frame,text='2',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(2))
bt_2.grid(column=1,row=1)
bt_3=tk.Button(master=frame,text='3',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(3))
bt_3.grid(column=2,row=1)
bt_add=tk.Button(master=frame,text='+',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick('+'))
bt_add.grid(column=3,row=1)

bt_4=tk.Button(master=frame,text='4',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(4))
bt_4.grid(column=0,row=2)
bt_5=tk.Button(master=frame,text='5',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(5))
bt_5.grid(column=1,row=2)
bt_6=tk.Button(master=frame,text='6',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(6))
bt_6.grid(column=2,row=2)
bt_sub=tk.Button(master=frame,text='-',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick('-'))
bt_sub.grid(column=3,row=2)

bt_7=tk.Button(master=frame,text='7',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(7))
bt_7.grid(column=0,row=3)
bt_8=tk.Button(master=frame,text='8',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(8))
bt_8.grid(column=1,row=3)
bt_9=tk.Button(master=frame,text='9',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(9))
bt_9.grid(column=2,row=3)
bt_mul=tk.Button(master=frame,text='*',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick('*'))
bt_mul.grid(column=3,row=3)

bt_C=tk.Button(master=frame,text='C',font='bold',bg='yellow',padx=15,pady=5,width=3,command=clear)
bt_C.grid(column=0,row=4)
bt_0=tk.Button(master=frame,text='0',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick(0))
bt_0.grid(column=1,row=4)
bt_eq=tk.Button(master=frame,text='=',font='bold',bg='yellow',padx=15,pady=5,width=3,command=equal)
bt_eq.grid(column=2,row=4)
bt_div=tk.Button(master=frame,text='/',font='bold',bg='yellow',padx=15,pady=5,width=3,command=lambda:myclick('/'))
bt_div.grid(column=3,row=4)
window.mainloop()