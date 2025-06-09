from solver_comparison_configuration import SudokuSolverComparisonConfiguration


# path_to_save_directory, is_save = None, False
path_to_save_directory, is_save = "/Users/owner/Desktop/programming/sudoku/output/", True


if __name__ == "__main__":

	sudoku_solver_comparison = SudokuSolverComparisonConfiguration(
		is_include_worlds_toughest_puzzle=False)
	sudoku_solver_comparison.initialize_comparison(
		number_runs_per_solver=10,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_descending_frequency_search=False,
		is_include_adaptive_search=False,
		is_include_dancing_links=False,
		random_state_seed=0)

	sudoku_solver_comparison.initialize_visual_settings()
	sudoku_solver_comparison.update_save_directory(
		path_to_save_directory=path_to_save_directory)
	sudoku_solver_comparison.view_comparison_of_solver_timings(
		is_show_data=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_timings(
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_timings(
		is_show_data=True,
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_successes(
		is_show_data=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_successes(
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_successes(
		is_show_data=True,
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_iterations(
		is_show_data=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_iterations(
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_iterations(
		is_show_data=True,
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_back_tracks(
		is_show_data=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_back_tracks(
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)
	sudoku_solver_comparison.view_comparison_of_solver_back_tracks(
		is_show_data=True,
		is_show_statistics=True,
		is_include_depth_first_search=True,
		is_include_ascending_size_search=True,
		is_include_easy=True,
		is_include_medium=True,
		is_include_hard=True,
		is_include_expert=True,
		figsize=(12, 7),
		is_save=is_save)

##