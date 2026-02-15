# Given an array of integers nums and an integer target, return indices of
#  the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


#create a hashmap
#enumerate through the hashmap 
#calc diff -> target - value in nums
#if diff exists return indices
#if not store index values as the values of the hash



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       d = {}
    #using unpacking to store the key-value pairs from enumerating nums
    #i = iterable of nums, n = numbers in nums
       for i, n in enumerate(nums):
           diff = target - n
           #checks if the diff is within the dict d, bc dicts get checked
           #by keys, and in this case the key is the number from nums
           if diff in d:
               return [d[diff], i]
           else:
            #stores n as kes, and i as  values
            #backwards intuitively b/c we want to return the index
                d[n] = i 



c = Solution()
print("First Test:")
print(c.twoSum([2,7,11,15], 9))
print()
print("Second Test:")
print(c.twoSum([3, 2, 4], 6))
print()
print("Third Test:")
print(c.twoSum([3,3], 6))
print("   runtime approx: , Solved: fF    ")
