from typing import List
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ans = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            ans.append(newInterval)
            return ans + intervals[i:]

        elif newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
        
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    ans.append(newInterval)

    return ans
            


if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(insert(intervals, newInterval))