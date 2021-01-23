# Merge Sort
def merge_sort(arr):
    MAX_DATA = 10
    temp = [0] * MAX_DATA

    def _merge_sort(arr, l, r):
        nonlocal temp

        if l >= r:
            return
 
        mid = (l + r) // 2
        _merge_sort(arr, l, mid)
        _merge_sort(arr, mid + 1, r)

        for i in range(l, mid + 1):
            temp[i] = arr[i]

        i = mid + 1
        j = r
        for i in range(mid + 1, r + 1):
            temp[i] = arr[j]
            j = j - 1

        i = l
        j = r
        for k in range(l, r + 1):
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i = i + 1
            else:
                arr[k] = temp[j]
                j = j - 1

        return
    return _merge_sort(arr, 0, MAX_DATA - 1)

# Bubble Sort
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            else:
                continue

# Quick Sort
def quick_sort(l):
    if l == []:
        return l
    else:
        pivot = l[len(l) // 2]
        y = quick_sort([i for i in l if i < pivot])
        p = [i for i in l if i == pivot]
        n = quick_sort([i for i in l if i > pivot])
        y += p
        y += n
        return y
        

if __name__ == '__main__':
    arr = [3,6,1,7,2,0,4,5,9,8]
    arr2 = arr[:]

    print(arr)
    merge_sort(arr)
    print(arr)

    print(arr2)
    bubble_sort(arr2)
    print(arr2)
