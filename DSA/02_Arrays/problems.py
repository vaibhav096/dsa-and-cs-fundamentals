# ============================================================================
#                    ARRAY PROBLEMS - CODE SOLUTIONS
# ============================================================================

# ============================================================================
# PROBLEM 1: TWO SUM
# Given array and target, return indices of two numbers that add to target
# Time: O(n), Space: O(n)
# ============================================================================

def two_sum(nums, target):
    """
    Example: nums = [2,7,11,15], target = 9 → [0,1] (2+7=9)
    """
    seen = {}  # num -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print("Two Sum:", two_sum([2, 7, 11, 15], 9))


# ============================================================================
# PROBLEM 2: BEST TIME TO BUY AND SELL STOCK
# Find maximum profit from buying and selling once
# Time: O(n), Space: O(1)
# ============================================================================

def max_profit(prices):
    """
    Example: prices = [7,1,5,3,6,4] → 5 (buy at 1, sell at 6)
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

print("Max Profit:", max_profit([7, 1, 5, 3, 6, 4]))


# ============================================================================
# PROBLEM 3: MAXIMUM SUBARRAY (Kadane's Algorithm)
# Find contiguous subarray with largest sum
# Time: O(n), Space: O(1)
# ============================================================================

def max_subarray(nums):
    """
    Example: nums = [-2,1,-3,4,-1,2,1,-5,4] → 6 ([4,-1,2,1])
    """
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print("Max Subarray Sum:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# ============================================================================
# PROBLEM 4: CONTAINS DUPLICATE
# Check if array has any duplicate
# Time: O(n), Space: O(n)
# ============================================================================

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

print("Contains Duplicate:", contains_duplicate([1, 2, 3, 1]))


# ============================================================================
# PROBLEM 5: PRODUCT OF ARRAY EXCEPT SELF
# Return array where each element is product of all others
# Time: O(n), Space: O(1) excluding output
# ============================================================================

def product_except_self(nums):
    """
    Example: [1,2,3,4] → [24,12,8,6]
    """
    n = len(nums)
    result = [1] * n

    # Left pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right pass
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result

print("Product Except Self:", product_except_self([1, 2, 3, 4]))


# ============================================================================
# PROBLEM 6: MAXIMUM PRODUCT SUBARRAY
# Find contiguous subarray with largest product
# Time: O(n), Space: O(1)
# ============================================================================

def max_product(nums):
    """
    Example: [2,3,-2,4] → 6 ([2,3])
    """
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result

print("Max Product Subarray:", max_product([2, 3, -2, 4]))


# ============================================================================
# PROBLEM 7: FIND MINIMUM IN ROTATED SORTED ARRAY
# Time: O(log n), Space: O(1)
# ============================================================================

def find_min(nums):
    """
    Example: [3,4,5,1,2] → 1
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

print("Min in Rotated Array:", find_min([3, 4, 5, 1, 2]))


# ============================================================================
# PROBLEM 8: SEARCH IN ROTATED SORTED ARRAY
# Time: O(log n), Space: O(1)
# ============================================================================

def search_rotated(nums, target):
    """
    Example: nums = [4,5,6,7,0,1,2], target = 0 → 4
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print("Search Rotated:", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))


# ============================================================================
# PROBLEM 9: 3SUM
# Find all unique triplets that sum to zero
# Time: O(n²), Space: O(1)
# ============================================================================

def three_sum(nums):
    """
    Example: [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

print("3Sum:", three_sum([-1, 0, 1, 2, -1, -4]))


# ============================================================================
# PROBLEM 10: CONTAINER WITH MOST WATER
# Time: O(n), Space: O(1)
# ============================================================================

def max_area(height):
    """
    Example: [1,8,6,2,5,4,8,3,7] → 49
    """
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

print("Max Water Area:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))


# ============================================================================
# PROBLEM 11: MERGE INTERVALS
# Time: O(n log n), Space: O(n)
# ============================================================================

def merge_intervals(intervals):
    """
    Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged

print("Merged Intervals:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))


# ============================================================================
# PROBLEM 12: SORT COLORS (Dutch National Flag)
# Sort array of 0s, 1s, 2s in-place
# Time: O(n), Space: O(1)
# ============================================================================

def sort_colors(nums):
    """
    Example: [2,0,2,1,1,0] → [0,0,1,1,2,2]
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

print("Sort Colors:", sort_colors([2, 0, 2, 1, 1, 0]))


# ============================================================================
# PROBLEM 13: MAJORITY ELEMENT (Moore's Voting)
# Find element appearing more than n/2 times
# Time: O(n), Space: O(1)
# ============================================================================

def majority_element(nums):
    """
    Example: [2,2,1,1,1,2,2] → 2
    """
    candidate = nums[0]
    count = 1

    for num in nums[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print("Majority Element:", majority_element([2, 2, 1, 1, 1, 2, 2]))


# ============================================================================
# PROBLEM 14: MOVE ZEROES
# Move all zeros to end, maintain order of non-zero
# Time: O(n), Space: O(1)
# ============================================================================

def move_zeroes(nums):
    """
    Example: [0,1,0,3,12] → [1,3,12,0,0]
    """
    pos = 0  # Position to place next non-zero

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

    return nums

print("Move Zeroes:", move_zeroes([0, 1, 0, 3, 12]))


# ============================================================================
# PROBLEM 15: ROTATE ARRAY
# Rotate array right by k steps
# Time: O(n), Space: O(1)
# ============================================================================

def rotate_array(nums, k):
    """
    Example: nums = [1,2,3,4,5,6,7], k = 3 → [5,6,7,1,2,3,4]
    """
    n = len(nums)
    k = k % n  # Handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse entire array
    reverse(0, n - 1)
    # Reverse first k elements
    reverse(0, k - 1)
    # Reverse remaining elements
    reverse(k, n - 1)

    return nums

print("Rotate Array:", rotate_array([1, 2, 3, 4, 5, 6, 7], 3))


# ============================================================================
# PROBLEM 16: FIND DUPLICATE NUMBER
# Array of n+1 integers where each is in [1, n], one duplicate
# Time: O(n), Space: O(1) using Floyd's Algorithm
# ============================================================================

def find_duplicate(nums):
    """
    Example: [1,3,4,2,2] → 2
    """
    # Floyd's Tortoise and Hare
    slow = fast = nums[0]

    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

print("Find Duplicate:", find_duplicate([1, 3, 4, 2, 2]))


# ============================================================================
# PROBLEM 17: FIRST MISSING POSITIVE
# Find smallest missing positive integer
# Time: O(n), Space: O(1)
# ============================================================================

def first_missing_positive(nums):
    """
    Example: [3,4,-1,1] → 2
    """
    n = len(nums)

    # Place each number in its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_pos = nums[i] - 1
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]

    # Find first missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1

print("First Missing Positive:", first_missing_positive([3, 4, -1, 1]))


# ============================================================================
# PROBLEM 18: TRAPPING RAIN WATER
# Calculate water that can be trapped
# Time: O(n), Space: O(1)
# ============================================================================

def trap_water(height):
    """
    Example: [0,1,0,2,1,0,1,3,2,1,2,1] → 6
    """
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water

print("Trap Water:", trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# ============================================================================
# PROBLEM 19: SUBARRAY SUM EQUALS K
# Count subarrays with sum equal to k
# Time: O(n), Space: O(n)
# ============================================================================

def subarray_sum(nums, k):
    """
    Example: nums = [1,1,1], k = 2 → 2
    """
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}  # sum -> frequency

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count

print("Subarray Sum K:", subarray_sum([1, 1, 1], 2))


# ============================================================================
# PROBLEM 20: LONGEST CONSECUTIVE SEQUENCE
# Find length of longest consecutive elements sequence
# Time: O(n), Space: O(n)
# ============================================================================

def longest_consecutive(nums):
    """
    Example: [100,4,200,1,3,2] → 4 ([1,2,3,4])
    """
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from sequence start
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length

print("Longest Consecutive:", longest_consecutive([100, 4, 200, 1, 3, 2]))


print("\n=== All Array Problems Complete ===")
