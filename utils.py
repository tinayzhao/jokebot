'''An assortment of general useful helper functions'''

import sys

def deliver_error_message(msg):
	'''Prints an error message and ends the program.

	Args:
		msg: a message string
	Returns: None

	Used when encountering an error. 
	'''
	print(msg)
	sys.exit(0)