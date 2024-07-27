from typing import Dict

from collections import defaultdict

my_dict = defaultdict(int)

my_dict: dict = {"banana": 3, "apple": 2, "cherry": 5}

# print(my_dict["gauva"])
print(my_dict.get("gauva", 0))


def sort_my_dict_by_key_and_value(my_dict):
    sort_by_key = dict(sorted(my_dict.items()))
    sort_by_value = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    return sort_by_key, sort_by_value


def returnSum(dict):
    return sum(dict.values())


def get_size_of_dic(dic1):
    import sys

    return sys.getsizeof(dic1)


def Merge(d1, d2):
    return {**d1, **d2}


def mean_values(test_dict):
    import statistics

    return statistics.mean(list(test_dict.values()))


def find_dup_char(input):
    return " ".join(set(filter(lambda x: input.count(x) >= 2, input)))


def maximum_unique_values(test_dict1):
    unique_counts = [(key, len(set(values))) for key, values in test_dict1.items()]
    return max(unique_counts, key=lambda x: x[0])[0]


if __name__ == "__main__":
    my_dict: dict[str, int] = {"banana": 3, "apple": 2, "cherry": 5}
    dict_sum = {"a": 100, "b": 200, "c": 300}
    dic1 = {"A": 1, "B": 2, "C": 3}
    dict1 = {"a": 10, "b": 8}
    dict2 = {"d": 6, "c": 4}
    test_dict = {"Gfg": 4, "is": 7, "Best": 8, "for": 6, "Geeks": 10}
    input = "geeksforgeeks"
    test_dict1 = {
        "Gfg": [5, 7, 5, 4, 5],
        "is": [6, 7, 4, 3, 3],
        "Best": [9, 9, 6, 5, 5],
    }

    print(find_dup_char(input))
    print(Merge(dict1, dict2))
    print(sort_my_dict_by_key_and_value(my_dict))
    print(f"Sum: {returnSum(dict_sum)}")
    print(f"size of dic1 is:{get_size_of_dic(dic1)} bytes")
    print(f"The computed mean is: {mean_values(test_dict)}")
    print(maximum_unique_values(test_dict1))
