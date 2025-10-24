from tkinter import * 

# Biến toàn cục để lưu phép tính dưới dạng chuỗi
expression = ""

# --- CÁC HÀM XỬ LÝ KHI NHẤN NÚT ---
def press(num):
    """Hàm này được gọi khi nhấn nút số hoặc phép toán (+, -, *, /)."""
    global expression
    expression = expression + str(num)  # Nối số/ký tự vào chuỗi phép tính
    equation.set(expression)            # Cập nhật lại màn hình

def equalpress():
    """Hàm này được gọi khi nhấn nút '='."""
    try:
        global expression
        total = str(eval(expression))     # Dùng hàm eval() để tính kết quả
        equation.set(total)               # Hiển thị kết quả lên màn hình
        expression = total                # Lưu lại kết quả để có thể tính tiếp
    except:
        equation.set(" Lỗi ")             # Nếu phép tính sai, báo lỗi
        expression = ""

def clear():
    clearExpression = ""
    equation.set(clearExpression)

# --- THIẾT KẾ GIAO DIỆN ---

root = Tk()
root.resizable(height=True,width=True)
root.title("Máy tính")

equation = StringVar()
display = Entry(root, textvariable=equation, justify='right').grid(row=0, columnspan=4, sticky="ew") 

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

r = 1 # Bắt đầu từ hàng 1
c = 0 # Bắt đầu từ cột 0
for btn_text in buttons:
    
    Button(root, text=btn_text, command=lambda t=btn_text: press(t)).grid(row=r, column=c)
    c += 1
    if c > 3: 
        c = 0
        r += 1

Button(root, text='=', command=equalpress).grid(row=4, column=2)
Button(root, text='Clr', command=clear).grid(row=5, columnspan=4, sticky="ew")

root.mainloop()