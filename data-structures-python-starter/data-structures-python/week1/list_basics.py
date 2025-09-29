"""
Day 1 — Python List (Dynamic Array)
Practice: append, insert, pop/remove, slicing, iteration.
Big-O: index O(1), append amortized O(1), insert/delete O(n).
"""
def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None