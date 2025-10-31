# Lab Problem 2: Largest Divisible Set
# Objective: Implement a dynamic programming solution to find the largest subset where every pair satisfies divisibility.
# Problem Statement:
# Given a set of distinct positive integers, find the largest subset such that for every pair (x, y) in the subset, either x % y == 0 or y % x == 0. Return the subset in any order.
# Inputs: nums = [1, 2, 4, 8, 16]
def largestDivisibleSubset(nums):
    if not nums:
        return []
    
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    
    dp = [1] * n       # dp[i] = length of largest subset ending at i
    prev = [-1] * n    # prev[i] = index of previous element in subset
    
    max_len = 1
    max_index = 0

    # Step 2: Build DP table
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i

    # Step 3: Reconstruct subset
    subset = []
    while max_index != -1:
        subset.append(nums[max_index])
        max_index = prev[max_index]
    
    subset.reverse()
    return subset


# -----------------------------
# Example Usage
# -----------------------------
nums = [1, 2, 4, 8, 16]
result = largestDivisibleSubset(nums)
print("Largest Divisible Subset:", result)
