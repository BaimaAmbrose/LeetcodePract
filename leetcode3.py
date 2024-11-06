class Solution(object):
    def removeDuplicates(self, nums):
        m = 0
        n = 0
        for m in range(len(nums)):
            if nums[n] == nums[m]:
                m +=1
            else:
                nums[n+1] = nums[m]
                n += 1
                m +=1
        for i in range(n+1,len(nums)):
            del nums[n]
        return n+1
