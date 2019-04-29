import numpy as np
from .workout import Workout
import copy
import time

class Split(object):

	def __init__(self, name):

		self.split = dict()
		self.create_split()
		self.start_date = time.ctime()
		self.name = name

	def create_split(self):

		while True:

			usr_input = str(input("Would you like to add a workout (y/n)? "))

			if usr_input == 'y':

				name = str(input("Workout name: "))
				self.split[name] = list()
				self.split[name].append(Workout(name))
				self.split[name][0].create_routine()

				print("\nCurrent split:\n", self.__str__())

			elif usr_input == 'n':
				break

	def start_workout(self, workout_name):

		if len(self.split[workout_name]) > 1:

			previous_values = self._show_previous_values(workout_name)

			self.split[workout_name][-1].start_workout(previous_values)

		elif len(self.split[workout_name]) == 1:

			self.split[workout_name][-1].start_workout()

		self._copy_previous_workout(workout_name)

	def _copy_previous_workout(self, workout_name):

		next_workout = copy.deepcopy(self.split[workout_name][-1])
		
		# setting the weight and rep matrices of what will be the next workout to zero	
		for exercise in next_workout.routine:

			exercise._reset_matrices()

		self.split[workout_name].append(next_workout)

	def _show_previous_values(self, workout_name):

		out = list()

		for exercise in self.split[workout_name][-2].routine:

			previous_weights = exercise.weight_matrix
			previous_reps = exercise.rep_matrix

			exercise_weights = list()
			for i in range(previous_weights.shape[1]):

				exercise_weights.append(f"{previous_weights[0,i]} x {previous_reps[0,i]}")

			out.append(exercise_weights)
		
		return out

	def __str__(self):

		out = "\n"
		for name, workout_list in self.split.items():

			last_workout = workout_list[-1]
			out += name + f" | {last_workout._get_total_sets()} sets\n=========="
			out += "\t" + last_workout + "\n"

		return out

	def __len__(self):

		return len(self.split)

	def __getitem__(self, key):

		return self.split[key]
