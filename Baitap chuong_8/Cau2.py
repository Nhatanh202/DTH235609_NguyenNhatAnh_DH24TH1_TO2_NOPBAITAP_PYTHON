from tkinter import *
from math import sqrt

def tiepAction():
    stringhsA.set("")
    stringhsB.set("")
    stringhsC.set("")
    stringKQ.set("")
def giaiAction():
    a = float( stringhsA.get())
    b = float ( stringhsB.get())
    c = float (stringhsC.get())
    if a==0:
        if b==0 and c==0:
            stringKQ.set("Vô số nghiệm")
        elif b==0 and c!=0:
            stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set("x=" + str(-c/b))
    else:
        delta = b*b - 4*a*c
        if delta<0:
            stringKQ.set("Vô nghiệm")
        elif delta == 0:
            stringKQ.set("x1=x2=" + str(-b/(2*a)))
        else:
            x1 = (-b + sqrt(delta))/(2*a)
            x2 = (-b - sqrt(delta))/(2*a)
            stringKQ.set("x1=" + str(x1) + ", x2=" + str(x2))
root =Tk()
stringhsA = StringVar()
stringhsB = StringVar() 
stringhsC = StringVar()
stringKQ = StringVar()
root.title("PTB2")
root.minsize(150,250)
root.resizable(height=True,width=True)

Label(root, text="Phương trình bậc 2", fg="red", font=("tahoma",16)).grid(row = 0, column=0,columnspan =2)

Label ( root, text = "Hệ số a:").grid(row=1, column = 0)
Entry ( root, width=30, textvariable = stringhsA).grid(row=1, column=1)

Label ( root, text = "Hệ số b:").grid( row = 2, column = 0)
Entry (root, width=30, textvariable = stringhsB).grid (row=2, column=1)

Label (root, text="Hệ số c:").grid(row=3, column = 0)
Entry (root, width=30, textvariable = stringhsC).grid(row =3, column=1)

frameButton = Frame()
Button (frameButton, text="Giải", command=giaiAction).pack(side=LEFT)
Button (frameButton, text = "Tiếp", command=tiepAction).pack(side = LEFT)
Button(frameButton, text = "Thoát", command= root.quit).pack(side=LEFT)
frameButton.grid(row = 4, columnspan=2)

Label (root, text="Kết quả: ").grid(row = 5, column = 0)
Entry (root, width=30, textvariable = stringKQ).grid(row = 5, column = 1 )

root.mainloop()
