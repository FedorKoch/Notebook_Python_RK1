import datetime

from core.Models.Note import Note
from MVP.ConsoleView import ConsoleView
from MVP.Model import Model


class Presenter:

	def __init__(self, model: Model, view: ConsoleView):
		self.model = model
		self.view = view

	def show_menu(self) -> str:
		self.view.console_clear()
		choise = self.view.show_menu()
		return str(choise)

	def display_clear(self) -> None:
		self.view.console_clear()

	def display_wrong_choise(self) -> None:
		self.view.console_clear()
		self.view.display('Такого пункта меню нет..')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def display(self, data: str) -> None:
		self.view.console_clear()
		self.view.display(data)

	def add_note(self) -> None:
		self.view.console_clear()
		self.model.get_current_book().add_note(Note(id=1,
													title=self.view.get_value('Введите название заметки: '),
													body=self.view.get_value('Введите тело заметки: '),
													date_created=datetime.datetime.now(),
													date_modified=datetime.datetime.now()))
		self.view.display('Заметка добавлена!')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def save_notes_to_file(self) -> None:
		self.view.console_clear()
		self.model.get_current_book().save_notes_db_to_file()
		self.view.display('Файл заметок сохранен!')
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def load_notes_from_file(self) -> None:
		self.view.console_clear()
		self.view.display(self.model.get_current_book().load_notes_db_from_file())
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def find_note_by_id(self) -> None:
		self.view.console_clear()
		try:
			id_from_user: int = int(self.view.get_value('введите ID заметки для поиска: '))
			self.view.display(self.model.get_current_book().find_note_by_id(id_from_user))
			self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
		except:
			self.view.display('Заметки с таким ID нет..')
			self.view.user_waiting('Нажмите Enter чтобы продолжить..')

	def show_all_notes(self) -> None:
		self.view.console_clear()
		notes_list: list[Note] = self.model.get_current_book().get_notes_list()
		for note in notes_list:
			self.view.display(str(note))
		self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')

	def delete_note_by_id(self) -> None:
		self.view.console_clear()
		try:
			id_from_user: int = int(self.view.get_value('введите ID заметки для удаления: '))
			self.view.display(self.model.get_current_book().remove_note_by_id(id_from_user))
			self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
		except:
			self.view.display('Заметки с таким ID нет..')
			self.view.user_waiting('Нажмите Enter чтобы продолжить..')

	def find_notes_by_date(self) -> None:
		self.view.console_clear()
		try:
			date_str: str = self.view.get_value('Введите дату в формате ГГГГ-ММ-ДД: ')
			date_parts: list[str]  = date_str.split('-')
			year: int = int(date_parts[0])
			month: int = int(date_parts[1])
			day: int = int(date_parts[2])
			date_from_user: datetime = datetime.date(year=year, month=month, day=day)
			notes_list: list[Note] = self.model.get_current_book().find_notes_by_date(date_from_user)
			if len(notes_list) == 0:
				self.view.display('Заметок не найдено!')
				self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
			else:
				for note in notes_list:
					self.view.display(str(note))
				self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
		except:
			self.view.display('Неверный формат даты!')
			self.view.user_waiting('Нажмите Enter чтобы продолжить..')
	def edit_note_by_id(self):
		self.view.console_clear()
		try:
			id_from_user: int = int(self.view.get_value('введите ID заметки для изменения: '))
			edited_note = self.model.get_current_book().find_note_by_id(id_from_user)
			if isinstance(edited_note, Note):
				self.view.display('вы выбрали заметку для изменения:\n')
				self.view.display(str(edited_note))
				new_note_body = self.view.get_value('введите новое тело заметки: ')
				self.view.display(self.model.get_current_book().edit_note(edited_note, new_note_body))
				self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
			else:
				self.view.display(edited_note)
				self.view.user_waiting('Нажмите Enter чтобы вернуться в меню..')
		except:
			self.view.display('Заметки с таким ID нет..')
			self.view.user_waiting('Нажмите Enter чтобы продолжить..')
			