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

	def __getitem__(self, key):

		return self.splits[key]

	def __iter__(self):

		return iter(self.splits.values())

	def keys(self):

		return self.splits.keys()

	def items(self):

		return self.splits.items()

	def values(self):

		return self.splits.values()
