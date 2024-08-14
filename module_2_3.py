
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list) - 1:
    y = my_list[x]
    x += 1
    if y > 0:
        print(y)
    elif y == 0:
        continue
    else:
        break
