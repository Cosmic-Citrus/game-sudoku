from solver_search_configuration import SudokuSolverBySearchConfiguration



if __name__ == "__main__":

	sudoku = SudokuSolverBySearchConfiguration()
	sudoku.initialize_board(
		# board=None,
		difficulty_level="easy",
		is_apply_transform=True,
		random_state_seed=0)

	print(
		sudoku)

	sudoku.solve(
		search_method="depth-first search",
		number_maximum_iterations=1e6,
		is_suppress_errors=False)

	print(
		sudoku)


##