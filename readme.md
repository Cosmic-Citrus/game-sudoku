# Repo:    game-sudoku

The purpose of this code is to solve sudoku puzzles and play via graphical user interface.

## Description

Sudoku puzzles are categorized into the following difficulty levels:

* `"easy"`

* `"medium"`

* `"hard"`

* `"expert"`

* `"worlds toughest puzzle"` (according to [sudoku2](https://sudoku2.com/play-the-hardest-sudoku-in-the-world/))

Each of these preset boards can be transformed by:

* rotating the board

* swapping bands of unique rows 

* swapping bands of unique columns

* reflecting the board horizontally

* reflecting the board vertically

* mapping each character to another character

These boards can be solved using a variety of methods. The `"depth-first search"` solver - which attempts to fill each empty cell from a sequential pool of possible values and back-tracks when necessary - is guaranteed to find a solution in non-optimal time (assuming the threshold recursion depth is not exceeded). One optimization to improve the search time is the `"ascending-size search"` method, which selects the next empty cell to fill by finding the empty cell for which the number of possible values is the minimum of all cells; this saves time because it reduces the number of potential mistakes and back-tracks. The plot below shows a time-comparison of these methods.

![example-solver_comparison](output/example_04-sudoku_solver_comparison/SudokuSolverComparison_Elapsed-Seconds_DepthFirstSearch_AscSizeSearch_E_M_H_XwData_wStats_.png)

## Getting Started

### Dependencies

* Python 3.9.6
* numpy == 1.26.4
* matplotlib == 3.9.4
* time (default)

### Executing program

* Download this repository to your local computer

* Create and solve a sudoku puzzle by running the following scripts
  
  * `src/example_01-solve_sudoku_by_depth_first_search.py`
  
  * `src/example_02-solve_sudoku_by_ascending_size_search.py`

* To view a comparison of solver methods, modify `path_to_save_directory` in `src/example_04-sudoku_solver_comparison` and then run the script

## Version History

* 0.1
  * Initial Release

## To-Do
* add `"dancing links"` solver method
* add `"diophantine system of equations"` solver method
* the `"worlds toughest puzzle"` is actually the third toughest puzzle in the world - at least according to [sudokuwiki.org](https://www.sudokuwiki.org/Arto_Inkala_Sudoku); verify that these puzzles have unique solutions and implement them if so
* add gui via `pygame`

## License

This project is licensed under the Apache License - see the LICENSE file for details.
