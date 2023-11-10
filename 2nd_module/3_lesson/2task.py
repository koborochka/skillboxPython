def mergeSortedLists(list1, list2):
    result = sorted(set(list1 + list2))
    return result

list1 = [1, 4, 8, 111]
list2 = [2, 4, 6, 7, 8]

mergedList = mergeSortedLists(list1, list2)
print("Объединенный отсортированный список без дубликатов:", mergedList)
