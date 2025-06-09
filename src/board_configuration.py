from plotter_base_configuration import BasePlotterConfiguration
import numpy as np


class BaseSudokuBoardSettingsConfiguration(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()
		self._random_state_seed = None
		self._selectable_difficulty_levels = None
		self._is_include_worlds_toughest_puzzle = None
		self._difficulty_level = None
		self._outer_square_length = None
		self._inner_square_length = None
		self._number_cell_rows = None
		self._number_cell_columns = None
		self._number_cells = None
		self._number_block_rows = None
		self._number_block_columns = None
		self._number_blocks = None
		self._missing_character = None
		self._non_missing_characters = None
		self._characters = None
		self._region_sum = None
		self._region_product = None

	@property
	def random_state_seed(self):
		return self._random_state_seed

	@property
	def selectable_difficulty_levels(self):
		return self._selectable_difficulty_levels
	
	@property
	def is_include_worlds_toughest_puzzle(self):
		return self._is_include_worlds_toughest_puzzle
	
	@property
	def difficulty_level(self):
		return self._difficulty_level
	
	@property
	def outer_square_length(self):
		return self._outer_square_length
	
	@property
	def inner_square_length(self):
		return self._inner_square_length
	
	@property
	def number_cell_rows(self):
		return self._number_cell_rows

	@property
	def number_cell_columns(self):
		return self._number_cell_columns

	@property
	def number_cells(self):
		return self._number_cells

	@property
	def number_block_rows(self):
		return self._number_block_rows

	@property
	def number_block_columns(self):
		return self._number_block_columns

	@property
	def number_blocks(self):
		return self._number_blocks

	@property
	def missing_character(self):
		return self._missing_character

	@property
	def non_missing_characters(self):
		return self._non_missing_characters

	@property
	def characters(self):
		return self._characters

	@property
	def region_sum(self):
		return self._region_sum

	@property
	def region_product(self):
		return self._region_product

	@staticmethod
	def initialize_selectable_difficulty_levels(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

	def update_random_state_seed(self, random_state_seed=None):
		if random_state_seed is not None:
			np.random.seed(
				random_state_seed)
		self._random_state_seed = random_state_seed

	def update_difficulty_level(self, difficulty_level):
		if not isinstance(difficulty_level, str):
			raise ValueError("invalid type(difficulty_level): {}".format(type(difficulty_level)))
		if difficulty_level not in self.selectable_difficulty_levels:
			raise ValueError("invalid difficulty_level: {}".format(difficulty_level))
		self._difficulty_level = difficulty_level

	def update_custom_difficulty_level(self):
		self._difficulty_level = None # "custom"

	def initialize_base_board_parameters(self, outer_square_length=9, inner_square_length=3):
		if not isinstance(outer_square_length, int):
			raise ValueError("invalid type(outer_square_length): {}".format(type(outer_square_length)))
		if outer_square_length <= 1:
			raise ValueError("invalid outer_square_length: {}".format(outer_square_length))
		if not isinstance(inner_square_length, int):
			raise ValueError("invalid type(inner_square_length): {}".format(type(inner_square_length)))
		if inner_square_length <= 1:
			raise ValueError("invalid inner_square_length: {}".format(inner_square_length))
		square_root_of_outer_length = np.sqrt(
			outer_square_length)
		integer_square_root_of_outer_length = int(
			square_root_of_outer_length)
		if integer_square_root_of_outer_length != square_root_of_outer_length:
			raise ValueError("outer_square_length={} is not a perfect square".format(outer_square_length))
		if integer_square_root_of_outer_length != inner_square_length:
			raise ValueError("inner_square_length={} is not equivalent to the square root of outer_square_length={}".format(inner_square_length, outer_square_length))
		if (outer_square_length != 9) or (inner_square_length != 3):
			raise ValueError("not yet implemented") ## preset_boards (necessary to initialize selectable_difficulty_levels) are 9x9 ==> 3x3 x 3x3
		number_cell_rows = outer_square_length
		number_cell_columns = outer_square_length
		number_cells = int(
			number_cell_rows * number_cell_columns)
		number_block_rows = inner_square_length
		number_block_columns = inner_square_length
		number_blocks = int(
			number_block_rows * number_block_columns)
		missing_character = 0
		non_missing_characters = np.array(
			list(
				range(
					1,
					outer_square_length + 1)))
		characters = np.concatenate((
			[0],
			non_missing_characters))
		region_sum = int(
			np.sum(
				non_missing_characters))
		region_product = int(
			np.prod(
				non_missing_characters))
		self._outer_square_length = outer_square_length
		self._inner_square_length = inner_square_length
		self._number_cell_rows = number_cell_rows
		self._number_cell_columns = number_cell_columns
		self._number_cells = number_cells
		self._number_block_rows = number_block_rows
		self._number_block_columns = number_block_columns
		self._number_blocks = number_blocks
		self._missing_character = missing_character
		self._non_missing_characters = non_missing_characters
		self._characters = characters
		self._region_sum = region_sum
		self._region_product = region_product

class BaseSudokuBoardOperationsConfiguration(BaseSudokuBoardSettingsConfiguration):

	def __init__(self):
		super().__init__()
		self._user_board = None
		self._solved_board = None
		self._original_board = None
		self._is_solved = None

	@property
	def user_board(self):
		return self._user_board
	
	@property
	def solved_board(self):
		return self._solved_board

	@property
	def original_board(self):
		return self._original_board
	
	@property
	def is_solved(self):
		return self._is_solved

	@staticmethod
	def get_row(r, board):
		return board[r, :].copy()

	@staticmethod
	def get_column(c, board):
		return board[:, c].copy()

	def get_block(self, r, c, board):
		i = r // self.number_block_rows * self.number_block_rows
		j = c // self.number_block_columns * self.number_block_columns
		block = board[i:i+3, j:j+3].copy()
		return block

	def get_block_number(self, r, c):
		b = (r // self.number_block_rows) * self.number_block_rows + (c // self.number_block_columns)
		return b

	def get_row_and_column_indices_from_block_number(self, b):
		top_row = (b // self.number_block_rows) * self.number_block_rows
		leftest_column = int(b)
		while leftest_column >= self.number_block_columns:
			leftest_column -= int(self.number_block_columns)
		leftest_column *= int(self.number_block_columns)
		top_row, leftest_column = int(top_row), int(leftest_column)
		rs, cs = [], []
		for r in range(top_row, top_row + self.number_block_rows):
			for c in range(leftest_column, leftest_column + self.number_block_columns):
				rs.append(r)
				cs.append(c)
		return rs, cs

	def update_solved_board(self):
		if not self.is_solved:
			raise ValueError("cannot update self._solved_board without solving sudoku puzzle")
		self._solved_board = np.copy(
			self.user_board)

	@staticmethod
	def update_solve_status(*args, **kwargs):
		raise ValueError("this method should be over-written by a child class")

class BaseSudokuBoardStateConfiguration(BaseSudokuBoardOperationsConfiguration):

	def __init__(self):
		super().__init__()
		self._is_cells_fillable = None
		self._remaining_cell_indices = None
		self._number_cells_remaining = None
		self._number_cells_occupied = None
		self._number_cells_given = None
		self._preset_boards = None

	@property
	def is_cells_fillable(self):
		return self._is_cells_fillable
	
	@property
	def remaining_cell_indices(self):
		return self._remaining_cell_indices
	
	@property
	def number_cells_remaining(self):
		return self._number_cells_remaining
	
	@property
	def number_cells_occupied(self):
		return self.number_cells - self.number_cells_remaining
	
	@property
	def number_cells_given(self):
		return self._number_cells_given
	
	@property
	def preset_boards(self):
		return self._preset_boards
	
	def initialize_selectable_difficulty_levels(self, is_include_worlds_toughest_puzzle=False):
		if not isinstance(is_include_worlds_toughest_puzzle, bool):
			raise ValueError("invalid type(is_include_worlds_toughest_puzzle): {}".format(type(is_include_worlds_toughest_puzzle)))
		if is_include_worlds_toughest_puzzle:
			selectable_difficulty_levels = tuple(
				list(
					self.preset_boards.keys()))
		else:
			selectable_difficulty_levels = tuple([
				key
					for key in self.preset_boards.keys()
						if key != "worlds toughest puzzle"])
		self._selectable_difficulty_levels = selectable_difficulty_levels
		self._is_include_worlds_toughest_puzzle = is_include_worlds_toughest_puzzle

	def initialize_preset_boards(self):
		preset_boards = {
			## https://sudoku.com/easy/
			"easy" : np.array([
				[9, 0, 0, 3, 0, 0, 0, 7, 1],
				[4, 3, 7, 8, 0, 0, 2, 5, 0],
				[0, 0, 5, 0, 2, 0, 0, 4, 9],
				[0, 5, 8, 4, 0, 9, 0, 3, 0],
				[7, 0, 0, 1, 0, 0, 0, 9, 8],
				[2, 9, 0, 0, 3, 0, 0, 0, 4],
				[0, 8, 0, 0, 1, 3, 0, 0, 0],
				[3, 0, 4, 6, 8, 7, 0, 0, 0],
				[1, 0, 0, 2, 5, 0, 0, 0, 0]],
				dtype=int),
			## https://sudoku.com/medium/
			"medium" : np.array([
				[0, 7, 0, 0, 0, 5, 1, 0, 3],
				[0, 0, 0, 0, 0, 0, 0, 0, 7],
				[0, 1, 3, 7, 2, 6, 8, 0, 0],
				[0, 6, 0, 0, 0, 0, 0, 0, 2],
				[2, 0, 0, 0, 0, 0, 0, 0, 5],
				[0, 0, 0, 8, 4, 0, 9, 0, 0],
				[9, 0, 0, 1, 0, 0, 7, 0, 8],
				[0, 0, 8, 0, 3, 0, 0, 4, 0],
				[0, 0, 0, 0, 8, 9, 6, 5, 1]],
				dtype=int),
			## https://sudoku.com/hard/
			"hard" : np.array([
				[0, 0, 0, 0, 0, 0, 0, 3, 0],
				[3, 4, 9, 0, 0, 1, 2, 0, 0],
				[0, 5, 0, 0, 0, 0, 9, 0, 0],
				[0, 2, 0, 5, 0, 8, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 8, 6, 7],
				[6, 0, 0, 0, 0, 0, 0, 0, 4],
				[0, 0, 0, 6, 0, 0, 0, 0, 0],
				[5, 9, 8, 7, 0, 4, 0, 0, 0],
				[7, 0, 0, 2, 0, 0, 0, 0, 8]],
				dtype=int),
			## https://sudoku.com/expert/
			"expert" : np.array([
				[4, 7, 9, 0, 0, 5, 0, 0, 0],
				[0, 0, 0, 0, 3, 0, 0, 0, 8],
				[0, 0, 0, 0, 0, 0, 0, 6, 0],
				[3, 4, 0, 0, 0, 0, 0, 0, 1],
				[0, 0, 6, 0, 5, 0, 0, 0, 9],
				[8, 0, 0, 0, 0, 0, 0, 0, 6],
				[0, 0, 0, 0, 0, 0, 4, 2, 7],
				[0, 0, 7, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 1, 9, 0, 0, 0, 0]],
				dtype=int),
			## https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
			"worlds toughest puzzle" : np.array([
				[8, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 3, 6, 0, 0, 0, 0, 0],
				[0, 7, 0, 0, 9, 0, 2, 0, 0],
				[0, 5, 0, 0, 0, 7, 0, 0, 0],
				[0, 0, 0, 0, 4, 5, 7, 0, 0],
				[0, 0, 0, 1, 0, 0, 0, 3, 0],
				[0, 0, 1, 0, 0, 0, 0, 6, 8],
				[0, 0, 8, 5, 0, 0, 0, 1, 0],
				[0, 9, 0, 0, 0, 0, 4, 0, 0]],
				dtype=int)}
		self._preset_boards = preset_boards

	def update_fillable_cells_status(self, board):
		is_cells_fillable = (board == self.missing_character)
		self._is_cells_fillable = is_cells_fillable

	def update_remaining_cell_indices(self):
		(rs, cs) = np.where(
			self.is_cells_fillable)
		remaining_cell_indices = np.array([
			(r, c)
				for (r, c) in zip(
					rs,
					cs)])
		self._remaining_cell_indices = remaining_cell_indices

	def update_number_cells_remaining(self, board):
		number_cells_remaining = int(
			np.sum(
				board.flatten() == self.missing_character))
		self._number_cells_remaining = number_cells_remaining

	def update_solve_status(self, is_raise_errors=False):
		is_solved = self.get_board_validation(
			board=self.user_board,
			is_raise_errors=is_raise_errors)
		self._is_solved = is_solved

	def get_board_validation(self, board, is_raise_errors=False):
		is_valid = True
		for r in range(self.number_cell_rows):
			row = self.get_row(
				r=r,
				board=board)
			is_row_valid = self.get_region_validation(
				region=row,
				is_raise_errors=is_raise_errors)
			if not is_row_valid:
				is_valid = False
				break
		for c in range(self.number_cell_columns):
			column = self.get_column(
				c=c,
				board=board)
			is_column_valid = self.get_region_validation(
				region=column,
				is_raise_errors=is_raise_errors)
			if not is_column_valid:
				is_valid = False
				break
		for r in range(0, self.number_cell_rows, self.number_block_rows):
			for c in range(0, self.number_cell_columns, self.number_block_columns):
				block = self.get_block(
					r=r,
					c=c,
					board=board)
				is_block_valid = self.get_region_validation(
					region=block.flatten(),
					is_raise_errors=is_raise_errors)
				if not is_block_valid:
					is_valid = False
					break
		return is_valid

	def get_region_validation(self, region, is_raise_errors=False):
		is_valid = True
		number_unique_cell_values = len(
			set(
				region.tolist()))
		deltas = np.diff([
			number_unique_cell_values,
			region.size,
			self.non_missing_characters.size])
		if np.any(deltas != self.missing_character):
			is_valid = False
			if is_raise_errors:
				raise ValueError("region is not unique")
		if np.any(region == self.missing_character):
			is_valid = False
			if is_raise_errors:
				raise ValueError("region contains empty cells")
		return is_valid

class BaseSudokuBoardTransformConfiguration(BaseSudokuBoardStateConfiguration):

	def __init__(self):
		super().__init__()

	@staticmethod
	def apply_clockwise_rotation(board):
		board = list(zip(*board[::-1]))
		return np.array(board)

	@staticmethod
	def reflect_board(board, is_horizontal=False, is_vertical=False):
		j = -1 if is_horizontal else 1
		i = -1 if is_vertical else 1
		return board[::i, ::j]

	def swap_row_bands(self, board, ri, rj):
		bi = ri // self.number_block_rows * self.number_block_rows
		bj = rj // self.number_block_rows * self.number_block_rows
		i = np.arange(
			bi,
			bi + self.number_block_rows,
			dtype=int)
		j = np.arange(
			bj,
			bj + self.number_block_rows,
			dtype=int)
		board[i, :], board[j, :] = board[j, :], board[i, :]
		return board

	def swap_column_bands(self, board, ci, cj):
		bi = ci // self.number_block_columns * self.number_block_columns
		bj = cj // self.number_block_columns * self.number_block_columns
		i = np.arange(
			bi,
			bi + self.number_block_columns,
			dtype=int)
		j = np.arange(
			bj,
			bj + self.number_block_columns,
			dtype=int)
		board[:, i], board[:, j] = board[:, j], board[:, i]
		return board

	def randomize_character_mapping(self, board):
		original_characters = self.non_missing_characters.copy()
		prime_characters = np.random.choice(
			original_characters,
			size=original_characters.size,
			replace=False)
		mapping = dict(
			zip(
				original_characters,
				prime_characters))
		mapping[self.missing_character] = self.missing_character
		for r in range(self.number_cell_rows):
			for c in range(self.number_cell_columns):
				original_cell_value = board[r, c]
				prime_cell_value = mapping[original_cell_value]
				board[r, c] = prime_cell_value
		return board

class SudokuBoardTransformConfiguration(BaseSudokuBoardTransformConfiguration):

	def __init__(self):
		super().__init__()

	def get_transformed_board(self, board, number_remaps=1, number_rotations=1, number_row_band_swaps=1, number_column_band_swaps=1, is_reflect_horizontal=False, is_reflect_vertical=False):
		
		def verify_strictly_positive_integer(s, value):
			if not isinstance(value, int):
				raise ValueError("invalid type({}): {}".format(s, type(value)))
			if value < 0:
				raise ValueError("invalid {}: {}".format(s, value))

		if not isinstance(board, np.ndarray):
			raise ValueError("invalid type(board): {}".format(type(board)))
		verify_strictly_positive_integer(
			s="number_remaps",
			value=number_remaps)
		verify_strictly_positive_integer(
			s="number_rotations",
			value=number_rotations)
		verify_strictly_positive_integer(
			s="number_row_band_swaps",
			value=number_row_band_swaps)
		verify_strictly_positive_integer(
			s="number_column_band_swaps",
			value=number_column_band_swaps)
		if not isinstance(is_reflect_horizontal, bool):
			raise ValueError("invalid type(is_reflect_horizontal): {}".format(type(is_reflect_horizontal)))
		if not isinstance(is_reflect_vertical, bool):
			raise ValueError("invalid type(is_reflect_vertical): {}".format(type(is_reflect_vertical)))
		modified_board = board.copy()
		for _ in range(number_remaps):
			modified_board = self.randomize_character_mapping(
				board=modified_board)
		for _ in range(number_rotations):
			modified_board = self.apply_clockwise_rotation(
				board=modified_board)
		modified_board = self.reflect_board(
			board=modified_board,
			is_horizontal=is_reflect_horizontal,
			is_vertical=is_reflect_vertical)
		if (number_row_band_swaps > 0) or (number_column_band_swaps > 0):
			swappable_dimensions = np.arange(
				self.non_missing_characters.size,
				dtype=int)
			for _ in range(number_row_band_swaps):
				ri, rj = np.random.choice(
					swappable_dimensions,
					size=2,
					replace=False)
				modified_board = self.swap_row_bands(
					board=modified_board.copy(),
					ri=ri,
					rj=rj)
			for _ in range(number_column_band_swaps):
				ci, cj = np.random.choice(
					swappable_dimensions,
					size=2,
					replace=False)
				modified_board = self.swap_column_bands(
					board=modified_board,
					ci=ci,
					cj=cj)
		return modified_board

class BaseSudokuBoardConfiguration(SudokuBoardTransformConfiguration):

	def __init__(self):
		super().__init__()

	def get_initial_board_without_missing_characters(self):
		values = self.non_missing_characters.copy()
		board = [
			values.copy()]
		divisors = [
			self.number_block_rows]
		while True:
			prev_div = divisors[-1]
			curr_div = prev_div + self.number_block_rows
			if curr_div >= self.number_cell_rows:
				curr_div = curr_div - self.number_cell_rows + 1
			divisors.append(curr_div)
			if len(divisors) == self.number_cell_rows - 1:
				break
		indices = np.array(
			divisors)
		for i in indices:
			row = np.array(values[i:].tolist() + values[:i].tolist())
			board.append(
				row)
		board = np.array(
			board,
			dtype=int)
		return board

	def get_initial_board_with_missing_characters(self):
		if self.difficulty_level not in self.preset_boards.keys():
			raise ValueError("invalid self.difficulty_level={}".format(self.difficulty_level))
		board = np.copy(
			self.preset_boards[self.difficulty_level])
		return board

	def get_input_board(self, board):
		if isinstance(board, SudokuBoardConfiguration):
			if not isinstance(board.user_board, np.ndarray):
				raise ValueError("board.user_board is not initialized")
			modified_board = np.copy(
				board.user_board)
		else:
			if isinstance(board, (tuple, list)):
				modified_board = np.array(
					board)
			elif isinstance(board, np.ndarray):
				modified_board = np.copy(
					board)
			else:
				raise ValueError("invalid type(board): {}".format(type(board)))
		if modified_board.shape != (self.number_cell_rows, self.number_cell_columns):
			raise ValueError("invalid board.shape: {}".format(board.shape))
		board_characters = np.unique(
			modified_board.flatten())
		for board_character in board_characters:
			if board_character not in self.characters:
				raise ValueError("invalid character on board: {}".format(board_character))
		if self.missing_character not in board_characters:
			self.get_board_validation(
				board=modified_board,
				is_raise_errors=True)
		return modified_board

class SudokuBoardConfiguration(BaseSudokuBoardConfiguration):

	def __init__(self, random_state_seed=None, outer_square_length=9, inner_square_length=3, is_include_worlds_toughest_puzzle=False):
		super().__init__()
		self.update_random_state_seed(
			random_state_seed=random_state_seed)
		self.initialize_base_board_parameters(
			outer_square_length=outer_square_length,
			inner_square_length=inner_square_length)
		self.initialize_preset_boards()
		self.initialize_selectable_difficulty_levels(
			is_include_worlds_toughest_puzzle=is_include_worlds_toughest_puzzle)

	def __repr__(self):
		sudoku_board = f"SudokuBoardConfiguration({self.random_state_seed, self.outer_square_length, self.inner_square_length})"
		return sudoku_board

	def __str__(self):
		s = "\n ** SUDOKU **\n"
		if self.user_board is not None:
			s += "\n - USER BOARD:"
			s += "\n .. number of cells given:\n{}\n".format(
				self.number_cells_given)
			s += "\n .. number of cells occupied:\n{}\n".format(
				self.number_cells_occupied)
			s += "\n .. number of cells remaining:\n{}\n".format(
				self.number_cells_remaining)
			s += "\n .. is solved:\n{}\n".format(
				self.is_solved)
			s += "\n .. board:\n{}\n".format(
				self.user_board)
		return s

	def initialize_board(self, difficulty_level=None, board=None, is_apply_transform=False, random_state_seed=None):
		if not isinstance(is_apply_transform, bool):
			raise ValueError("invalid type(is_apply_transform): {}".format(type(is_apply_transform)))
		self.update_random_state_seed(
			random_state_seed=random_state_seed)
		if board is None:
			is_raise_errors = False
			if difficulty_level is None:
				## try generating boards by removing cells per difficulty level
				## not for user
				self.update_custom_difficulty_level()
				# raise ValueError("invalid difficulty_level: {}".format(difficulty_level))
				modified_board = self.get_initial_board_without_missing_characters()
			else:
				self.update_difficulty_level(
					difficulty_level=difficulty_level)
				if self.difficulty_level is None:
					modified_board = self.get_initial_board_without_missing_characters()
				else:
					modified_board = self.get_initial_board_with_missing_characters()
		else:
			# is_raise_errors = True
			is_raise_errors = False
			self.update_custom_difficulty_level()
			modified_board = self.get_input_board(
				board=board)
		if is_apply_transform:
			modified_board = self.get_transformed_board(
				board=modified_board,
				number_remaps=10,
				number_rotations=int(
					np.random.choice(
						np.arange(
							4, ## ... --> 0 --> 1 --> 2 --> 3 --> 0 --> ...
							dtype=int))),
				number_row_band_swaps=10,
				number_column_band_swaps=10,
				is_reflect_horizontal=bool(
					np.random.choice(
						np.array([
							True,
							False]))),
				is_reflect_vertical=bool(
					np.random.choice(
						np.array([
							True,
							False]))))
		self.update_initial_state(
			board=modified_board,
			is_raise_errors=is_raise_errors)

	def update_initial_state(self, board, is_raise_errors):
		self._user_board = board.copy()
		self._original_board = board.copy()
		self.update_fillable_cells_status(
			board=board)
		self.update_remaining_cell_indices()
		self.update_number_cells_remaining(
			board=board)
		self._number_cells_given = int(
			self.number_cells_occupied)
		self.update_solve_status(
			is_raise_errors=is_raise_errors)

##