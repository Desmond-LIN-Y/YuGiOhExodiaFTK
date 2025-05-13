import pandas as pd
import numpy as np
from sklearn.metrics import (
	root_mean_squared_error,
	mean_absolute_error,
	mean_absolute_percentage_error
)

def compute_metrics(y_true, y_est, y_low, y_high):
	"""
	Compute RMSE, MAE, and coverage for given true values, estimates, and interval bounds.
	"""
	pass

def process_variable_metrics(var, data_eval, data_est):
	"""
	Compute metrics for a single variable across its categories and overall.
	"""
	pass


def aggregate_metrics(data_eval, data_est):
	"""
	Aggregate metrics for all variables and categories, and compute overall metrics.
	"""
	pass
	
class ModelEvaluator:
	"""Class for evaluating model accuracy.
	
	Parameters
	----------
	summariser : ModelSummariser
			A model summariser instance
			
	data_eval : tuple
			A tuple containing the dictionaries of true contact intensity and marginal contact intensity values
	""" 
	def __init__(self, summariser, cint_matrices_true: dict):
		pass
	
	def evaluate_cint(self):
		"""Evaluate the posterior contact intensity.
		Calculates the RMSE, MAE, MAPE, and 95% posterior coverage.
		
		Returns
		-------
		pd.DataFrame
				A DataFrame containing the metrics summary
		"""
		pass
	
	def evaluate_mcint(self):
		"""Evaluate the posterior marginal contact intensity.
		Calculates the RMSE, MAE, MAPE, and 95% posterior coverage.
		
		Returns
		-------
		pd.DataFrame
				A DataFrame containing the metrics summary
		"""
		pass
		