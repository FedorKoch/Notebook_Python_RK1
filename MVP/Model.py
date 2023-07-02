from core.Infrastructure.Notebook import Notebook


class Model:
	def __init__(self):
		self.current_book = Notebook()

	def get_current_book(self) -> Notebook:
		return self.current_book