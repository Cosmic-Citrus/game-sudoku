from solver_base_configuration import BaseSudokuSolverConfiguration
import numpy as np
from time import perf_counter


class BaseSudokuSolverByDancingLinksConfiguration(BaseSudokuSolverConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)


class SudokuSolverByDancingLinksConfiguration(BaseSudokuSolverByDancingLinksConfiguration):

	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			**kwargs)

	def initialize_solver(self):
		raise ValueError("not yet implemented")

	def solve(self, *args, is_suppress_errors=False, **kwargs):
		raise ValueError("not yet implemented")


##