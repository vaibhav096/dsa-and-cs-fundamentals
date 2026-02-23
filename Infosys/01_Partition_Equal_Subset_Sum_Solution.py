
def can_partition(arr):
    """
    Function to check if array can be partitioned into two subsets of equal sum.
    """
    total_sum = sum(arr)
    
    # If total sum is odd, it's impossible to divide into two equal integer parts
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(arr)
    
    # dp[j] will be True if sum 'j' is achievable
    dp = [False] * (target + 1)
    dp[0] = True  # Sum 0 is always achievable (empty subset)
    
    # Iterate through each number in the array
    for num in arr:
        # Iterate backwards to avoid using the same element multiple times
        # for numbers greater than or equal to the current number
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                
        # Optimization: If target is already reached, we can stop early
        if dp[target]:
            return True
            
    return dp[target]

# ---------------------------------------------------
# Driver Code to test the solution
# ---------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 11, 5], True),
        ([1, 3, 5], False),
        ([2, 2, 2, 2, 4], True),  # Split: [2,2,2] and [2,4] -> 6,6
        ([100], False)
    ]
    
    print(f"{'TestCase':<30} | {'Expected':<10} | {'Result':<10} | {'Status'}")
    print("-" * 65)
    
    for arr, expected in test_cases:
        result = can_partition(arr)
        status = "PASSED" if result == expected else "FAILED"
        print(f"{str(arr):<30} | {str(expected):<10} | {str(result):<10} | {status}")

