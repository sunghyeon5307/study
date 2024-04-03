def a(list):
    if not list:
        return 0
    return list.pop(0) + a(list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = a(list)
print(result)