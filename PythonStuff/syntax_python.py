#https://www.youtube.com/watch?v=PNSIWjWAA7o
#https://www.youtube.com/watch?v=0K_eZGS5NsU

#https://www.youtube.com/watch?v=VchuKL44s6E&t=14s

#https://rs-punia.medium.com/21-most-frequently-used-built-in-functions-in-python-a-beginners-guide-2224a6cda953

l = [1, 2, 4, 3, 6, 5]
#x = l.sort()
#r = l.reverse()
#s = list(reversed(l))
t = sorted(l, reverse=True)
# print(l)
# print(x)
#print(r)
# print(s)
print(t)
print(l)

#sorted and reversed doesnot change the orginal list
from collections import defaultdict, deque, Counter
import bisect

# word_count = defaultdict(int)

# for word in doc.split():
#     word_count[word] += 1


text = "Even if you decided to use a particular default value for defaultdict, you can replace the value or \
keys at any point of time and you MUST never do that. There is nothing wrong \
in it syntactically, but this is not the reason for using defaultdict, and you must use other constructs for writing your code"

counts = {}

for word in text.split():
    counts.setdefault(word, 0)
    counts[word] += 1
print(counts)

name = "IndianPythonista"

d = defaultdict(int)
for c in name:
    d[c] += 1

print(d)
