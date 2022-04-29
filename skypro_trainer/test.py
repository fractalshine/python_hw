keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь" ]
word_count = {}

for word in keywords:
    word_count[word] = len(word)

print(word_count.get(input()))
