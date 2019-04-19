import pickle
from src import Exercise, Workout, Split, Person

if __name__ == "__main__":

	filename = str(input("What is the filename you would like to use? "))

	with open(filename, "rb") as tmp:
		test = pickle.load(tmp)

	print(test)
