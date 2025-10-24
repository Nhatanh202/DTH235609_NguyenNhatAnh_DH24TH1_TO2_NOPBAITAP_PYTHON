from tkinter import *
from tkinter import messagebox

def clearAction():
    stringOldPass.set("")
    stringNewPass.set("")
    stringEnterNewPass.set("")
def okAction():
    oldPass = stringOldPass.get().strip().lower()
    newPass = stringNewPass.get().strip().lower()
    enterNewPass = stringEnterNewPass.get().strip().lower()
    if newPass == oldPass:
        messagebox.showerror("Error", "Bạn không được dùng mật khẩu cũ")
    elif newPass != enterNewPass:
        messagebox.showerror("Error", "Bạn phải nhập mật khẩu mới giống nhau")
    else:
        messagebox.showinfo("Success", "Cập nhật mật khẩu thành công")

root = Tk()
root.minsize(200,150)
root.resizable(height=True,width=True)
root.title("Enter New Password")

stringOldPass = StringVar()
stringNewPass = StringVar()
stringEnterNewPass = StringVar()

Label (root, text = "Old Password: ").grid (row = 1, column = 0)
Entry (root, width=30, textvariable = stringOldPass, show="*").grid(row=1, column =2)

Label (root, text= "New Password: ").grid (row = 2, column = 0)
Entry (root, width = 30, textvariable = stringNewPass, show ="*").grid(row = 2, column =2)

Label (root, text = "Enter New Password Again: ").grid (row=3, column=0)
Entry (root, width =30, textvariable = stringEnterNewPass, show="*").grid(row=3, column=2)

frameButton = Frame()
Button (frameButton, text = "OK", command = okAction).pack(side = LEFT)
Button (frameButton, text = "Cancel", command= root.quit).pack (side = LEFT)
frameButton.grid(row=4, columnspan=3)

root.mainloop() 