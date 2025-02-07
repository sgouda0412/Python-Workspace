#!/usr/bin/env python3
# -*- coding: cp1252 -*-


from collections import deque, defaultdict, Counter

d = deque([1, 2, 3, 4, 5], maxlen= 10)

for ele in d:
    print(ele)

d.append(6)
d.appendleft(0)
d.pop()
d.popleft()

d.reverse()
print(d)
for i in d:
    print(i, end= ' ')
print()

d.remove(2)
d.rotate(2)
c = d.copy()
print(c)
x = d.index(3)
print(x)
print(list(d))
d.clear()
print(d)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d  = defaultdict(list)

for k, v in s:
    d[k].append(v)
print(sorted(d.items()))


d = {}

for k, v in s:
    d.setdefault(k, []).append(v)
print(sorted(d.items()))

s = 'mississippi'
d = defaultdict(int)

for k in s:
    d[k] += 1
print(sorted(d.items()))


c = Counter("santosh")
print(c)

c = Counter({'red': 4, 'blue': 2})
print(c)

c = Counter(cats=4, dogs=8)
print(c)

c = Counter(['eggs', 'ham'])
print(c)
del c['eggs']
print(c['bacon'])

print(c)

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))

c = Counter('abracadabra').most_common(3)
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

c = Counter(a=10, b=5, c=0)
print(c.total())

d = dict.fromkeys(['a', 'b', 'c'], 0)
print(d)

c = Counter({'a': 2, 'b': 3})
c.update({'a': 5, 'b': 7})
print(c)

vec = [[1,2,3], [4,5,6], [7,8,9]]
r = []
for x in vec:
    for j in x:
        r.append(j)
print(r)

r = [j for x in vec for j in x]
print(r)

import heapq

a = [52, 94, 13, 77, 41]
heapq.heapify(a)

print(a)

heapq.heappush(a, 19)
print(a)

heapq.heappushpop(a, 14)
print(a)

x = heapq.nlargest(3, a)
print(x)

words = ["apple", "banana", "cherry", "date"]
longest_words = heapq.nlargest(2, words, key=len)
print(longest_words)

a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a + b
print()
users = {'Hans': 'active', 'Sams':'inactive', 'Cats': 'active'}

active_users = {}
for k, v in users.items():
    if v == 'active':
        active_users[k] = v
print(active_users)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break
print("All you going to executed......")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
try:
    color =  Color(input("Enter the choice of color: "))
    match color:
        case Color.RED:
            print("i see red")
        case Color.GREEN:
            print("i see green")
        case Color.BLUE:
            print("i see blue")
        case _:
            print("i see no color")
except ValueError:
    print("Invalid color choice...")

args = [3, 6]
print(list(range(*args)))

import os
import sys

a = [1, 2, 3, 4, 5, 6, 7, 8]
del a[0]
print(a)

del a[2:5]
print(a)


v = ([1,2, 3],[3, 2, 1])
#v[0] = [1, 2]
print(v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}. it is {1}.'.format(q,a))

for i in reversed(range(1, 10, 2)):  # sequence should be in forward direction
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket): # Sorted Squence Order
    print(i)


