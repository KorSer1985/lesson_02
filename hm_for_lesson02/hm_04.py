# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
user_str = input('Enter a custom string: ')

user_word = []
num = 1
for i in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f'{num}: {user_word[i]}')
        num += 1
    else:
        print(f'{num}: {user_word[i][:10]}')
        num += 1
