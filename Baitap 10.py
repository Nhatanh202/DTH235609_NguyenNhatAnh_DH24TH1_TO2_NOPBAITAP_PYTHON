sao = [1, 3, 5, 3, 5, 7, 2, 2]
for i in sao:
    if i == 2:
        print(' ' * (max(sao) - i) + '*  ' * i)
    else:
        print(' ' * (max(sao) - i) + '* ' * i)