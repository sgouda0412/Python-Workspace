def bubblesort(list):
    for i in range(len(list) - 1, 0, -1):
        for x in range(i):
            if list[x] > list[x + 1]:
                temp = list[x]
                list[x] = list[x + 1]
                list[x + 1] = temp
    return list

lst = [5, 6, 2, 3, 8, 7, 1, 4, 9]
print(bubblesort(lst))
