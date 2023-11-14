from collections import defaultdict

with open('voina-i-mir.txt', 'r', encoding='windows-1251') as file:
    text = file.read()

letter_counts = defaultdict(int)
total_letters = 0

for char in text:
    if char.isalpha():
        total_letters += 1
        letter_counts[char] += 1

sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

with open('voina-i-mir-letter-statistics.txt', 'w', encoding='utf-8') as file:
    for letter, count in sorted_letter_counts:
        frequency = count / total_letters
        file.write(f"{letter}: {frequency:.6f}\n")