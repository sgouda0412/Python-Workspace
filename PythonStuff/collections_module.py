# https://medium.com/towardsdev/collections-module-in-python-fbd50615af85

from collections import (
    defaultdict,
    deque,
    Counter,
    ChainMap,
    UserDict,
    UserList,
    UserString,
    OrderedDict,
)

# Counting characters in a string
char_count = Counter("hello world")

print(char_count)

# Output:
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Create a Counter object
word_counts = Counter("mississippi")

# Elements
print(list(word_counts.elements()))

# Most common elements
print(word_counts.most_common(2))

# Subtract counts
word_counts.subtract("miss")
print(word_counts)

# ['m', 'i', 'i', 's', 's', 's', 's', 'p', 'p', 'i', 'i']
# [('s', 4), ('i', 4)]
# Counter({'i': 2, 'p': 2, 's': 2, 'm': 0})


# Using an integer as the default value
int_default_dict = defaultdict(int)
int_default_dict["a"] += 1
int_default_dict["b"] += 2

print(int_default_dict)


# Grouping items by their first letter
words = ["apple", "banana", "cherry", "date", "eggplant", "fig"]
grouped_words = defaultdict(list)

for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)

print(grouped_words)


# counting elements

# from collections import defaultdict

# Counting occurrences of each character in a string
char_count = defaultdict(int)
for char in "hello world":
    char_count[char] += 1

print(char_count)


# if __name__ == "__main__":
#     pass
# 34.54.231.80
