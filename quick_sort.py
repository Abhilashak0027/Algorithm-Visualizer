def quick_sort(arr, low, high, steps):
    if low < high:
        pivot_index = partition(arr, low, high, steps)
        quick_sort(arr, low, pivot_index - 1, steps)
        quick_sort(arr, pivot_index + 1, high, steps)

def partition(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps.append(arr.copy())
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append(arr.copy())
    return i + 1
