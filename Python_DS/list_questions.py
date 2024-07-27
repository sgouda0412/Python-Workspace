from typing import List


def interchange_first_and_last_elements(l):
    l[0], l[-1] = l[-1], l[0]
    return l


def swap_positions(l, pos1, pos2):
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l


def swap_character(test_list):
    x = [sub.replace("G", "-").replace("e", "G").replace("-", "e") for sub in test_list]
    return x


def length_of_list(l):
    # return len(l)
    count = 0
    for i in l:
        count += 1
    return count


def max_of_2_number(a, b):
    # return a if a >= b else b
    return max(a, b)


def min_of_2_number(a, b):
    return a if a <= b else b


def is_item_exist(l, item):
    return True if item in l else False


def clear_a_list(l):
    while len(l) != 0:
        l.pop()
    return l
    # x = l.clear()
    # return x


def reverse_a_list(lst):
    nl = lst[::-1]
    return nl


def list_reverse(lst):
    i = 0
    while i < len(lst) // 2:
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
        i += 1
    return lst


def list_cloning(lst):
    # li_copy = lst[:]
    # return li_copy
    li_copy = []
    li_copy.extend(lst)
    return li_copy


def count_all_occurrences(lst, x):
    # c = lst.count(x)
    # return c
    c = 0
    for ele in lst:
        if ele == x:
            c += 1
    return c


from typing import List, TypedDict


def sum_and_average(lst):
    # s = sum(lst)
    # a = s // len(lst)
    # return s, a
    s = 0
    for ele in lst:
        s += ele
        a = s // len(lst)
    return s, a


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def list_of_digit_sum(nums):
    return list(map(digit_sum, nums))


from math import prod


def multiply_all_numbers_in_list(nums):
    # s = 1
    # for i in nums:
    #     s *= i
    # return s

    return prod(nums)


def smallest_number_in_a_list(nums):
    return min(nums)


def largest_number_in_a_list(nums):
    return max(nums)


def find_second_largest(nums):
    m = max(nums)
    return max([i for i in nums if i < m])


def find_second_smallest(nums):
    m = min(nums)
    return min([i for i in nums if i > m])


def print_even_number_in_a_list(nums):
    return [i for i in nums if i % 2 == 0]


def print_odd_number_in_a_list(nums):
    return [i for i in nums if i % 2 != 0]


def print_even_number_in_a_range():
    return [i for i in range(10, 50) if i % 2 == 0]


def print_odd_number_in_a_range():
    return [i for i in range(10, 50) if i % 2 != 0]


def evenoddcount(nums):
    ecount = len(list(filter(lambda x: x % 2 == 0, nums)))
    ocount = len(list(filter(lambda x: x % 2 != 0, nums)))

    return [ecount, ocount]


def positive_number_of_a_list(arr):
    return list(filter(lambda x: x > 0, arr))


def negative_number_of_a_list(arr):
    return list(filter(lambda x: x < 0, arr))


def count_pos_and_neg(arr):
    cpos = 0
    cneg = 0
    for i in arr:
        if i > 0:
            cpos += 1
        else:
            cneg += 1
    return [cpos, cneg]


def remove_empty_tuples(tuples):
    return [t for t in tuples if t]


def duplicate(input_list):
    return list(set(i for i in input_list if input_list.count(i) > 1))


def convert_to_tuple(in_list):
    return tuple(in_list)


def convert_list_to_str(s):
    return " ".join([str(ele) for ele in s])


def convert_str_to_int(test_list):
    return [int(ele) for ele in test_list]


def deduplicate(my_list):
    seen = set()
    return [i for i in my_list if i not in seen and not seen.add(i)]


def merge_two_list(l1, l2):
    l1.extend(l2)
    return l1


def initialize_empty_array_of_given_length():
    # x = [0] * 10
    # return x
    # return [0 for x in range(10)]
    return [[0] * 4 for i in range(3)]


def createList(r1, r2):
    return [item for item in range(r1, r2 + 1)]


def append_at_the_beg(l1):
    from collections import deque

    l2 = deque(l1)
    l2.appendleft(6)
    return list(l2)


def most_frequent_element_in_a_list(li):
    return max(set(li), key=lambda x: li.count(x))


def conversion_of_number_to_list_of_integers(n):
    res = []
    while n > 0:
        n, remainder = divmod(n, 10)
        res.insert(0, remainder)
    return res


def is_list_empty(k):
    if k:
        return "Non empty"
    else:
        return "empty"


def check_text_present(p, text):
    import operator

    if operator.contains(p, text):
        return "Text Contains"
    else:
        return "Text does not contains"


if __name__ == "__main__":
    lst: List[int] = [2, 4, 1, 6, 7, 8, 3, 5, 9, 7]
    l: List[int] = [2, 4, 1, 6, 7, 8, 3, 5, 9]
    nums = [12, 43, 87, 45, 23]
    mul = [1, 2, 3]
    arr = [-1, 3, 4, -6, 7, -8]
    tuples = [
        (),
        ("ram", "15", "8"),
        (),
        ("laxman", "sita"),
        ("krishna", "akbar", "45"),
        ("", ""),
        (),
    ]
    test_list = ["Gfg", "is", "best", "for", "Geeks"]
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    s = ["I", "want", 4, "apples", "and", 18, "bananas"]
    test_list = ["1", "4", "3", "6", "7"]
    my_list = [1, 2, 3, 2, 4, 3, 5]
    l1 = [1, 3, 4, 5]
    l2 = [9, 7, 5, 4]
    z = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    pos1 = 2
    pos2 = 6
    n = 1234
    r1 = 5
    r2 = 20
    a = 2
    b = 4
    item = 10
    x = 7
    k = []
    p = [1, 2.0, "have", "a", "geeky", "day"]
    # assign string
    text = "geeky"
    print(interchange_first_and_last_elements(l))
    print(swap_positions(l, pos1, pos2))
    print(swap_character(test_list))
    print(length_of_list(l))
    print(max_of_2_number(a, b))
    print(min_of_2_number(a, b))
    print(is_item_exist(l, item))
    print(clear_a_list(l))
    print(reverse_a_list(lst))
    print(list_reverse(lst))
    print(list_cloning(lst))
    print(count_all_occurrences(lst, x))
    print(sum_and_average(lst))
    print(list_of_digit_sum(nums))
    print(multiply_all_numbers_in_list(mul))
    print(smallest_number_in_a_list(nums))
    print(largest_number_in_a_list(nums))
    print(find_second_largest(nums))
    print(find_second_smallest(nums))
    print(print_even_number_in_a_list(nums))
    print(print_odd_number_in_a_list(nums))
    print(print_even_number_in_a_range())
    print(print_odd_number_in_a_range())
    print(evenoddcount(nums))
    print(positive_number_of_a_list(arr))
    print(negative_number_of_a_list(arr))
    print(count_pos_and_neg(arr))
    print(remove_empty_tuples(tuples))
    print(duplicate(input_list))
    print(convert_to_tuple(input_list))
    print(convert_list_to_str(s))
    print(convert_str_to_int(test_list))
    print(deduplicate(my_list))
    print(merge_two_list(l1, l2))
    print(initialize_empty_array_of_given_length())
    print(createList(r1, r2))
    print(append_at_the_beg(l1))
    print(most_frequent_element_in_a_list(z))
    print(conversion_of_number_to_list_of_integers(n))
    print(is_list_empty(k))
    print(check_text_present(p, text))
