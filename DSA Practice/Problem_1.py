'''
Leetcode 3010. Divide an Array Into Subarrays With Minimum Cost I

'''

''' My Solution'''

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # we just needs to find the two smallest numbers from the remaining
        ans=nums[0]
        nums2=sorted(nums[1:])
        return ans+nums2[0]+nums2[1]

        
# ═══════════════════════════════════════════════════════════════════════════
# CLAUDE'S ANALYSIS & SOLUTION
# ═══════════════════════════════════════════════════════════════════════════

'''
PROBLEM UNDERSTANDING:
- Given array nums of length n
- Cost of an array = its FIRST element
- Divide into 3 contiguous subarrays
- Return MINIMUM sum of costs

KEY INSIGHT:
- First subarray MUST start at index 0 → nums[0] is ALWAYS included
- We pick 2 more "starting points" from indices 1 to n-1
- To minimize → pick 2 SMALLEST values from nums[1:]
- Contiguity is auto-satisfied (any 2 indices define valid splits)
'''

# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS OF YOUR SOLUTION
# ═══════════════════════════════════════════════════════════════════════════

'''
YOUR APPROACH:
✓ Correctly identified nums[0] is always included
✓ Correctly sorts remaining to find 2 smallest
✓ Logic is 100% CORRECT!

COMPLEXITY:
- Time:  O(n log n)  ← due to sorting
- Space: O(n)        ← nums2 creates a copy

VERDICT: Correct! But can be optimized to O(n).
'''

# ═══════════════════════════════════════════════════════════════════════════
# OPTIMIZED SOLUTION - O(n) Single Pass
# ═══════════════════════════════════════════════════════════════════════════

from typing import List

class SolutionOptimized:
    def minimumCost(self, nums: List[int]) -> int:
        '''
        Instead of sorting, find 2 smallest in ONE PASS.
        '''
        min1 = float('inf')  # smallest
        min2 = float('inf')  # second smallest

        for i in range(1, len(nums)):  # Start from index 1
            if nums[i] < min1:
                min2 = min1      # old smallest → second smallest
                min1 = nums[i]   # new smallest
            elif nums[i] < min2:
                min2 = nums[i]   # new second smallest

        return nums[0] + min1 + min2


# ═══════════════════════════════════════════════════════════════════════════
# DRY RUN
# ═══════════════════════════════════════════════════════════════════════════

'''
nums = [1, 2, 3, 12]

i=1, nums[1]=2: 2 < inf → min1=2, min2=inf
i=2, nums[2]=3: 3 < inf → min2=3
i=3, nums[3]=12: no change

Result: 1 + 2 + 3 = 6 ✓
'''

# ═══════════════════════════════════════════════════════════════════════════
# COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════

'''
┌─────────────────┬──────────────┬──────────────┐
│ Approach        │ Time         │ Space        │
├─────────────────┼──────────────┼──────────────┤
│ Your Solution   │ O(n log n)   │ O(n)         │
│ Optimized       │ O(n)         │ O(1)         │
└─────────────────┴──────────────┴──────────────┘
'''

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN: Find 2 Smallest Without Sorting
# ═══════════════════════════════════════════════════════════════════════════

'''
if num < min1:
    min2 = min1      # Shift down
    min1 = num       # New smallest
elif num < min2:
    min2 = num       # New second smallest

Use this pattern whenever you need K smallest in O(n)!
'''

# ═══════════════════════════════════════════════════════════════════════════
# TEST
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 12], 6),
        ([5, 4, 3], 12),
        ([10, 3, 1, 1], 12),
    ]

    sol = SolutionOptimized()
    for nums, expected in test_cases:
        result = sol.minimumCost(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums} → {result} (expected {expected})")