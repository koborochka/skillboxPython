base = open("number.txt", 'r')
data = base.read()
sum = 0
for line in data:
	for char in line:
		if char.isdigit():
			sum += int(char)

answer = open("answer.txt", "w")
answer.write(str(sum))

answer.close()
base.close()