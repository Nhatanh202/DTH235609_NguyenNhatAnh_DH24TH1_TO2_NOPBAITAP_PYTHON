from tkinter import *

def congAction():
    soA = float (stringA.get())
    soB = float(stringB.get())
    stringKQ.set(soA + soB)
def truAction():
    soA = float (stringA.get())
    soB = float(stringB.get())
    stringKQ.set((soA-soB))
def nhanAction():
    soA = float (stringA.get())
    soB = float(stringB.get())
    stringKQ.set(soA * soB)
def chiaAction():
    soA = float (stringA.get())
    soB = float(stringB.get())
    stringKQ.set(soA / soB)

root = Tk()
root.title("Cộng Trừ Nhân Chia")
root.minsize(150,250)
root.resizable(height=True,width=True)

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

Label (root, text = "Cộng Trừ Nhân Chia", fg= "black", font=("tahome",16)).grid(row=0, columnspan=3)

frameButton = Frame()
Button(frameButton, text="Cộng", command= congAction).pack(side=TOP, fill=X)
Button(frameButton, text="Trừ", command = truAction).pack(side=TOP, fill=X)
Button(frameButton, text = "Nhân", command= nhanAction).pack(side=TOP, fill=X)
Button(frameButton, text = "Chia", command = chiaAction).pack(side=TOP, fill=X)
frameButton.grid(row = 1, column=0, rowspan=4)

Label( root, text="Số A:").grid(row = 1, column =1)
Entry (root, width = 30, textvariable = stringA).grid(row=1, column=2)

Label ( root, text ="Số B: ").grid(row = 2, column = 1)
Entry ( root, width=30, textvariable = stringB).grid(row=2,column=2)

Label (root, text="Kết quả: ").grid(row =3, column =1)
Entry( root, width = 30, textvariable = stringKQ).grid(row=3, column=2)

Button(root, text = "Thoát", command= root.quit).grid(row =4, column=2)
root.mainloop()