def bin_search(arr, t):
    if len(arr) == 0:
        return -1
    l, r = 0, len(arr)
    while l <= r:
        m = (l + r - 1) // 2
        if arr[m] == t:
            return m
        elif arr[m] < t:
            l = m + 1
        else:
            r = m - 1
        
        
    if arr[m] != t:
        return -1
    else:
        return m
