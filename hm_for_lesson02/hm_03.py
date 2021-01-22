# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}

while True:
    month = int(input('Enter the month number: '))
    if month < 1 or month > 12:
        print('There is no such month!')
    elif month == 12 or month < 3:
        print(f'Now: {seasons_dict.get(0)}\nNow: {seasons_list[0]}')
        break
    elif month < 6:
        print(f'Now: {seasons_dict.get(1)}\nNow: {seasons_list[1]}')
        break
    elif month < 9:
        print(f'Now: {seasons_dict.get(2)}\nNow: {seasons_list[2]}')
        break
    else:
        print(f'Now: {seasons_dict.get(3)}\nNow: {seasons_list[3]}')
        break
