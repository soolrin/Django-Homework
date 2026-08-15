# Дана строка. Посчитай частоту каждой буквы, а затем сколько
# букв имеют одинаковую частоту. Результатом дайте словари.
# ввод: "aabbccc"

text = input("Введите строку: ")
letters = {}
letter_freq = {}

for let in text:
    if let in letters:
        letters[let] += 1
    else:
        letters[let] = 1

for value in letters.values():
    if value in letter_freq:
        letter_freq[value] += 1
    else:
        letter_freq[value] = 1

print(letters)
print(letter_freq)