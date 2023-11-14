text_file = open("text.txt", "r")
text = text_file.read()
text_file.close()

letters = {}
total_letters = 0

for char in text:
    if char.isalpha():
        total_letters += 1
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))

analysis_file = open("analysis.txt", "w")
for letter, count in sorted_letters:
    frequency = count / total_letters
    analysis_file.write(f"{letter} {frequency:.3f}\n")

analysis_file.close()