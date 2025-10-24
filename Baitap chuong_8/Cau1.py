from tkinter import *

def tiepAction():
    stringhsA.set("")
    stringhsB.set("")
    stringKQ.set("")

def giaiAction():
    a = float(stringhsA.get())
    b = float(stringhsB.get())
    if a == 0:
        if b == 0:
            stringKQ.set("Phương trình vô số nghiệm")
        else:
            stringKQ.set("Phương trình vô nghiệm")
    else:
        stringKQ.set("x=" + str(-b/a))
root = Tk()
stringhsA = StringVar()
stringhsB = StringVar()
stringKQ = StringVar()

root.title("PTB1")
root.minsize(150, 250)
root.resizable(height=True, width=True)

Label(root,text="Phương Trình Bậc1",fg="red",font=("tohama",16),justify=CENTER).grid(row=0,columnspan=2)
Label(root,text="Hệ số a:").grid(row=1,column=0)
Entry(root,width=30,textvariable=stringhsA).grid(row=1,column=1)
Label(root,text="Hệ số b:").grid(row=2,column=0)
Entry(root,width=30,textvariable=stringhsB).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text="Giải",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="Tiếp",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)

Label(root,text="Kết quả:").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)

root.mainloop()