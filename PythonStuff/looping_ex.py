list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in list_of_lists:
    for item in sublist:
        print(item)


my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

new_list = [item * 2 for item in my_list]

for index, item in enumerate(my_list):
    print(index, item)


def square(x):
    return x * x


squared_list = list(map(square, my_list))
