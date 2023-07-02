import datetime


class Note:
	def __init__(self, id: int,
					title: str,
					body: str,
					date_created: datetime,
					date_modified: datetime):
		self.id = id
		self.title = title
		self.body = body
		self.date_created = date_created
		self.date_modified = date_modified

	def __str__(self):
		return "* * *\n"\
				f"ID: {self.id}\n" \
				"--\n" \
				f"Название: {self.title}\n" \
				"--\n"\
				f"Заметка: {self.body}\n" \
				"--\n" \
				f"Дата создания: {self.date_created.date()}\n" \
				f"Дата изменения: {self.date_modified.date()}\n" \
				"* * *\n"
	def get_id(self) -> int:
		return self.id

	def set_id(self, new_id: int) -> None:
		self.id = new_id

	def get_title(self) -> str:
		return self.title

	def set_title(self, new_title: str) -> None:
		self.title = new_title

	def get_body(self) -> str:
		return self.body

	def set_body(self, new_body: str) -> None:
		self.body = new_body

	def get_created_date(self) -> datetime:
		return self.date_created

	def get_date_modified(self) -> datetime:
		return self.date_modified

	def set_date_modified(self, new_dete: datetime) -> None:
		self.date_modified = new_dete

	def serialize(self) -> dict:
		return {
				"id": self.id,
				"title": self.title,
				"body": self.body,
				"date_created": self.date_created.isoformat(),
				"date_modified": self.date_modified.isoformat()
		}