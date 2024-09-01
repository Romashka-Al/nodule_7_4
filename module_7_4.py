team1_num = 5
team2_num = 6
print('В команде Мастера кода участников %x' % team1_num)
print('Итого сегодня в командах участников: %x и %x' % (team1_num, team2_num))

score_2 = 42
team2_time = 18015.2
print('Команда Вошебники данных решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {time} с!'.format(time=team2_time))

score_1 = 40
team1_time = 17900
task_total = score_1 + score_2
time_avg = (team1_time + team2_time) / task_total
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result}')
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')