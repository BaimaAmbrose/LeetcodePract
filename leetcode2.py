def removeElement(nums,val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    for i in range(k,len(nums)):
        nums[i] = 0
    return k

nums=[1,2,4,3,6,3,2,2,5]
val = 2
k = removeElement(nums,val)
print(k)
print(nums)
