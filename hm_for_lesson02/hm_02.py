# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
item_count = int(input('Enter the value of the list items: '))
user_list = []

i = 0
item = 0
while i < item_count:
    user_list.append(input('Enter the following list value: '))
    i += 1

for elem in range(int(len(user_list)/2)):
    user_list[item], user_list[item + 1] = user_list[item + 1], user_list[item]
    item += 2
print(user_list)
