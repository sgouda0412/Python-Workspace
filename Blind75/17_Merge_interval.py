from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x : x[0])

    ans = [intervals[0]]

    for first, second in intervals[1:]:
        last_of_second = ans[-1][1]   #3 #[[1,3],[2,6],[8,10],[15,18]]

        if first <= last_of_second:   #2 <= 3
            ans[-1][1] = max(last_of_second, second) # max(3, 6)
        else:
            ans.append([first, second]) #[8, 10] [15, 18]
    return ans


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))