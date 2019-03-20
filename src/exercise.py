import numpy as np

class Exercise(object):

	def __init__(self, name, number_sets, target_reps):
	
		self.name = name
		self.number_sets = number_sets
		self.target_reps = target_reps
		self.weight_matrix = np.zeros((1, number_sets))
		self.rep_matrix = np.zeros((1, number_sets))

	def add_set(self, set_number, weight, reps):
		
		self.weight_matrix[set_number - 1] = weight
		self.rep_matrix[set_number - 1] = reps

	def __str__(self):

		out = f"""{self.name} | {self.number_sets} Sets | {self.target_reps} Reps"""
		return out

	def __add__(self, other):

		if isinstance(other, str):

			return self.__str__() + other			

	def __radd__(self, other):

		if isinstance(other, str):

			return other + self.__str__()
