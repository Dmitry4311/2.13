#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def show_commands():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <средний балл> - запросить студентов с баллом выше 4.0;")
    print("exit - завершить работу с программой.")


def add_student(students):
    """
    Запросить данные о студенте
    """
    name = input("ФИО? ")
    group = input("Номер группы? ")
    grade = str(input('Оценки: '))
    # Создать словарь.
    student = {
        'name': name,
        'group': group,
        'grade': grade,
    }
    # Добавить словарь в список.
    students.append(student)
    # Отсортировать список в случае необходимости.
    if len(students) > 1:
        students.sort(key=lambda item: item.get('group')[::-1])


def show_list(students):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)
    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                student.get('name', ''),
                student.get('group', ''),
                student.get('grade', 0)
            )
        )
    print(line)


def show_selected(students):
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения студентов из списка.
    for student in students:
        grade = list(map(int, student.get('grade', '').split()))
        if sum(grade) / max(len(grade), 1) >= 4.0:
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('№ группа', student.get('group', ''))
            )
            count += 1
    if count == 0:
        print("Студенты с баллом 5.0 и выше не найдены.")
