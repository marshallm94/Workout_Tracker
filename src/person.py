import numpy as np
from split import Split

class Person(object):

	def __init__(self, name):

		self.name = name
		self.splits = dict()

	def add_split(self, name):

		self.splits[name] = Split(name)	
