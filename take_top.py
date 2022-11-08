# Подключаем библиотеки

import numpy as np
import pandas as pd
import os
from google.colab import files

# Загружаем файл 'train.csv' с помощью "Загрузить в сессионное хранилище"

# Считываем данные из файлов

train = pd.read_csv('train.csv')
train

users = train['user_id']
courses = train['course_id']
users

# Смотрим, какие курсы проходили чаще всего

courses_number = {} # словарь по частоте прохождений курсов
for course in courses:
    if courses_number.get(course) == None:
        courses_number[course] = 1
    else:
        courses_number[course] += 1
print(courses[0], courses_number[courses[0]])

# Смотрим, какой пользователь какие курсы проходил

user_courses = {} # словарь по тому, какой пользователь какие курсы прошёл
for i in range(10272):
    if user_courses.get(users[i]) == None:
        user_courses[users[i]] = []
    user_courses[users[i]].append(courses[i])
print(users[4], user_courses[users[4]])
#user_courses

# Сортируем курсы по частоте прохождения

d = {'course_id': courses_number.keys(), 'course_num': courses_number.values()}
courses_num = pd.DataFrame(data=d)
courses_num = courses_num.sort_values(by=['course_num'], ascending=False)
frequent_courses = list(courses_num['course_id'])
#frequent_courses
courses_num

# Загружаем файл 'test.csv' с помощью "Загрузить в сессионное хранилище"

test = pd.read_csv('sample_submission.csv')
test

# Создаём список из ID пользователей

test_id = list(test['user_id'])
test_id[:10]

# Даём в качестве рекомендаций пользователю самые популярные курсы

test_answer = {}
for user in test_id:
    num = 0
    test_answer[user] = []
    for course in frequent_courses:
        if num == 3:
            break
        if user_courses.get(user) == None:
            test_answer[user].append(course)
            num += 1
            continue
        if (course not in user_courses[user]) and (course not in test_answer[user]):
            test_answer[user].append(course)
            num += 1
test_answer[78]

# Записываем полученные рекомендации в списки и делаем DataFrame

answer_user_id = test_answer.keys()
answer_courses = test_answer.values()
answer_course_id_1 = []
answer_course_id_2 = []
answer_course_id_3 = []
for rec in answer_courses:
    answer_course_id_1.append(rec[0])
    answer_course_id_2.append(rec[1])
    answer_course_id_3.append(rec[2])

d = {'user_id': answer_user_id, 'course_id_1': answer_course_id_1, \
     'course_id_2': answer_course_id_2, 'course_id_3': answer_course_id_3}
ans = pd.DataFrame(data=d)
ans

# Записываем результаты в файл и скачиваем его

ans.to_csv('ans.csv', index=False)
print('ok')

files.download('ans.csv')
