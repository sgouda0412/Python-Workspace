# https://medium.com/gitconnected/python-lists-the-ultimate-guide-496779c4b3fb

x = [1, 2, 3, 4, 5, 6]
for i in reversed(x):
    print(i)

# [] is faster than list()
empty_list = []
weekdays = ["Monday", "Tuesday"]

empty_list = list()

list("cat")  # split into character

oceans = ("artics", "atlantics")

list(oceans)


today_date = "08/06/2022"
today_date.split("/")
# ['08','06','2022']

oceans = ["arctic", "atlantic", "pacific", "indian", "antarctic"]
oceans[1]
# 'atlantic'

oceans[-1]
# 'antarctic

oceans[0:2]
# ['arctic', 'atlantic']

oceans[0::2]
# ['arctic', 'pacific', 'antarctic']

oceans.reverse()

oceans[::-1]

oceans.append("arctic")
# ['antarctic', 'indian', 'pacific', 'atlantic', 'arctic']

oceans.insert(2, "arctic")
# ['antarctic', 'indian', 'arctic', 'pacific', 'atlantic']

["alright"] * 3
# ["alright", "alright", "alright"]

brics = ["brazil", "russia", "india"]
others = ["china", "south africa"]
brics.extend(others)
# ['brazil', 'russia', 'india', 'china', 'south africa']

brics += others
# ['brazil', 'russia', 'india', 'china', 'south africa']

brics.append(others)
# ['brazil', 'russia', 'india', ['china', 'south africa']]


colors = ["red", "blue", "green"]
colors[1] = "yellow"
# ['red', 'yellow', 'green']


numbers = [1, 2, 3, 5]
numbers[1:3] = [8, 9]
# [1, 8, 9, 5]

numbers[1:3] = (98, 99, 100)
# [1, 98, 99, 100, 5]

numbers[1:3] = "wat?"
# [1, 'w', 'a', 't', '?', 5]


numbers = [1, 2, 3, 5]
del numbers[2]
# [1, 2, 5]

numbers.remove(2)
# [1, 3, 5] #remove the first occurence of the value

oceans.pop()
# 'antarctic'
# ['arctic', 'pacific', 'indian']

oceans.pop(1)  # remove and return the value
# 'pacific'
# ['arctic', 'indian']


oceans.clear()
# []

oceans.index("indian")
# 2

"pacific" in oceans
# True

Simpsons = ["Abe", "Bart", "Homer", "Bart"]
Simpsons.count("Bart")
# 2

",".join(oceans)
# 'arctic, pacific, indian, atlantic'


oceans.sort()  # in place
# ['arctic', 'atlantic', 'indian', 'pacific']

sorted_oceans = sorted(oceans)  # new sorted list
# ['arctic', 'atlantic', 'indian', 'pacific']


oceans.sort(reverse=True)
# ['pacific', 'indian', 'atlantic', 'arctic']


len(oceans)
# 4

a = [1, 2, 3]  # copy by reference not value
b = a
a[1] = "two"
# a = [1, 'two', 3]
# b = [1, 'two', 3]

a = [1, 2, 3]
b = a.copy()
a[1] = "two"
# b = [1, 2, 3]

c = list(a)
# c = [1, 2, 3]

d = a[:]
# d = [1, 2, 3

import copy  # copy everything

a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
a[2][1] = 10
# a = [1, 2, [8, 10]]
# b = [1, 2, [8, 9]]

a = [7, 2]
b = [7, 2, 9]
a == b
# False

a <= b
# True


oceans = ["arctic", "antarctic", "atlantic", "indian", "pacific"]
for ocean in oceans:
    print(ocean)


oceans.count("arctic")

days = ["Monday", "Tuesday", "Wednesday"]
fruits = ["banana", "orange", "peach"]
drinks = ["coffee", "tea", "cola"]
desserts = ["tiramisu", "ice cream", "pie", "pudding"]

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(f"{day}: drink {drink}, eat {fruit}, enjoy {dessert}")


a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
# [1, 3, 5]

a_list = [number for number in range(1, 6) if number % 2 == 1]
# [1, 3, 5]

items = [1, 2, 2, 3, 4, 4, 5]  # remove duplicate elements from the list
unique_items = list(dict.fromkeys(items))
# [1, 2, 3, 4, 5]

unique_items = list(set(items))
# Note: This will not maintain the original order


data = [1, 2, 3]
a, b, c = data
# a = 1, b = 2, c = 3

# Using * to unpack remaining elements
first, *rest = data
# first = 1, rest = [2, 3]


for index, value in enumerate(oceans):
    print(f"Index: {index}, Value: {value}")


ids = [1, 2, 3]
names = ["Alice", "Bob", "Cathy"]
grades = ["A", "B", "A+"]

students = list(zip(ids, names, grades))
print(students)  # Output: [(1, 'Alice', 'A'), (2, 'Bob', 'B'), (3, 'Cathy', 'A+')]


zipped = zip(ids, names, grades)
unzipped = list(zip(*zipped))
print(unzipped)
