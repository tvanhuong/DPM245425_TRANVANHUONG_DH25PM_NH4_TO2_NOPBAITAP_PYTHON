from tkinter import *
#hi
def tiepAction():
    stringA.set("")
    stringB.set("")
    stringKQ.set("")
def giaiAction():
    a=float(stringA.get())
    b=float(stringB.get())
    if a==0 and b==0:
        stringKQ.set("Phuong trinh vo so nghiem")
    elif a==0 and b!=0:
        stringKQ.set("Phuong trinh vo nghiem")
    else:
     
        stringKQ.set("Phuong trinh co nghiem x = "+str((-b/a)))
        
root = Tk()

stringA=StringVar()
stringB=StringVar()
stringKQ=StringVar()

root.title("Giai phuong trinh bac nhat")
root.minsize(height=200,width=250)
Label(root,text="Phuong trinh bac nhat",fg="blue",font=("Arial",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="He so a").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringA).grid(row=1,column=1)

Label(root,text="He so b").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringB).grid(row=2, column=1)

frameButton=Frame(root)
Button(frameButton,text="Giai",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="Tiep",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoat",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)


Label(root,text="Ket qua").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)

root.mainloop()