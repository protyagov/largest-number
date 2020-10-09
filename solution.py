# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#   Input: nums = [3,30,34,5,9]
#   Output: "9534330"
# ALGO:
# Sort array highest to lowest and join into string. Key is to write compare function.
# Easy: Just join a+b and b+a and find largest:
#       return int(self.value + other.value) < int(other.value + self.value)
# FUN:  When strings start with equal numbers, ex: [3432312, 3432], then we compare as
#       [3432312, 3432] -> [312, 3432] -> [12, 432] -> second number should go first.
#       Function can be done recursively each time remove start common part from largest string

from typing import List


class ArrayElem:
    def __init__(self, val: int):
        self.value = str(val)

    def __repr__(self):
        return self.value

    def __lt__(self, other):
        return self.is_string_a_gt_b(other.value, self.value)

    @staticmethod
    def is_string_a_gt_b(a: str, b: str) -> bool:
        if len(a) == len(b):
            return a > b

        min_l = min(len(a), len(b))
        for i in range(0, min_l):
            if a[i] != b[i]:
                return a[i] > b[i]

        if min_l == len(a):
            return ArrayElem.is_string_a_gt_b(a, b[min_l:])
        else:
            return ArrayElem.is_string_a_gt_b(a[min_l:], b)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = [ArrayElem(x) for x in nums]
        res.sort(reverse=True)
        while res and res[0].value == "0":
            res.pop(0)
        return "".join([x.value for x in res]) if res else "0"


assert "0" == Solution().largestNumber([0, 0])
assert "210" == Solution().largestNumber([10, 2])
assert "9534330" == Solution().largestNumber([3, 30, 34, 5, 9])
assert "1" == Solution().largestNumber([1])
assert "10" == Solution().largestNumber([10])
assert "34323432312" == Solution().largestNumber([3432312, 3432])
assert "9876543210" == Solution().largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
