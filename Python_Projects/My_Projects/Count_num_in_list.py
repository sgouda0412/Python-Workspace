def count(lst, x):
    """
    Iterates through a list, if a number is equal to the number that is
    checked, the count increases
    """
    count = 0
    for num in lst:
        if (num == x):
            count += 1
    return count

num_lst = []

while len(num_lst) < 10:
    numbers = int(input("Please enter a number to add to the list: "))
    num_lst.append(numbers)

x = int(input("Please enter a number to count: "))

print(f"{x} has occured {count(num_lst, x)} times")
