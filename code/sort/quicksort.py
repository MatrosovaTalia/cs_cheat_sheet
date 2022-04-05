import random

def quicksort(nums, l, r):
    if l < r:
        p = partition(nums, l, r)

        quicksort(nums, l, p - 1)
        quicksort(nums, p + 1, r)
    return nums

def partition(nums, l, r):
    p_idx = choose_pivot(l, r)
    pivot = nums[p_idx]
    i = l
    j = r

    for j in range(l, r):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i] 
            i += 1
    return p_idx    



def choose_pivot(left, right):
    i1 = random.randint(0, right - left)
    i2 = random.randint(0, right - left)
    i3 = random.randint(0, right - left)

    return min(max(i1, i2), max(i2, i3))


print(quicksort([10, 7, 8, 9, 1, 5] , 0, 6))

