def merge_sort(nums):
    if len(nums) > 1:
        m = len(nums) // 2 + len(nums) % 2
        left = nums[:m]
        right = nums[m:]

        merge_sort(left)
        merge_sort(right)

        i, j = 0, 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    
    return nums

print(merge_sort([2, 8 , 33, 64, 3, 6, 99, 111, 56]))



