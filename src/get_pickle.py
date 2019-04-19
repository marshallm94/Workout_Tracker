import pickle

if __name__ == "__main__":

	with open("../data/test.pickle", "rb") as tmp:
		test = pickle.load(tmp)

	print(test)
