import numpy as np
from .split import Split

class Person(object):

	def __init__(self, name):

		self.name = name
		self.splits = dict()

	def add_split(self, name):

		self.splits[name] = Split(name)	

	def __str__(self):

		out = f"{self.name}'s splits\n==========\n"
		for split_name, split in self.splits.items():

			out += split_name + "\n==========\n" + split.__str__()

		return out

			
