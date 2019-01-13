import requests

from utils import deliver_error_message

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
	json_dict = get_json("https://www.reddit.com/r/dadjokes.json")
	interr_word_list = ['how','why','what', 'is', 'who', 'if', 'when', 'which']
	return [(joke['data']['title'], joke['data']['selftext']) #creates tuple
		for joke in json_dict['data']['children'] #iterates through each Reddit post 
			if not joke['data']['over_18'] #checks if joke is not over 18
			and joke['data']['title'].split(' ')[0].lower() in interr_word_list  #checks for interrogative word
			and not joke['data']['title'].split('?')[-1]] #checks for question mark		


def get_json(url):
	try: 
		res = requests.get(url, headers = {'User-agent': 'jokebot'})
		res.raise_for_status()
		return res.json()
	except: 
		deliver_error_message("Unable to process jokes from {0}".format(url.split('.')[1]))