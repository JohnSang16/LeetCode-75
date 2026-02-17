class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        pivot = 0
        leftsum = 0 
        rightsum = 0
        for i in range(len(nums)):
            pivot = i
            while pivot < len(nums)-1:
                pivot += 1
                rightsum += nums[pivot] 
            
            if i == 0: 
                pass
            else:
                leftsum += nums[i-1]
            
            pivot = i
            if leftsum == rightsum:
                return pivot
            rightsum = 0
        return -1
    
c = Solution()
test1 = c.pivotIndex([1,7,3,6,5,6])
print(test1)