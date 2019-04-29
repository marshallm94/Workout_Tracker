from src import Person
import pickle

if __name__ == "__main__":

	test = Person(str(input("What is your name? ")))

	add_split = True
	while add_split:

		add_split = str(input("What would you like to call this split? "))

		if add_split == 'STOP':
			add_split = False
		else:
			test.add_split(add_split)

	filename = str(input("name of file? "))
	with open(f'users/{filename}.pickle', 'wb') as tmp:
		pickle.dump(test, tmp)
