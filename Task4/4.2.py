import re

def tokenize(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words

with open('data.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = tokenize(text)


word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)


print("3 самых часто встречающихся слова и их количество:")
for word, count in sorted_word_count[:3]:
    print(f"{word}: {count}")