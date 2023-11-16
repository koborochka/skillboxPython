letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
results = list(map(lambda x, y: (x, y), letters, numbers))
print(results)
