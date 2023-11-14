zen = open("zen.txt", "r")
zen_line = [line for line in zen if line != "\n"]
for index in range(len(zen_line) - 1, -1, -1):
	print(zen_line[index], end='')