'''Functions used for processing jokes from a CSV file.'''

import csv 
import os

from utils import deliver_error_message

def get_csv_jokes(csv_file):
	'''Obtain CSV jokes file.
	
	Args:
		csv_file: String name of csv_file
	Returns: See 'Returns' of the read_csv function. 
	'''
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
	'''
	try:
		with open(file_name) as csv_file:
			table = csv.reader(csv_file, delimiter=',')
			return [(row[0], row[1]) for row in table if len(row) == 2 and row[0] and row[1]]
	except:
		deliver_error_message("Unable to read CSV file")