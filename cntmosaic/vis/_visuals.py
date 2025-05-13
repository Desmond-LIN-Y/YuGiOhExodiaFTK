import numpy as np
from numpy.typing import NDArray
import pandas as pd
import altair as alt
alt.data_transformers.disable_max_rows()
import matplotlib.pyplot as plt

from ..utils import AgeBins, depixilate
from ._utils import ravel_matrix, generate_vega_expression
from ..preprocess._utils import check_required_columns, expand_age_interval

def plot_mosaic(
	matrix: np.ndarray,
	title: str='Contact pattern',
	xlabel: str='Age of contacting individual',
	ylabel: str='Age of contacted individual',
	zlabel: str=None,
	width: int | float=250,
	height: int | float=250,
 	style_config: dict = None
) -> alt.Chart:
	"""
	Plot a mosaic visualization of a contact matrix.

	Parameters
	----------
	matrix : np.ndarray
			A 2D array representing the contact intensity or rate matrix.
	title : str, optional
			The title of the chart. Default is 'Contact pattern'.
	xlabel : str, optional
			Label for the x-axis. Default is 'Age of contacting individual'.
	ylabel : str, optional
			Label for the y-axis. Default is 'Age of contacted individual'.
	zlabel : str, optional
			Label for the color scale legend. If None, the legend is not displayed.
	width : int, optional
			The width of the chart in pixels. Default is 250.
	height : int, optional
			The height of the chart in pixels. Default is 250.
	style_config : dict, optional
			A dictionary to override default style settings for axes, title, and legend.
			The keys can include 'x_axis', 'y_axis', 'title', and 'legend'.

	Returns
	-------
	alt.Chart
			An Altair Chart object representing the mosaic visualisation of a contact matrix.

	Notes
	-----
	The function flattens the input matrix using `ravel_matrix` to extract the x and y indices along with corresponding values.
	It then constructs a DataFrame and configures the chart properties using default style settings,
	which can be further customized via the `style_config` parameter.
	"""
	# Default configurations for axis, title, and legend
	pass

def plot_mosaic_pixilated(
  matrix: np.ndarray,
  age_bins: AgeBins,
  title: str='Contact pattern',
	xlabel: str='Age of contacting individual',
	ylabel: str='Age of contacted individual',
	zlabel: str=None,
	width: int | float=250,
	height: int | float=250,
  style_config: dict = None
) -> alt.Chart:  
  # Default configurations for axis, title, and legend
	pass

def plot_mosaic_marginal(
  mcint: np.ndarray,
  mcint_lb: np.ndarray = None,
  mcint_ub: np.ndarray = None,
  width: int = 250,
  height: int = 250,
  title: str = 'Contact intensity',
  style_config: dict = None
) -> alt.Chart:
  """
	Plot the marginal contact intensity with optional uncertainty bands.
	
 Parameters
	----------
	mcint : np.ndarray
		Array representing the main contact intensity values.
	mcint_lb : np.ndarray, optional
		Array representing the lower bound of the uncertainty band. If provided, both mcint_lb and mcint_ub are used to
		display an error band around the line plot. Default is None.
	mcint_ub : np.ndarray, optional
		Array representing the upper bound of the uncertainty band. If provided, both mcint_lb and mcint_ub are used to
		display an error band around the line plot. Default is None.
	width : int, optional
		The width of the resulting chart in pixels. Default is 250.
	height : int, optional
		The height of the resulting chart in pixels. Default is 250.
	title : str, optional
		The title for the chart. Default is 'Contact intensity'.
	style_config : dict, optional
		A dictionary for overriding default style configurations for the axes and title. The keys should correspond to the
		configuration parts ('x_axis', 'y_axis', or 'title') and the values should be dictionaries of style parameters.
		Default is None.
  
	Returns
	-------
	alt.Chart
		An Altair Chart object that visualizes the marginal contact intensity. When error bounds are provided, the chart includes
		an error band alongside the main line plot.
	"""
  pass
		
def plot_mosaic_empirical(
		data: pd.DataFrame,
	ax,
	title: str = 'Empirical contact intensity',
	xlabel: str | None = 'Age of contacting individual',
	ylabel: str | None = 'Age of contacted individual',
	vmin: float = None,
	vmax: float = None,
	cbar_ax=None,
	cbar_label: str | None = 'Contact intensity',
	cmap: str = 'Spectral_r'
):
	pass