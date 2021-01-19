# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
user_list = [8, 8, 6, 5, 5, 5, 2]
print(user_list)

while True:
    num = input('Enter a number or type "q" to exit: ')
    if num.lower() == 'q':
        break
    else:
        num = int(num)

    if num in user_list:
        user_list.insert(user_list.index(num) + 1, num)
    elif num > max(user_list):
        user_list.insert(0, num)
    else:
        user_list.append(num)
    print(f'The list at the moment: {user_list}')
