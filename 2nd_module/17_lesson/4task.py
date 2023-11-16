def count_unique_characters(s: str) -> int:
    s_lower = s.lower()
    unique_letters = filter(lambda x: s_lower.count(x) == 1 and x.isalpha(), s_lower)
    return len(set(unique_letters))


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
