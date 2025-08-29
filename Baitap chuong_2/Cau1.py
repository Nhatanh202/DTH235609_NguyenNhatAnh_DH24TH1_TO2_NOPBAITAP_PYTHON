import math
try :
    r = float(input("Nhap ban kinh hinh tron: "))
    cv = 2 * math.pi * r
    dt = r ** 2
    print("Chu vi = ", cv)
    print("Dien tich = ", dt)
except :
    print("Lỗi rồi!")