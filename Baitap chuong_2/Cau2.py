t = int (input("Nhap so giay: "))
hour = (t//3600)%24
minute = (t%3600)//60
second = (t%3600)%60
print (hour, "gio", minute, "phut", second, "giay")