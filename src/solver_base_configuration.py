from board_configuration import SudokuBoardConfiguration


class BaseSudokuSolverConfiguration(SudokuBoardConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)
		self._solver_method = None
		self._elapsed_seconds = None

	@property
	def solver_method(self):
		return self._solver_method

	@property
	def elapsed_seconds(self):
		return self._elapsed_seconds
	
	@staticmethod
	def solve(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	@staticmethod
	def initialize_solver_method(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	def get_unsolved_warning_message(self):
		s = "self.solver_method={} did not solve sudoku puzzle".format(
			self.solver_method)
		return s

	def initialize_elapsed_seconds(self, start_time, end_time):
		elapsed_seconds = end_time - start_time
		self._elapsed_seconds = elapsed_seconds



##