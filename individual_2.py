#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from moduls import show_commands, add_student, show_list, show_selected


if __name__ == '__main__':
    # Список студентов.
    show_commands()

    def main():
        students = []
        # Организовать бесконечный цикл запроса команд.
        while True:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                add_student(students)

            elif command == 'list':
                show_list(students)

            elif command.startswith('select'):
                show_selected(students)

            else:
                print(f"Неизвестная команда {command}", file=sys.stderr)
                
    main()