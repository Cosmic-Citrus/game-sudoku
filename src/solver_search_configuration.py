from solver_base_configuration import BaseSudokuSolverConfiguration
import numpy as np
from time import perf_counter


class BaseSudokuSolverBySearchConfiguration(BaseSudokuSolverConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)
		self._cell_value_counter = None
		self._cell_value_choices = None
		self._number_maximum_iterations = None
		self._number_iterations = None
		self._number_back_tracks = None
		self._search_method = None
		self._get_selected_cell = None

	@property
	def cell_value_counter(self):
		return self._cell_value_counter

	@property
	def cell_value_choices(self):
		return self._cell_value_choices

	@property
	def number_maximum_iterations(self):
		return self._number_maximum_iterations

	@property
	def number_iterations(self):
		return self._number_iterations

	@property
	def number_back_tracks(self):
		return self._number_back_tracks

	@property
	def search_method(self):
		return self._search_method

	@property
	def get_selected_cell(self):
		return self._get_selected_cell

	def initialize_solver_method(self):
		self._solver_method = "Search-Based Sudoku Solver"

	def initialize_cell_value_counter(self):
		self._cell_value_counter = dict(
			zip(
				self.non_missing_characters,
				np.zeros(
					self.non_missing_characters.size,
					dtype=int)))
		for cell_value in self.user_board.reshape(-1):
			if cell_value != self.missing_character:
				self._cell_value_counter[cell_value] += 1

	def update_cell_value_counter_by_forward_track(self, cell_value):
		self._cell_value_counter[cell_value] += 1

	def update_cell_value_counter_by_back_track(self, cell_value):
		self._cell_value_counter[cell_value] -= 1

	def initialize_cell_value_choices(self):
		self._cell_value_choices = dict()
		for (r, c) in self.remaining_cell_indices:
			self._cell_value_choices[(r, c)] = self.get_mutual_value_choices(
				r=r,
				c=c)

	def update_cell_value_choices(self, r, c, b):
		rc_indices = list()
		## forward-track
		if self.user_board[r, c] != self.missing_character:
			self._cell_value_choices.pop(
				(r, c))
		## back-track
		else:
			self._cell_value_choices[(r, c)] = self.get_mutual_value_choices(
				r=r,
				c=c)
			rc_indices.append(
				(r, c))
		## update value-choices of all cells in column
		for ri in range(self.number_cell_rows):
			if ((ri, c) not in rc_indices) and (self.user_board[ri, c] == self.missing_character):
				self._cell_value_choices[(ri, c)] = self.get_mutual_value_choices(
					r=ri,
					c=c)
				rc_indices.append(
					(ri, c))
		## update value-choices of all cells in row
		for ci in range(self.number_cell_columns):
			if ((r, ci) not in rc_indices) and (self.user_board[r, ci] == self.missing_character):
				self._cell_value_choices[(r, ci)] = self.get_mutual_value_choices(
					r=r,
					c=ci)
				rc_indices.append(
					(r, ci))
		## update value-choices of all cells in block
		rjs, cjs = self.get_row_and_column_indices_from_block_number(
			b=b)
		for rj, cj in zip(rjs, cjs):
			if ((rj, cj) not in rc_indices) and (self.user_board[rj, cj] == self.missing_character):
				self._cell_value_choices[(rj, cj)] = self.get_mutual_value_choices(
					r=rj,
					c=cj)
				rc_indices.append(
					(rj, cj))

	def initialize_number_maximum_iterations(self, number_maximum_iterations):
		if isinstance(number_maximum_iterations, float):
			number_maximum_iterations = int(
				number_maximum_iterations)
		if not isinstance(number_maximum_iterations, int):
			raise ValueError("invalid type(number_maximum_iterations): {}".format(type(number_maximum_iterations)))
		if number_maximum_iterations < 1:
			raise ValueError("invalid number_maximum_iterations: {}".format(number_maximum_iterations))
		self._number_maximum_iterations = number_maximum_iterations

	def initialize_number_iterations(self):
		self._number_iterations = 0

	def initialize_number_back_tracks(self):
		self._number_back_tracks = 0

	def update_selected_cell_getter(self, search_method):
		cell_selection_methods = {
			"depth-first search" : self.get_selected_cell_by_depth_first_search,
			"ascending-size search" : self.get_selected_cell_by_ascending_choice_size_search,
			"descending-frequency search" : self.get_selected_cell_by_descending_choice_frequency,
			"adaptive search" : self.get_selected_cell_by_adaptive_search}
		if search_method not in cell_selection_methods.keys():
			raise ValueError("invalid search_method: {}".format(search_method))
		get_selected_cell = cell_selection_methods[search_method]
		self._get_selected_cell = get_selected_cell
		self._search_method = search_method

	def get_mutual_value_choices(self, r, c):
		block = self.get_block(
			board=self.user_board,
			r=r,
			c=c)
		row_choices = self.get_cell_value_choices_by_region(
			region=self.user_board[r, :])
		column_choices = self.get_cell_value_choices_by_region(
			region=self.user_board[:, c])
		block_choices = self.get_cell_value_choices_by_region(
			region=block)
		mutual_choices = np.sort(
			list(
				(row_choices & column_choices & block_choices)))
		return mutual_choices

	def get_cell_value_choices_by_region(self, region):
		value_choices = set([
			character for character in self.non_missing_characters
				if character not in region])
		return value_choices

	def get_selected_cell_by_depth_first_search(self):
		rc_index = None
		for r in range(self.number_cell_rows):
			for c in range(self.number_cell_columns):
				if self.user_board[r, c] == self.missing_character:
					rc_index = (r, c)
					break
		return rc_index

	def get_selected_cell_by_ascending_choice_size_search(self):
		if self.number_cells_remaining > 0:
			(r, c), cell_value_choices = min(
				self.cell_value_choices.items(),
				key=lambda x : len(x[1]))
			rc_index = (r, c)
		else:
			rc_index = None
		return rc_index

	def get_selected_cell_by_descending_choice_frequency(self):
		# if self.number_cells_remaining > 0:
		#     most_frequent_cell_value, frequency = max(
		#         self.cell_value_counter.items(),
		#         key=lambda x : x[1])
		#     rc_index = None
		#     for r in range(self.number_cell_rows):
		#         for c in range(self.number_cell_columns):
		#             if (self.user_board[r, c] == self.missing_character) and (most_frequent_cell_value in self.cell_value_choices[(r, c)]):
		#                 rc_index = (r, c)
		#                 break
		# else:
		#     rc_index = None
		# return rc_index
		rc_index = None
		raise ValueError("not yet implemented")
		return rc_index

	def get_selected_cell_by_adaptive_search(self):
		# if self.number_cells_remaining > 0:
		#     ## rc-index by ascending number of choices
		#     (ri, ci), cell_value_choices = min(
		#         self.cell_value_choices.items(),
		#         key=lambda x : len(x[1]))
		#     ## rc-index by descending frequency of cell-value
		#     (rj, cj) = ...
		#     ## select optimal option
		#     rc_index = ...
		# else:
		#     rc_index = None
		# return rc_index
		rc_index = None
		raise ValueError("not yet implemented")
		return rc_index

class SudokuSolverBySearchConfiguration(BaseSudokuSolverBySearchConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)

	def initialize_solver(self, number_maximum_iterations=1e6, search_method="depth-first search"):
		if not isinstance(self.is_solved, bool):
			raise ValueError("invalid type(self.is_solved): {}".format(type(self.is_solved)))
		self.initialize_solver_method()
		self.initialize_number_maximum_iterations(
			number_maximum_iterations=number_maximum_iterations)
		self.initialize_number_iterations()
		self.initialize_number_back_tracks()
		self.update_selected_cell_getter(
			search_method=search_method)
		if search_method != "depth-first search":
			self.initialize_cell_value_choices()
			self.initialize_cell_value_counter()

	def solve(self, *args, is_suppress_errors=False, **kwargs):
		start_time = perf_counter()
		self.initialize_solver(
			*args,
			**kwargs)
		if self.search_method == "depth-first search":
			self.solve_by_depth_first_search()
		elif self.search_method == "adaptive search":
			self.solve_by_adaptive_search()
		else:
			self.solve_by_choice_tuned_search()
		self.update_solve_status(
			is_raise_errors=np.invert(
				is_suppress_errors))
		if self.is_solved:
			self.update_solved_board()
		end_time = perf_counter()
		if not self.is_solved:
			unsolved_warning_message = self.get_unsolved_warning_message()
			if is_suppress_errors:
				print(
					unsolved_warning_message)
			else:
				raise ValueError(unsolved_warning_message)
		elapsed_seconds = end_time - start_time
		self.initialize_elapsed_seconds(
			start_time=start_time,
			end_time=end_time)

	def solve_by_depth_first_search(self):
		## continue solving puzzle recursively until solved
		if (self.is_solved) or (self.number_iterations >= self.number_maximum_iterations):
			return True
		else:
			## select cell to fill
			rc_index = self.get_selected_cell()
			## continue solving puzzle recursively until solved
			if rc_index is None:
				return True
			else:
				(r, c) = rc_index
				## iterate possibilities or back-track
				block = self.get_block(
					r=r,
					c=c,
					board=self.user_board)
				for cell_value in self.non_missing_characters:
					is_value_out_of_block = (cell_value not in block)
					is_value_out_of_row = (cell_value not in self.user_board[r, :])
					is_value_out_of_column = (cell_value not in self.user_board[:, c])
					if all([is_value_out_of_block, is_value_out_of_row, is_value_out_of_column]):
						self._number_iterations += 1
						self._number_cells_remaining -= 1
						self._user_board[r, c] = cell_value
						## continue solving puzzle recursively until solved
						## OR
						## back-track
						if self.solve_by_depth_first_search():
							return True
						else:
							self._number_back_tracks += 1
							self._number_cells_remaining += 1
							self._user_board[r, c] = self.missing_character
		## continue solving puzzle recursively until solved
		## True if sudoku is solved on next call
		return False

	def solve_by_choice_tuned_search(self):
		## the sudoku is solved or a stop-condition has been reached
		if (self.is_solved) or (self.number_iterations >= self.number_maximum_iterations):
			return True
		## continue solving the sudoku
		else:
			## trigger back-track if empty cells have zero value-choices
			is_empty_without_choices = False
			for (r, c), cell_value_choices in self.cell_value_choices.items():
				if cell_value_choices.size == 0:
					is_empty_without_choices = True
					break
			if is_empty_without_choices:
				return False
			## select cell to fill
			rc_index = self.get_selected_cell()
			if rc_index is None: ## all cells are filled
				return True
			else: ## continue solving the sudoku
				(r, c) = rc_index
				b = self.get_block_number(
					r=r,
					c=c)
				block = self.get_block(
					r=r,
					c=c,
					board=self.user_board)
				## attempt guesses
				for cell_value in self.non_missing_characters:
					is_value_out_of_block = (cell_value not in block)
					is_value_out_of_row = (cell_value not in self.user_board[r, :])
					is_value_out_of_column = (cell_value not in self.user_board[:, c])
					## guess is valid
					if all([is_value_out_of_block, is_value_out_of_row, is_value_out_of_column]):
						self._number_iterations += 1
						self._number_cells_remaining -= 1
						self._user_board[r, c] = cell_value
						self.update_cell_value_counter_by_forward_track(
							cell_value=cell_value)
						self.update_cell_value_choices(
							r=r,
							c=c,
							b=b)
						## sudoku is solved // all cells are filled
						if self.solve_by_choice_tuned_search():
							return True
						## back-track
						else:
							self._number_back_tracks += 1
							self._number_cells_remaining += 1
							self._user_board[r, c] = self.missing_character
							self.update_cell_value_counter_by_back_track(
								cell_value=cell_value)
							self.update_cell_value_choices(
								r=r,
								c=c,
								b=b)
		## only reach here if never reached "return True"
		## trigger back-track
		return False

	def solve_by_adaptive_search(self):
		raise ValueError("not yet implemented")
		## toggle between methods depending upon choices
		## max(frequency) = x1, min(choice_size) = x2 ==> optimal strategy

##