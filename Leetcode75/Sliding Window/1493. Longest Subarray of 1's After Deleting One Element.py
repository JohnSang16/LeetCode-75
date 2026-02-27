# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        s = 0
        e = 0
        max_ones = 0
        k = 1

        while e < len(nums):
            if nums[e] == 0:
                k -=1

            while k < 0:
                if nums[s] == 0:
                    k += 1
                s += 1

            max_ones = max(max_ones, e - s + 1)
            e += 1
        return max_ones - 1
    
    
    
c = Solution()
test1 = c.longestSubarray([1,1,0,1])
test2 = c.longestSubarray([0,1,1,1,0,1,1,0,1])
test3 = c.longestSubarray([1,1,1])
print(test1)

print("---------------Test Cases:---------------")
print(f"test1 output:{test1}, expected output: 3")
print(f"test2 output:{test2}, expected output: 5")
print(f"test3 output:{test3}, expected output: 2")
print("   runtime approx: 67ms, Solved: T     ")