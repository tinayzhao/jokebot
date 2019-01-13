'''Main file for running jokebot.

Run python jokebot.py for joke to deliver jokes taken from Reddit.
Run python jokebot.py file_name.csv to deliver jokes from the given CSV file.
'''

import sys
import time

from csv_jokes import get_csv_jokes
from reddit_jokes import get_reddit_jokes
from utils import deliver_error_message

def main():
	jokes_list = get_jokes()
	num_deliv_jokes = 0 #tracks the number of jokes delievered
	for joke in jokes_list:
		deliver_joke(joke[0], joke[1])
		num_deliv_jokes += 1
		if num_deliv_jokes != len(jokes_list) and not read_user_input(): #checks for last joke and user inputs
			break

def deliver_joke(prompt, punchline):
	''' Delivers the prompt and punchline of a joke.

	Skips jokes with no prompt or no punchline.
	
	Args: 
		prompt: string for joke setup
		punchline: string for joke punchline of the joke
	Returns: None
	'''
	if prompt and punchline:
		print(prompt)
		time.sleep(2)
		print(punchline)

def read_user_input():
	'''Prompts for and responds to user input. 

	Encourages user to input readable commands. 

	Args: None

	Returns: 
		A boolean value. 
		True if user responds with 'next'. False if response is 'quit'.
		Otherwise, prints 'I don't understand' and prompts again. 

	'''
	while True:
		time.sleep(1) #delays prompt by 1 second
		response = input("Type next for another joke and quit to stop. \n")
		if response == "next":
			return True
		elif response == "quit":
			return False
		else:
			print("I don't understand.")


def get_jokes(): 
	'''Interprets command line arguments to obtain jokes. 

	Args: None
	Returns:
		List of tuples containing the prompt and punchline. 
		The first item is the prompt. The second item is the punchline.
	'''
	if len(sys.argv) == 1:
		jokes_list = get_reddit_jokes()
	elif len(sys.argv) == 2:
		jokes_list = get_csv_jokes(sys.argv[1])
	else:
		deliver_error_message("Unable to interpret command.")
	if not jokes_list:
			deliver_error_message("No jokes available.")
	return jokes_list


if __name__ == "__main__":
	main()



