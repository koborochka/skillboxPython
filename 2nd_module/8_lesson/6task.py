def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less, equal, greater = partition(arr[:-1], pivot)
        return quicksort(less) + [pivot] + quicksort(greater)


def partition(arr, pivot):
    less = []
    equal = []
    greater = []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return less, equal, greater


numbers = [4, 9, 2, 7, 5]
sorted_numbers = quicksort(numbers)
print("Отсортированный список:", sorted_numbers)
