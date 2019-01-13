import csv 
import os

from utils import deliver_error_message

def get_csv_jokes(csv_file): 
	if csv_file.split(".")[-1] != "csv":
		deliver_error_message("Please reference a CSV file.")
	if not os.path.isfile(csv_file):
		deliver_error_message("Cannot find joke file in current directory.")
	return read_csv(csv_file)


def read_csv(file_name):
	''' Reads jokes from a CSV file.
	
	Args: 
		file_name: String of CSV file name
	Returns:
		List of tuples containing the prompt and punchline. 
		The first item is the prompt. The second item is the punchline.
		example:

		[("Why don't people play cards in the jungle?", "There's too many cheetahs!"), 
			("What is the least spoken language in the world?", "Sign language"),
			("What did the pirate say on his 80th birthday?", "Aye matey!")]

	'''
	try:
		with open(file_name) as csv_file:
			table = csv.reader(csv_file, delimiter=',')
			return [(row[0], row[1]) for row in table if len(row) == 2 and row[0] and row[1]]
	except:
		return False