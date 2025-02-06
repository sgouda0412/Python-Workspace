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
