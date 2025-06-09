from solver_search_configuration import SudokuSolverBySearchConfiguration



if __name__ == "__main__":

	sudoku = SudokuSolverBySearchConfiguration(
		is_include_worlds_toughest_puzzle=True)
	sudoku.initialize_board(
		# board=None,
		difficulty_level="worlds toughest puzzle",
		is_apply_transform=True,
		random_state_seed=0)

	print(
		sudoku)

	sudoku.solve(
		search_method="ascending-size search",
		number_maximum_iterations=1e6,
		is_suppress_errors=False)

	print(
		sudoku)


##