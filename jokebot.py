import csv
import os
import requests
import sys
import time


#main function
def main():
	jokes_list = get_jokes()
	num_deliv_jokes = 0 #tracks the number of jokes delievered
	for joke in jokes_list:
		deliver_joke(joke[0], joke[1])
		num_deliv_jokes += 1
		if num_deliv_jokes != len(jokes_list) and not read_user_input(): #stops prompting the user after delivering the last joke
			break

def deliver_error_message(msg):
	print(msg)
	sys.exit(0)

#returns a list of jokes depending on command line args
def get_jokes(): 
	'''Interprets command line arguments to obtain jokes. 

	Args: None
	Returns:
		List of jokes.
	'''
	if len(sys.argv) == 1:
		jokes_list = reddit_jokes()
		if not jokes_list:
			deliver_error_message("No jokes available. Check back later.")
	elif len(sys.argv) == 2:
		jokes_list = csv_jokes()
		if not jokes_list:
			deliver_error_message("Unable to read CSV file.")
	else:
		deliver_error_message("Unable to interpret command.")
	return jokes_list

def csv_jokes(): 
	csv_file = sys.argv[1]
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

def deliver_joke(prompt, punchline):
	''' Delivers the prompt and punchline of a joke.
	
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
		time.sleep(1)
		response = input("Type next for another joke and quit to stop. \n")
		if response == "next":
			return True
		elif response == "quit":
			return False
		else:
			print("I don't understand.")

def reddit_jokes():
	''' Filters out and returns a list of dad jokes for /r/dadjokes. 

	Filter guidelines: 
		1. Joke is not intended for an over 18 audience. 
		2. Prompt is a question.
			a. First word is a common interrogative word
			b. Ends with a question mark

	Args: None
	Returns:
		A list of tuples containing the prompt and the punchline of the joke. 
		The first item is the prompt. The second item is the punchline.
		example:

			[("What is brown and sticky?", "A stick."), 
			("What do you call an elephant that doesn't matter?", "An irrelephant."),
			("What do you call a man with a rubber toe?", "Roberto.")]
	'''
	try:
		json_dict = requests.get("https://www.reddit.com/r/dadjokes.json", headers = {'User-agent': 'jokebot'}).json()
		interr_word_list = ['how','why','what', 'is', 'who', 'if', 'when', 'which']
		return [(joke['data']['title'], joke['data']['selftext']) 
			for joke in json_dict['data']['children'] #iterates through each Reddit post 
				if not joke['data']['over_18'] #checks if joke is not over 18
				and joke['data']['title'].split(' ')[0].lower() in interr_word_list  #checks for interrogative word
				and not joke['data']['title'].split('?')[-1]] #checks for question mark
	except: 
		deliver_error_message("Unable to process jokes from Reddit")


if __name__ == "__main__":
	main()



