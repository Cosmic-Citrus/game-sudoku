from plotter_base_configuration import BasePlotterConfiguration
import numpy as np
import matplotlib.pyplot as plt



class BaseSudokuSolverComparisonViewer(BasePlotterConfiguration):

	def __init__(self):
		super().__init__()

	@staticmethod
	def get_difficulty_levels(solver_comparison, is_include_easy, is_include_medium, is_include_hard, is_include_expert, is_include_worlds_toughest_puzzle):
		if not isinstance(is_include_easy, bool):
			raise ValueError("invalid type(is_include_easy): {}".format(type(is_include_easy)))
		if not isinstance(is_include_medium, bool):
			raise ValueError("invalid type(is_include_medium): {}".format(type(is_include_medium)))
		if not isinstance(is_include_hard, bool):
			raise ValueError("invalid type(is_include_hard): {}".format(type(is_include_hard)))
		if not isinstance(is_include_expert, bool):
			raise ValueError("invalid type(is_include_expert): {}".format(type(is_include_expert)))
		if not isinstance(is_include_worlds_toughest_puzzle, bool):
			raise ValueError("invalid type(is_include_worlds_toughest_puzzle): {}".format(type(is_include_worlds_toughest_puzzle)))
		difficulty_levels = list()
		if is_include_easy:
			difficulty_levels.append(
				"easy")
		if is_include_medium:
			difficulty_levels.append(
				"medium")
		if is_include_hard:
			difficulty_levels.append(
				"hard")
		if is_include_expert:
			difficulty_levels.append(
				"expert")		
		if is_include_worlds_toughest_puzzle:
			if "worlds toughest puzzle" not in solver_comparison.selectable_difficulty_levels:
				raise ValueError("solver_comparison does not contain 'worlds toughest puzzle' difficulty")
			difficulty_levels.append(
				"worlds toughest puzzle")
		difficulty_levels = tuple(
			difficulty_levels)
		number_difficulty_levels = len(
			difficulty_levels)
		if number_difficulty_levels == 0:
			raise ValueError("zero difficulty_levels selected")
		return difficulty_levels, number_difficulty_levels

	@staticmethod
	def get_solver_sub_methods(solver_comparison, is_include_depth_first_search, is_include_ascending_size_search, is_include_descending_frequency_search, is_include_adaptive_search, is_include_dancing_links):
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
		solver_sub_methods = list()
		if is_include_depth_first_search:
			if "depth-first search" not in solver_comparison.selectable_solver_sub_methods:
				raise ValueError("depth-first search solver is not initialized in solver_comparison.selectable_solver_sub_methods")
			solver_sub_methods.append(
				"depth-first search")
		if is_include_ascending_size_search:
			if "ascending-size search" not in solver_comparison.selectable_solver_sub_methods:
				raise ValueError("ascending-size search solver is not initialized in solver_comparison.selectable_solver_sub_methods")
			solver_sub_methods.append(
				"ascending-size search")
		if is_include_descending_frequency_search:
			if "descending-frequency search" not in solver_comparison.selectable_solver_sub_methods:
				raise ValueError("descending-frequency search solver is not initialized in solver_comparison.selectable_solver_sub_methods")
			solver_sub_methods.append(
				"descending-frequency search")
		if is_include_adaptive_search:
			if "adaptive search" not in solver_comparison.selectable_solver_sub_methods:
				raise ValueError("daptive search solver is not initialized in solver_comparison.selectable_solver_sub_methods")
			solver_sub_methods.append(
				"adaptive search")
		if is_include_dancing_links:
			if "dancing links" not in solver_comparison.selectable_solver_sub_methods:
				raise ValueError("dancing links solver is not initialized in solver_comparison.selectable_solver_sub_methods")
			solver_sub_methods.append(
				"dancing links")
		solver_sub_methods = tuple(
			solver_sub_methods)
		number_solver_sub_methods = len(
			solver_sub_methods)
		if number_solver_sub_methods == 0:
			raise ValueError("zero solver_sub_methods selected")
		return solver_sub_methods, number_solver_sub_methods

	@staticmethod
	def get_x(solver_comparison):
		x = np.array(
			list(
				range(
					solver_comparison.number_runs_per_solver)))
		return x

	@staticmethod
	def get_save_name(parameter, is_include_depth_first_search, is_include_ascending_size_search, is_include_descending_frequency_search, is_include_adaptive_search, is_include_dancing_links, is_include_easy, is_include_medium, is_include_hard, is_include_expert, is_include_worlds_toughest_puzzle, is_show_data, is_show_statistics, is_save):
		if is_save:
			solver_sub_methods_abbreviations = list()
			if is_include_depth_first_search:
				solver_sub_methods_abbreviations.append(
					"DepthFirstSearch")
			if is_include_ascending_size_search:
				solver_sub_methods_abbreviations.append(
					"AscSizeSearch")
			if is_include_descending_frequency_search:
				solver_sub_methods_abbreviations.append(
					"DescFreqSearch")
			if is_include_adaptive_search:
				solver_sub_methods_abbreviations.append(
					"AdaptiveSearch")
			if is_include_dancing_links:
				solver_sub_methods_abbreviations.append(
					"DancingLinks")
			combined_solver_sub_method_abbreviations = "_".join(
				solver_sub_methods_abbreviations)
			difficulty_level_abbreviations = list()
			if is_include_easy:
				difficulty_level_abbreviations.append(
					"E")
			if is_include_medium:
				difficulty_level_abbreviations.append(
					"M")
			if is_include_hard:
				difficulty_level_abbreviations.append(
					"H")
			if is_include_expert:
				difficulty_level_abbreviations.append(
					"X")
			if is_include_worlds_toughest_puzzle:
				difficulty_level_abbreviations.append(
					"Wtp")
			combined_difficulty_level_abbreviations = "_".join(
				difficulty_level_abbreviations)
			save_name = "SudokuSolverComparison_{}_{}_{}".format(
				parameter.title().replace(
					" ",
					"-"),
				combined_solver_sub_method_abbreviations,
				combined_difficulty_level_abbreviations)
			if is_show_data:
				save_name += "wData_"
			if is_show_statistics:
				save_name += "wStats_"
		else:
			save_name = None
		return save_name

	def plot_data(self, ax, solver_comparison, solver_sub_method, parameter, difficulty_level, runs_color, is_label=False):
		if is_label:
			label = "{:,} Runs per Solver".format(
				solver_comparison.number_runs_per_solver)
		else:
			label = None
		x = self.get_x(
			solver_comparison=solver_comparison)
		y = np.copy(
			solver_comparison.comparison_information["data"][difficulty_level][solver_sub_method][parameter])
		if y.dtype == bool:
			modified_y = np.full(
				fill_value=0,
				shape=y.shape,
				dtype=float)
			modified_y[y] = 100 ## 1 * 100% = 100%
		else:
			modified_y = y
		ylim = (
			np.min(
				modified_y),
			np.max(
				modified_y))
		ax.plot(
			x,
			modified_y,
			color=runs_color,
			label=label,
			marker=".")
		return ax, ylim

	def plot_statistics(self, ax, solver_comparison, solver_sub_method, parameter, difficulty_level, mean_color, median_color, interval_color, bounds_color, is_label=False):
		statistic_names_and_respective_colors = (
			("mean", mean_color),
			("median", median_color),
			("interval", interval_color),
			("bounds", bounds_color),
			)
		statistics = dict(
			solver_comparison.comparison_information["statistics"][difficulty_level][solver_sub_method][parameter])
		x = self.get_x(
			solver_comparison=solver_comparison)
		for statistic_name_and_respective_color in statistic_names_and_respective_colors:
			(statistic_name, statistic_color) = statistic_name_and_respective_color
			if statistic_name in ("mean", "median"):
				y = statistics[statistic_name]
				if is_label:
					label = statistic_name.title()
				else:
					label = None
				ax.axhline(
					y,
					color=statistic_color,
					label=label,
					linestyle="--")
			elif statistic_name == "interval":
				y = (
					statistics["mean"] + statistics["standard deviation"],
					statistics["mean"] - statistics["standard deviation"])
				if is_label:
					label = r"Mean $\pm$ Standard Deviation"
				else:
					label = None
				ax.fill_between(
					(x[0], x[-1]),
					(y[0], y[0]),
					(y[-1], y[-1]),
					step="mid",
					color=statistic_color,
					alpha=0.3,
					label=label)
			elif statistic_name == "bounds":
				for index_at_bound, bound_name in enumerate(["minimum", "maximum"]):
					y = statistics[bound_name]
					if (is_label) and (index_at_bound == 0):
						label = "Min/Max"
					else:
						label = None
					ax.axhline(
						y,
						color=statistic_color,
						label=label,
						linestyle="--")
			else:
				raise ValueError("invalid statistic_name: {}".format(statistic_name))
		ylim = (
			np.min(
				y),
			np.max(
				y))
		return ax, ylim

	def autoformat_axes(self, axes, solver_comparison, parameter, ylim, number_solver_sub_methods, number_difficulty_levels):
		for ax in axes.ravel():
			ax = self.autoformat_ax(
				ax=ax,
				solver_comparison=solver_comparison,
				parameter=parameter,
				ylim=ylim)
		if (number_solver_sub_methods > 1) and (number_difficulty_levels > 1):
			for ax in axes[:-1, :].ravel():
				ax = self.autoformat_null_x_axis_ticks_and_labels(
					ax=ax)
			for ax in axes[:, 1:].ravel():
				ax = self.autoformat_null_y_axis_ticks_and_labels(
					ax=ax)
		elif (number_solver_sub_methods > 1) and (number_difficulty_levels == 1):
			for ax in axes[:-1].ravel():
				ax = self.autoformat_null_x_axis_ticks_and_labels(
					ax=ax)				
		elif (number_solver_sub_methods == 1) and (number_difficulty_levels > 1):
			for ax in axes[1:].ravel():
				ax = self.autoformat_null_y_axis_ticks_and_labels(
					ax=ax)				
		else:
			raise ValueError("number_solver_sub_methods={} and number_difficulty_levels={} means that self.autoformat_ax should be called instead of this method".format(number_solver_sub_methods, number_difficulty_levels))
		return axes

	def autoformat_ax(self, ax, solver_comparison, parameter, ylim, title=None):
		x = self.get_x(
			solver_comparison=solver_comparison)
		x_minor_ticks = x[1::2]
		x_major_ticks = x[::2]
		x_major_fmt = lambda p : r"{:,}".format(
			int(
				p))
		xlim = (
			np.min(
				x),
			np.max(
				x))
		xlabel = "Runs"
		if parameter == "is solved":
			y = np.array(
				list(
					range(
						0,
						101,
						10)))
			y_minor_ticks = y[1::2]
			y_major_ticks = y[::2]
			y_major_fmt = lambda p : r"{:,}".format(
				int(
					p))
			ylabel = "Percentage of Puzzles Solved"
		else:
			(minimum_y, maximum_y) = ylim
			modified_minimum_y = 0
			if maximum_y > 1:
				if maximum_y >= 100:
					if maximum_y >= 1e6:
						y_spacing = int(
							int(maximum_y - minimum_y) / 5)
						# y_spacing = int(
						# 	10 * np.sqrt(
						# 		(maximum_y - minimum_y)))
						# y_spacing = int(
						# 	1e4)
						modified_minimum_y = int(
							np.floor(minimum_y / y_spacing) * y_spacing)
					elif maximum_y >= 1e3:
						y_spacing = 100
					else:
						y_spacing = 10
				else:
					y_spacing = 1
				modified_maximum_y = int(
					np.ceil(maximum_y / y_spacing) * y_spacing)
				y = np.array(
					list(
						range(
							modified_minimum_y,
							modified_maximum_y,
							y_spacing)))
				y_major_fmt = lambda p : r"{:,}".format(
					int(
						p))
			else:
				y = np.linspace(
					0,
					1,
					11,)
				y_major_fmt = lambda p : r"{:,.2f}".format(
					p)
			y_minor_ticks = y[1::2]
			y_major_ticks = y[::2]
			if parameter == "elapsed seconds":
				ylabel = "Elapsed Time (seconds)"
			elif parameter == "number iterations":
				ylabel = "Number of Iterations"
			elif parameter == "number back-tracks":
				ylabel = "Number of Back-tracks"
			else:
				raise ValueError("invalid parameter: {}".format(parameter))
		ax = self.visual_settings.autoformat_axis_ticks_and_ticklabels(
			ax=ax,
			x_minor_ticks=x_minor_ticks,
			x_major_ticks=x_major_ticks,
			x_minor_ticklabels=False,
			x_major_ticklabels=True,
			x_major_fmt=x_major_fmt,
			y_minor_ticks=y_minor_ticks,
			y_major_ticks=y_major_ticks,
			y_minor_ticklabels=False,
			y_major_ticklabels=True,
			y_major_fmt=y_major_fmt)
		ax = self.visual_settings.autoformat_grid(
			ax=ax,
			grid_color="gray",
			grid_alpha=0.3,
			grid_linestyle=":")
		ax = self.visual_settings.autoformat_axis_limits(
			ax=ax,
			xlim=xlim,
			ylim=ylim)
		ax = self.visual_settings.autoformat_axis_labels(
			ax=ax,
			xlabel=xlabel,
			ylabel=ylabel,
			title=title)
		return ax

	def autoformat_null_x_axis_ticks_and_labels(self, ax):
		ax.set_xlabel(
			"",
			fontsize=self.visual_settings.label_size)
		ax.set_xticklabels(
			list(),
			fontsize=self.visual_settings.tick_size)
		return ax

	def autoformat_null_y_axis_ticks_and_labels(self, ax):
		ax.set_ylabel(
			"",
			fontsize=self.visual_settings.label_size)
		ax.set_yticklabels(
			list(),
			fontsize=self.visual_settings.tick_size)
		return ax

class SudokuSolverComparisonViewer(BaseSudokuSolverComparisonViewer):

	def __init__(self):
		super().__init__()

	def view_solver_comparison_of_parameter(self, solver_comparison, parameter, runs_color="black", mean_color="darkorange", median_color="steelblue", interval_color="limegreen", bounds_color="black", offset_y_factor=0.1, is_include_depth_first_search=False, is_include_ascending_size_search=False, is_include_descending_frequency_search=False, is_include_adaptive_search=False, is_include_dancing_links=False, is_include_easy=False, is_include_medium=False, is_include_hard=False, is_include_expert=False, is_include_worlds_toughest_puzzle=False, is_show_data=False, is_show_statistics=False, figsize=None, is_save=False):
		
		def get_ylim_with_extra_space_about_bounds(ylim, offset_y_factor):
			(minimum_y, maximum_y) = ylim
			modified_minimum_y = minimum_y - (minimum_y * offset_y_factor)
			# if modified_minimum_y < 0:
			# 	modified_minimum_y = 0
			modified_maximum_y = maximum_y + (maximum_y * offset_y_factor)
			modified_ylim = (
				modified_minimum_y,
				modified_maximum_y)
			return modified_ylim

		def get_ylim_at_solve_status():
			ylim = (
				-5,
				105)
			return ylim

		if not isinstance(is_show_data, bool):
			raise ValueError("invalid type(is_show_data): {}".format(type(is_show_data)))
		if not isinstance(is_show_statistics, bool):
			raise ValueError("invalid type(is_show_statistics): {}".format(type(is_show_statistics)))
		if (not is_show_data) and (not is_show_statistics):
			raise ValueError("invalid combination of is_show_data={} and is_show_statistics={}".format(is_show_data, is_show_statistics))
		if solver_comparison.comparison_information is None:
			raise ValueError("solver_comparison.comparison_information is not initialized")
		difficulty_levels, number_difficulty_levels = self.get_difficulty_levels(
			solver_comparison=solver_comparison,
			is_include_easy=is_include_easy,
			is_include_medium=is_include_medium,
			is_include_hard=is_include_hard,
			is_include_expert=is_include_expert,
			is_include_worlds_toughest_puzzle=is_include_worlds_toughest_puzzle)
		solver_sub_methods, number_solver_sub_methods = self.get_solver_sub_methods(
			solver_comparison=solver_comparison,
			is_include_depth_first_search=is_include_depth_first_search,
			is_include_ascending_size_search=is_include_ascending_size_search,
			is_include_descending_frequency_search=is_include_descending_frequency_search,
			is_include_adaptive_search=is_include_adaptive_search,
			is_include_dancing_links=is_include_dancing_links)
		number_solver_sub_methods = len(
			# solver_comparison.comparison_information["parameters"]["solver sub-methods"])
			solver_comparison.selectable_solver_sub_methods)
		minimum_y, maximum_y = np.inf, -1 * np.inf
		if (number_solver_sub_methods == 1) and (number_difficulty_levels == 1):
			fig, ax = plt.subplots(
				figsize=figsize)
			for difficulty_level in difficulty_levels:
				for solver_sub_method in solver_sub_methods:
					if is_show_data:
						ax, ylim = self.plot_data(
							ax=ax,
							solver_comparison=solver_comparison,
							solver_sub_method=solver_sub_method,
							parameter=parameter,
							difficulty_level=difficulty_level,
							runs_color=runs_color,
							is_label=True)
						if ylim[0] < minimum_y:
							minimum_y = ylim[0]
						if ylim[1] > maximum_y:
							maximum_y = ylim[1]
					if is_show_statistics:
						ax, ylim = self.plot_statistics(
							ax=ax,
							solver_comparison=solver_comparison,
							solver_sub_method=solver_sub_method,
							parameter=parameter,
							difficulty_level=difficulty_level,
							mean_color=mean_color,
							median_color=median_color,
							interval_color=interval_color,
							bounds_color=bounds_color,
							is_label=True)
						if ylim[0] < minimum_y:
							minimum_y = ylim[0]
						if ylim[1] > maximum_y:
							maximum_y = ylim[1]
			if parameter == "is solved":
				modified_ylim = get_ylim_at_solve_status()
			else:
				modified_ylim = (
					minimum_y,
					maximum_y)
			modified_ylim = get_ylim_with_extra_space_about_bounds(
				ylim=modified_ylim,
				offset_y_factor=offset_y_factor)
			ax = self.autoformat_ax(
				ax=ax,
				solver_comparison=solver_comparison,
				parameter=parameter,
				ylim=modified_ylim,
				title=title)
			handles, labels = ax.get_legend_handles_labels()
			leg = self.visual_settings.get_legend(
				fig=fig,
				ax=ax,
				handles=handles,
				labels=labels)
		else:
			fig, axes = plt.subplots(
				figsize=figsize,
				nrows=number_solver_sub_methods,
				ncols=number_difficulty_levels)
			for index_at_difficulty_level, difficulty_level in enumerate(difficulty_levels):
				for index_at_solver_sub_method, solver_sub_method in enumerate(solver_sub_methods):
					if index_at_solver_sub_method == 0:
						title = "{}\n{}".format(
							difficulty_level.title(),
							solver_sub_method.title())
					else:
						title = solver_sub_method.title()
					if (number_solver_sub_methods > 1) and (number_difficulty_levels > 1):
						ax = axes[index_at_solver_sub_method, index_at_difficulty_level]
					elif (number_solver_sub_methods > 1) and (number_difficulty_levels == 1):
						ax = axes[index_at_solver_sub_method]
					elif (number_solver_sub_methods == 1) and (number_difficulty_levels > 1):
						ax = axes[index_at_difficulty_level]
					else:
						raise ValueError("number_solver_sub_methods={} and number_difficulty_levels={} are not compatible".format(number_solver_sub_methods, number_difficulty_levels))
					ax.set_title(
						title,
						fontsize=self.visual_settings.title_size)
					if (index_at_solver_sub_method == 0) and (index_at_difficulty_level == 0):
						is_label = True
					else:
						is_label = False
					if is_show_data:
						ax, ylim = self.plot_data(
							ax=ax,
							solver_comparison=solver_comparison,
							solver_sub_method=solver_sub_method,
							parameter=parameter,
							difficulty_level=difficulty_level,
							runs_color=runs_color,
							is_label=is_label)
						if ylim[0] < minimum_y:
							minimum_y = ylim[0]
						if ylim[1] > maximum_y:
							maximum_y = ylim[1]
					if is_show_statistics:
						ax, ylim = self.plot_statistics(
							ax=ax,
							solver_comparison=solver_comparison,
							solver_sub_method=solver_sub_method,
							parameter=parameter,
							difficulty_level=difficulty_level,
							mean_color=mean_color,
							median_color=median_color,
							interval_color=interval_color,
							bounds_color=bounds_color,
							is_label=is_label)
						if ylim[0] < minimum_y:
							minimum_y = ylim[0]
						if ylim[1] > maximum_y:
							maximum_y = ylim[1]
			if parameter == "is solved":
				modified_ylim = get_ylim_at_solve_status()
			else:
				modified_ylim = (
					minimum_y,
					maximum_y)
			modified_ylim = get_ylim_with_extra_space_about_bounds(
				ylim=modified_ylim,
				offset_y_factor=offset_y_factor)
			axes = self.autoformat_axes(
				axes=axes,
				solver_comparison=solver_comparison,
				parameter=parameter,
				ylim=modified_ylim,
				number_solver_sub_methods=number_solver_sub_methods,
				number_difficulty_levels=number_difficulty_levels)
			ax = axes.ravel()[0]
			handles, labels = ax.get_legend_handles_labels()
			leg = self.visual_settings.get_legend(
				fig=fig,
				ax=ax,
				handles=handles,
				labels=labels)
		fig.suptitle(
			"Sudoku Solver Comparison",
			fontsize=self.visual_settings.title_size)
		save_name = self.get_save_name(
			parameter=parameter,
			is_include_depth_first_search=is_include_depth_first_search,
			is_include_ascending_size_search=is_include_ascending_size_search,
			is_include_descending_frequency_search=is_include_descending_frequency_search,
			is_include_adaptive_search=is_include_adaptive_search,
			is_include_dancing_links=is_include_dancing_links,
			is_include_easy=is_include_easy,
			is_include_medium=is_include_medium,
			is_include_hard=is_include_hard,
			is_include_expert=is_include_expert,
			is_include_worlds_toughest_puzzle=is_include_worlds_toughest_puzzle,
			is_show_data=is_show_data,
			is_show_statistics=is_show_statistics,
			is_save=is_save)
		self.visual_settings.display_image(
			fig=fig,
			save_name=save_name)

##