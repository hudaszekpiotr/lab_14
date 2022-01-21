

# Python program for implementation of Bubble Sort
 
def bubble_sort(arr, ascending = True):
    n = len(arr)
    if ascending:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    else:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
 


