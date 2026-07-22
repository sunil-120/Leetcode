class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closet = nums[0] +nums[1] +nums[2]
        n=len(nums)
        for i in range(n-2):

            left = i+1
            right = n-1

            while(left<right):

                sum=nums[i]+nums[left]+nums[right]

                if (abs(sum-target)<abs(closet-target)):
                    closet = sum


                if sum>target:
                    right-=1
                elif sum<target:
                    left+=1
                else:
                    return sum
        return closet


        