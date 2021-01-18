digits_str = ['abcdefg', 'list', 'type']
digits_list = [1, 2, 3, 4, 5, 6, 7]

# for digit in range(0,len(digits_list)):
#     print(f'Digit :{digits_str[digit]} and {digits_list[digit]}')

# for el in digits_str:
#     print("New el")
#     for ch in el:
#         print(ch)

'''
Описание работника:
характеристики работника:
    имя_фамилия
    возраст
    место работы
    есть ли прививка
'''
# worker_list = ['Name', 'Surname', 'Age']

# worker_dict = {'name_surname':'Basil Petrov',
#                'place': 'shop',
#                'vaccine': True}
#
# print(worker_dict['vaccine'])
# worker_dict['was_ill'] = False
# print(worker_dict.values())

'''
Вход через КПП:
На входе оставляет каждый данные о себе:
    имя фамилия
    место работы
    вакцина есть ли
    температура
Мы должны сохранить всех кто пришел,
если у нас кто-то заболел и у них есть не привитые на месте работы
то мы должны закрыть вход и вывести проблемную зону.
'''

worker_dict = {'name_surname': None,
               'place': None,
               'vaccine': None,
               'temperature': None}

today_workers = []
while True:
    continue_check = input("Continue: ")
    if continue_check == 'No':
        print(f'Today workers: {today_workers}')
        break
    worker_dict['name_surname'] = input("Your name: ")
    worker_dict['place'] = input("Your place: ")
    # worker_dict['vaccine'] = bool(input("Vaccine?: ")) #не рабочий вариант
    worker_dict['vaccine'] = input("Vaccine?: ") #работает проверка со строкой
    print(worker_dict['vaccine'])
    worker_dict['temperature'] = float(input("Temperature: "))
    today_workers.append(worker_dict.copy())
    if worker_dict['temperature'] > 37.5:
        inf_place = worker_dict['place']
        ill_workers = []
        for worker in today_workers:
            if worker['place'] == inf_place and worker['vaccine'] == 'No':
                print("Person is ill!")
                ill_workers.append(worker)
        print(f"Alarm! Next workers could be ill {ill_workers}" )
        print(f'Today workers: {today_workers}')
        break
