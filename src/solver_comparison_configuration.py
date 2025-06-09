from board_configuration import SudokuBoardConfiguration
from solver_search_configuration import SudokuSolverBySearchConfiguration
from solver_dancing_links_configuration import SudokuSolverByDancingLinksConfiguration
from plotter_solver_comparison_configuration import SudokuSolverComparisonViewer
import numpy as np


class BaseSudokuSolverComparisonConfiguration(SudokuBoardConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)
		self._number_runs_per_solver = None
		self._boards_by_difficulty = None
		self._solver_selection_mapping = None
		self._selectable_solver_sub_methods = None
		self._comparison_information = None

	@property
	def number_runs_per_solver(self):
		return self._number_runs_per_solver

	@property
	def boards_by_difficulty(self):
		return self._boards_by_difficulty
	
	@property
	def solver_selection_mapping(self):
		return self._solver_selection_mapping

	@property
	def selectable_solver_sub_methods(self):
		return self._selectable_solver_sub_methods

	@property
	def comparison_information(self):
		return self._comparison_information
		
	@staticmethod
	def get_statistics(arr):
		statistics = {
			"mean" : np.nanmean(
				arr),
			"median" : np.nanmedian(
				arr),
			"standard deviation" : np.nanstd(
				arr),
			"maximum" : np.nanmax(
				arr),
			"minimum" : np.nanmin(
				arr),
			"size" : arr.size}
		return statistics

	def initialize_number_runs_per_solver(self, number_runs_per_solver):
		if not isinstance(number_runs_per_solver, int):
			raise ValueError("invalid type(number_runs_per_solver): {}".format(type(number_runs_per_solver)))
		if number_runs_per_solver <= 0:
			raise ValueError("invalid number_runs_per_solver: {}".format(number_runs_per_solver))
		self._number_runs_per_solver = number_runs_per_solver

	def initialize_boards_by_difficulty(self):
		boards_by_difficulty = dict()
		for difficulty_level in self.selectable_difficulty_levels:
			boards_at_same_difficulty_level = list()
			for index_at_run in range(self.number_runs_per_solver):
				self.initialize_board(
					difficulty_level=difficulty_level,
					board=None,
					is_apply_transform=True,
					random_state_seed=None)
				boards_at_same_difficulty_level.append(
					self.user_board.copy())
			boards_by_difficulty[difficulty_level] = boards_at_same_difficulty_level
		self._boards_by_difficulty = boards_by_difficulty

	def initialize_solver_selection_mapping(self):

		def get_depth_first_search_solver(board, number_maximum_iterations=1e6):
			solver = SudokuSolverBySearchConfiguration(
				is_include_worlds_toughest_puzzle=self.is_include_worlds_toughest_puzzle)
			solver.initialize_board(
				board=board)
			solver.solve(
				search_method="depth-first search",
				is_suppress_errors=True,
				number_maximum_iterations=number_maximum_iterations)
			return solver

		def get_ascending_size_search_solver(board, number_maximum_iterations=1e6):
			solver = SudokuSolverBySearchConfiguration(
				is_include_worlds_toughest_puzzle=self.is_include_worlds_toughest_puzzle)
			solver.initialize_board(
				board=board)
			solver.solve(
				search_method="ascending-size search",
				is_suppress_errors=True,
				number_maximum_iterations=number_maximum_iterations)
			return solver

		def get_descending_frequency_search_solver(board, number_maximum_iterations=1e6):
			solver = SudokuSolverBySearchConfiguration(
				is_include_worlds_toughest_puzzle=self.is_include_worlds_toughest_puzzle)
			solver.initialize_board(
				board=board)
			solver.solve(
				search_method="descending-frequency search",
				is_suppress_errors=True,
				number_maximum_iterations=number_maximum_iterations)
			return solver

		def get_adaptive_search_solver(board, number_maximum_iterations=1e6):
			solver = SudokuSolverBySearchConfiguration(
				is_include_worlds_toughest_puzzle=self.is_include_worlds_toughest_puzzle)
			solver.initialize_board(
				board=board)
			solver.solve(
				search_method="adaptive search",
				is_suppress_errors=True,
				number_maximum_iterations=number_maximum_iterations)
			return solver

		def get_dancing_links_solver(board, ):
			solver = SudokuSolverByDancingLinksConfiguration(
				is_include_worlds_toughest_puzzle=self.is_include_worlds_toughest_puzzle)
			solver.initialize_board(
				board=board)
			solver.solve(
				is_suppress_errors=True)
			return solver

		solver_selection_mapping = {
			"depth-first search" : get_depth_first_search_solver,
			"ascending-size search" : get_ascending_size_search_solver,
			"descending-frequency search" : get_descending_frequency_search_solver,
			"adaptive search" : get_adaptive_search_solver,
			"dancing links" : get_dancing_links_solver}
		self._solver_selection_mapping = solver_selection_mapping

	def initialize_selectable_solver_sub_methods(self, is_include_depth_first_search=False, is_include_ascending_size_search=False, is_include_descending_frequency_search=False, is_include_adaptive_search=False, is_include_dancing_links=False):
		if not isinstance(is_include_depth_first_search, bool):
			raise ValueError("invalid type(is_include_depth_first_search): {}".format(type(is_include_depth_first_search)))
		if not isinstance(is_include_ascending_size_search, bool):
			raise ValueError("invalid type(is_include_ascending_size_search): {}".format(type(is_include_ascending_size_search)))
		if not isinstance(is_include_descending_frequency_search, bool):
			raise ValueError("invalid type(is_include_descending_frequency_search): {}".format(type(is_include_descending_frequency_search)))
		if not isinstance(is_include_adaptive_search, bool):
			raise ValueError("invalid type(is_include_adaptive_search): {}".format(type(is_include_adaptive_search)))
		if not isinstance(is_include_dancing_links, bool):
			raise ValueError("invalid type(is_include_dancing_links): {}".format(type(is_include_dancing_links)))
		if not is_include_depth_first_search:
			self._solver_selection_mapping.pop(
				"depth-first search")
		if not is_include_ascending_size_search:
			self._solver_selection_mapping.pop(
				"ascending-size search")
		if not is_include_descending_frequency_search:
			self._solver_selection_mapping.pop(
				"descending-frequency search")
		if not is_include_adaptive_search:
			self._solver_selection_mapping.pop(
				"adaptive search")
		if not is_include_dancing_links:
			self._solver_selection_mapping.pop(
				"dancing links")
		selectable_solver_sub_methods = tuple(
			list(
				self.solver_selection_mapping.keys()))
		number_selectable_solver_sub_methods = len(
			selectable_solver_sub_methods)
		if number_selectable_solver_sub_methods == 0:
			raise ValueError("at least one solver_sub_method is required as input to evaluate a comparison")
		self._selectable_solver_sub_methods = selectable_solver_sub_methods

	def initialize_comparison_information(self):

		def get_data():
			data = dict()
			for difficulty_level in self.selectable_difficulty_levels:
				if difficulty_level not in data.keys():
					data[difficulty_level] = dict()
				for index_at_run in range(self.number_runs_per_solver):
					for solver_sub_method in self.selectable_solver_sub_methods:
						if solver_sub_method not in data[difficulty_level].keys():
							data[difficulty_level][solver_sub_method] = {
								"elapsed seconds" : list(),
								"is solved" : list(),
								"number iterations" : list(),
								"number back-tracks" : list()}
						board = np.copy(
							self.boards_by_difficulty[difficulty_level][index_at_run])
						get_solver = self.solver_selection_mapping[solver_sub_method]
						solver = get_solver(
							board=board)
						if solver.is_solved:
							elapsed_seconds = solver.elapsed_seconds
						else:
							elapsed_seconds = np.nan
						data[difficulty_level][solver_sub_method]["elapsed seconds"].append(
							elapsed_seconds)
						data[difficulty_level][solver_sub_method]["is solved"].append(
							solver.is_solved)
						if hasattr(solver, "_number_iterations"):
							data[difficulty_level][solver_sub_method]["number iterations"].append(
								solver.number_iterations)
						else:
							if "number iterations" in data[difficulty_level][solver_sub_method].keys():
								data[difficulty_level][solver_sub_method]["data"].pop(
									"number iterations")
						if hasattr(solver, "number_back_tracks"):
							data[difficulty_level][solver_sub_method]["number back-tracks"].append(
								solver.number_back_tracks)
						else:
							if "number back-tracks" in data[difficulty_level][solver_sub_method].keys():
								data[difficulty_level][solver_sub_method].pop(
									"number back-tracks")
			return data

		def get_statistics(data):
			statistics = dict()
			for difficulty_level, data_at_difficulty_level in data.items():
				if difficulty_level not in statistics.keys():
					statistics[difficulty_level] = dict()
				for solver_sub_method, data_at_solver in data_at_difficulty_level.items():
					if solver_sub_method not in statistics[difficulty_level].keys():
						statistics[difficulty_level][solver_sub_method] = {
							parameter_name : dict()
								for parameter_name in data[difficulty_level][solver_sub_method].keys()}
					for parameter_name, parameter_value in data[difficulty_level][solver_sub_method].items():
						if parameter_name == "is solved": ## bool --> int
							modified_parameter_values = np.array(
								parameter_value,
								dtype=int)
						else:
							modified_parameter_values = np.array(
								parameter_value)
						parameter_statistics = self.get_statistics(
							modified_parameter_values)
						statistics[difficulty_level][solver_sub_method][parameter_name] = parameter_statistics
			return statistics

		def get_parameters(data):
			arbitrary_difficulty_level = self.selectable_difficulty_levels[0]
			solver_sub_methods = tuple(
				list(
					data[arbitrary_difficulty_level].keys()))
			all_parameters = set()
			for solver_sub_method in solver_sub_methods:
				all_parameters.update(
					list(
						data[arbitrary_difficulty_level][solver_sub_method].keys()))
			all_parameters = tuple(
				list(
					all_parameters))
			exclusive_parameters_by_solver_sub_method = dict()
			all_exclusive_parameters = set()
			for solver_sub_method in solver_sub_methods:
				exclusive_parameters_by_solver_sub_method[solver_sub_method] = list()
				solver_parameters = list(
					data[arbitrary_difficulty_level][solver_sub_method].keys())
				for solver_parameter in all_parameters:
					if solver_parameter not in solver_parameters:
						all_exclusive_parameters.add(
							solver_parameter)
						exclusive_parameters_by_solver_sub_method[solver_sub_method].append(
							solver_parameter)
				number_exclusive_parameters_at_solver_sub_method = len(
					exclusive_parameters_by_solver_sub_method[solver_sub_method])
				if number_exclusive_parameters_at_solver_sub_method == 0:
					exclusive_parameters_by_solver_sub_method[solver_sub_method] = None
			all_mutual_parameters = tuple(
				list(
					set(all_parameters) - all_exclusive_parameters))
			all_exclusive_parameters = tuple(
				list(
					all_exclusive_parameters))
			solver_sub_methods = tuple(
				list(
					exclusive_parameters_by_solver_sub_method.keys()))
			parameters = {
				"all metrics" : all_parameters,
				"all mutual metrics" : all_mutual_parameters,
				"all exclusive metrics" : all_exclusive_parameters,
				"exclusive metrics by solver sub-method" : exclusive_parameters_by_solver_sub_method,
				"solver sub-methods" : solver_sub_methods}
			return parameters

		data = get_data()
		statistics = get_statistics(
			data=data)
		parameters = get_parameters(
			data=data)
		comparison_information = {
			"data" : data,
			"statistics" : statistics,
			"parameters" : parameters}
		self._comparison_information = comparison_information

class SudokuSolverComparisonConfiguration(BaseSudokuSolverComparisonConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)

	def __repr__(self):
		solver_comparison = f"SudokuSolverComparisonConfiguration({self.random_state_seed, self.outer_square_length, self.inner_square_length, self.is_include_worlds_toughest_puzzle})"
		return solver_comparison

	def __str__(self):
		# s = "The fastest sudoku solver is ..."
		raise ValueError("not yet implemented")

	def initialize_comparison(self, number_runs_per_solver, is_include_depth_first_search=False, is_include_ascending_size_search=False, is_include_descending_frequency_search=False, is_include_adaptive_search=False, is_include_dancing_links=False, random_state_seed=None):
		self.update_random_state_seed(
			random_state_seed=random_state_seed)
		self.initialize_number_runs_per_solver(
			number_runs_per_solver=number_runs_per_solver)
		self.initialize_boards_by_difficulty()
		self.initialize_solver_selection_mapping()
		self.initialize_selectable_solver_sub_methods(
			is_include_depth_first_search=is_include_depth_first_search,
			is_include_ascending_size_search=is_include_ascending_size_search,
			is_include_descending_frequency_search=is_include_descending_frequency_search,
			is_include_adaptive_search=is_include_adaptive_search,
			is_include_dancing_links=is_include_dancing_links)
		self.initialize_comparison_information()

	def view_comparison_of_solver_timings(self, *args, **kwargs):
		viewer = SudokuSolverComparisonViewer()
		viewer.initialize_visual_settings()
		viewer.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		solver_comparison = self
		parameter = "elapsed seconds"
		viewer.view_solver_comparison_of_parameter(
			solver_comparison,
			parameter,
			*args,
			**kwargs)

	def view_comparison_of_solver_successes(self, *args, **kwargs):
		viewer = SudokuSolverComparisonViewer()
		viewer.initialize_visual_settings()
		viewer.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		solver_comparison = self
		parameter = "is solved"
		viewer.view_solver_comparison_of_parameter(
			solver_comparison,
			parameter,
			*args,
			**kwargs)

	def view_comparison_of_solver_iterations(self, *args, **kwargs):
		viewer = SudokuSolverComparisonViewer()
		viewer.initialize_visual_settings()
		viewer.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		solver_comparison = self
		parameter = "number iterations"
		viewer.view_solver_comparison_of_parameter(
			solver_comparison,
			parameter,
			*args,
			**kwargs)

	def view_comparison_of_solver_back_tracks(self, *args, **kwargs):
		viewer = SudokuSolverComparisonViewer()
		viewer.initialize_visual_settings()
		viewer.update_save_directory(
			path_to_save_directory=self.visual_settings.path_to_save_directory)
		solver_comparison = self
		parameter = "number back-tracks"
		viewer.view_solver_comparison_of_parameter(
			solver_comparison,
			parameter,
			*args,
			**kwargs)

##