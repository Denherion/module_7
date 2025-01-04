# Домашнее задание по теме "Форматирование строк"
team1_name = "Мастера кода"
team2_name = "Волшебники Данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

"""Использование %:"""
print("В команде %(team1_name)s участников: %(team1_num)s!" % {'team1_name': 'Мастера кода', 'team1_num': 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" % {'team1_num': 5, 'team2_num': 6})

"""Использование format():"""
print("Команда {} решила задач: {}!".format(team2_name, score_2))
print("{} решили задачи за {} с!".format(team2_name, team1_time))

"""Использование f-строк:"""
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f"Победа команды {team1_name}!")
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f"Победа команды {team2_name}!")
else:
    print("Ничья!")