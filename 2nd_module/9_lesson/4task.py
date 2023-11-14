import os
first_tour = open("first_tour.txt", "r")
second_tour = open("second_tour.txt", "a")
minimum_score = int(first_tour.readline())

second_tour_count = 0
people = 0
result = []
for line in first_tour:
	surname, name, score = line.split()
	score = int(score)
	if score > minimum_score:
		result.append(str("{0}) {1}. {2} {3}".format(str(second_tour_count+1), name[0].upper(), surname.title(), str(score))))
		people += 1

first_tour.close()
result.sort(reverse = True)
second_tour.write(str(people) + "\n")

for people in range(len(result)):
	second_tour.write(result[people] + "\n")

second_tour.close()