import json
from datetime import datetime

from core.Models.Note import Note


class Notebook:
	def __init__(self):
		self.notes_list: list[Note] = []
		self.db_file_name: str = 'notes_db.json'

	def add_note(self, note: Note) -> None:
		if len(self.notes_list) == 0:
			self.notes_list.append(note)
		else:
			note.set_id(self.notes_list[-1].get_id() + 1)
			self.notes_list.append(note)

	def get_note_by_idx(self, idx: int) -> Note | None:
		for note in self.notes_list:
			if note.get_id() == idx:
				return note
		return None

	def load_notes_db_from_file(self) -> str:
		try:
			with open(self.db_file_name, 'r') as file:
				data = json.load(file)
				if data:
					for note_data in data:
						id = note_data["id"]
						title = note_data["title"]
						body = note_data["body"]
						date_created = datetime.fromisoformat(note_data["date_created"])
						date_modified = datetime.fromisoformat(note_data["date_modified"])
						note = Note(id, title, body, date_created, date_modified)
						self.notes_list.append(note)
			return 'Библиотека записок загружена!'
		except FileNotFoundError:
			return f'Файл {self.db_file_name} не найден'

	def save_notes_db_to_file(self) -> None:
		serialized_notes = [note.serialize() for note in self.notes_list]

		with open(self.db_file_name, 'w') as file:
			json.dump(serialized_notes, file, indent=4)

	def find_note_by_id(self, note_id: int) -> Note | str:
		for note in self.notes_list:
			if note.get_id() == note_id:
				return note
		return f'заметки с id "{note_id}" не существует'

	def get_notes_list(self) -> list[Note]:
		return self.notes_list

	def remove_note_by_id(self, note_id: int) -> str:
		note_to_del = self.find_note_by_id(note_id)
		if isinstance(note_to_del, Note):
			self.notes_list.remove(note_to_del)
			return f'заметка с id "{note_id}" удалена!'
		return f'заметки с id "{note_id}" не существует'

	def find_notes_by_date(self, date: datetime.date) -> list[Note]:
		result_notes_list: list[Note] = []
		for note in self.notes_list:
			if note.date_created.date() == date:
				result_notes_list.append(note)
		return result_notes_list

	def edit_note(self, note_to_edit: Note, new_body: str) -> str:
		note_id = note_to_edit.get_id()
		index_to_edit = self.notes_list.index(note_to_edit)
		edited_note = self.notes_list.pop(index_to_edit)
		edited_note.set_body(new_body)
		edited_note.set_date_modified(datetime.now())
		self.notes_list.insert(index_to_edit, edited_note)
		return f'заметка с id "{note_id}" изменена!'