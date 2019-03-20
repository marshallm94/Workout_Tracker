from exercise import Exercise
import numpy as np
import time

class Workout(object):

	def __init__(self, name):
	
		self.routine = list()
		self.create_routine()
		self.date = time.ctime()
		self.total_volume = self.get_total_volume()
		self.name = name

	def add_exercise(self, name, number_sets, target_reps):

		self.routine.append(Exercise(name, number_sets, target_reps))	

	def create_routine(self):

		while True:

			usr_input = str(input("Would you like to add an exercise (y/n)? "))

			if usr_input == 'y':

				name = str(input("Exercise name: "))
				number_sets = int(input("Number of sets: "))
				target_reps = int(input("Target number of reps: "))

				self.add_exercise(name, number_sets, target_reps)

				print(f"\nCurrent workout: Total sets = {self._get_total_sets()}", self.__str__())

			elif usr_input == 'n':
				break

	def start_workout(self):

		for exercise in self.routine:
			for i in exercise.number_sets:
				exercise.add_set(i, weight, reps)

	def get_total_volume(self):
		pass

	def _get_total_sets(self):

		out = 0

		for exercise in self.routine:
			out += exercise.number_sets

		return out

	def __str__(self):

		out = "\n"
		for exercise in self.routine:
			out += exercise + "\n"
		return out

	def __add__(self, other):

		if isinstance(other, str):

			return self.__str__() + other

	def __radd__(self, other):

		if isinstance(other, str):

			return other + self.__str__()



