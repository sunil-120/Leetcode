class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = len(nums)-1
        length = len(nums)
        duplicates = 0
        while (right != left):
            if nums[left] == nums[left+1]:
                nums.pop(left)
                nums.append("_")
                duplicates+=1
                right-=1
            else:
                if left!=right:
                    left+=1

            if nums[right] == nums[right-1]:
                nums.pop(right-1)
                nums.append("_")
                duplicates+=1
            else:
                if left!=right:
                    right-=1
        return len(nums) - duplicates 

        