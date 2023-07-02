import os

from MVP.AbstractView import AbstractView


class ConsoleView(AbstractView):

	def get_value(self, title: str) -> str:
		return str(input(title))

	def display(self, data: str) -> None:
		print(data)

	def show_menu(self) -> str:
		print('''
Введите номер действия:
1 - Добавить заметку
2 - Сохранить заметки в файл
3 - Загрузить заметки из файла
4 - Найти заметку по ID
5 - Показать все заметки
6 - Удалить заметку по ID
7 - Вывести все заметки по дате создания
8 - Изменить заметку по ID
0 - Выход''')
		print()
		return str(input('ваш выбор > '))

	def console_clear(self) -> None:
		if os.name == 'posix':
			os.system('clear')
		else:
			os.system('cls')

	def user_waiting(self, waiting_message: str):
		input(f'{waiting_message}') 