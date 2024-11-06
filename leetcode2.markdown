Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return *the number of elements in* `nums` *which are not equal to* `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

```python
def remove(nums1 , val1):
    for i in range(len(nums1)-1):
        if nums1[i] == val1:
            nums1[i] = 0
    for i in range(len(nums1)):
        if nums1[i] == 0:
            for j in range(i,len(nums1)-1):
                nums1[j]= nums1[j+1]
                
```

将所有等于val1的数字换成0之后，不知道如何将这些0全部换到后面去
