my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list = iter(my_list)

while (s := next(my_list)) >= 0:
    if s == 0:
        continue
    else:
        print(s)
