import numpy as np

class Exercise(object):

	def __init__(self, name, number_sets, target_reps):
	
		self.name = name
		self.number_sets = number_sets
		self.targe_reps = target_reps
		self.weight_matrix = np.zeros((1, number_sets))
		self.rep_mnatrix = np.zeros((1, number_sets))

	def add_set(self, set_number, weight, reps):
		
		self.weight_matrix[set_number - 1] = weight
		self.rep_matrix[set_number - 1] = reps			
