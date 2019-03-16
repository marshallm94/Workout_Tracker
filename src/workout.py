from Exercise import Exercise
import numpy as np
import time

class Workout(object):

	def __init__(self, name, date):

		self.date = time.ctime()
		self.total_volume = self.get_total_volume()
		self.name = name
		self.routine = list()

	def create_routine(self, name, number_sets, target_reps):

		self.routine.append(Exercise(name, number_sets, target_reps))

	def start_workout(self):

		for exercise in self.routine:
			for i in exercise.number_sets:
				exercise.add_set(i, weight, reps)
				

		

