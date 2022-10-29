def bubble_sort(arr):
    n = len(arr)
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]['value'] > arr[j + 1]['value']:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return