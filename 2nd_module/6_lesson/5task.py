def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


words_count = int(input("Введите количество пар слов: "))
synonyms = dict()

for _ in range(words_count):
    word1, word2 = input("пара слов(через '-'): ").lower().replace(" ", "").split("-")
    synonyms[word1] = word2

while True:
    word = input("Введите слово: ").lower()
    if word in synonyms.keys() or word in synonyms.values():
        if word in synonyms.keys():
            print("Синоним:", synonyms.get(word))
        else:
            print("Синоним:", get_key(synonyms, word))
        break
    else:
        print("Такого слова в словаре нет.")