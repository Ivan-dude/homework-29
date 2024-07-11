#Использование %
team1_num = 5
team2_num = 6
print('"В команде  %s' % 'Мастера кода участников:', team1_num, '!"')
print('"Итого сегодня в командах участников %s' % team1_num, 'и', team2_num,'!"')

# Использование format():
score_2 = 42
team1_time = 18015.2
print('"Команда {} данных решила задач: {}!"'.format('Волшебники', score_2))
print('"Волшебники данных решили задачи за {time}c!"'.format(time=team1_time))

# Использование f-строк:
team1_num = 6 #переопределил
team2_num = 6 #переопределил
score1 = 40
score_1 = 40
score_2 = 42
team1_time = 1552.512 #переопределил для данного примера
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = '"Победа команды Волшебники данных!"'
challenge_result2 =  'Мастера кода' #добавил для удобства, чтобы меньше печатать
print(f'"Команды решили {score_1} и {score_2} задач."')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'"Победа команды {challenge_result2}!"'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'{challenge_result}'
else: result = 'Ничья!'
print(result)
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."')
