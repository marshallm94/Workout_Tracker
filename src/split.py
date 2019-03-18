import numpy as np
from exercise import Exercise
from workout import Workout
import time

class Split(object):

	def __init__(self):

		self.start_date = time.ctime()
		self.split = list()

	def create_split(self):

		self.split.append(Workout(name))
		
