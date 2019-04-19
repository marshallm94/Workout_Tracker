from src import Person
import pickle

if __name__ == "__main__":

	test = Person(str(input("What is your name? ")))
	test.add_split(str(input("What would you like to call this split? ")))

	filename = str(input("name of file? "))
	with open(f'users/{filename}.pickle', 'wb') as tmp:
		pickle.dump(test, tmp)
