from typing import List

lst = [0,1,-1,3,5,7,13]


def number_finder(nums:List[int],target):
    try:
        return nums.index(target)
    except ValueError:
        nums.append(target)
        return sorted(nums).index(target)

print(number_finder(lst,11))
