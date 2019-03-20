import numpy as np
from workout import Workout
import time

class Split(object):

	def __init__(self, name):

		self.split = list()
		self.create_split()
		self.start_date = time.ctime()
		self.name = name

	def create_split(self):

		while True:

			usr_input = str(input("Would you like to add a workout (y/n)? "))

			if usr_input == 'y':

				name = str(input("Workout name: "))
				self.split.append(Workout(name))

				print("\nCurrent split:", self.__str__())

			elif usr_input == 'n':
				break


	def __str__(self):

		out = "\n"
		for workout in self.split:
			out += workout.name + f" | {workout._get_total_sets()} sets\n=========="
			out += "\t" + workout + "\n"
		return out
	
