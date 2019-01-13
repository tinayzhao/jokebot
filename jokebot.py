import time, csv, sys, requests, os

#main function
def run_jokebot():
	jokes_list = get_jokes()
	num_deliv_jokes = 0
	for joke in jokes_list:
		deliver_joke(joke[0], joke[1])
		num_deliv_jokes += 1
		if num_deliv_jokes != len(jokes_list) and not read_input():
			break

#returns a list of jokes depending on command line args
def get_jokes(): 
	if len(sys.argv) == 1:
		jokes_list = reddit_jokes()
	else:
		csv_file = sys.argv[1]
		if not os.path.isfile(csv_file):
			print("Cannot find joke file in current directory")
			sys.exit(0)
		jokes_list = read_csv(csv_file)
		if not jokes_list:
			print("Unable to read CSV file")
			sys.exit(0)
	return jokes_list

#helper function that reads CSV file and returns list of tuples
#returns False if file is corrupted
def read_csv(file_name):
	try:
		with open(file_name) as csv_file:
			table = csv.reader(csv_file, delimiter=',')
			return [(row[0], row[1]) for row in table]
	except:
		return False

#times the delivery of prompt and punchline 
#if prompt/punchline are missing, skip line
def deliver_joke(prompt, punchline):
	if prompt:
		print(prompt)
		if punchline:
			time.sleep(2)
	if punchline:
		print(punchline)

#reads user input
def read_input():
	while True:
		time.sleep(1)
		response = input("Type next for another joke and quit to stop. \n")
		if response == "next":
			return True
		elif response == "quit":
			return False
		else:
			print("I don't understand.")

#returns list of dad jokes from Reddit
#filters out over 18 jokes and ensures joke is a question
def reddit_jokes():
	json_dict = requests.get("https://www.reddit.com/r/dadjokes.json", headers = {'User-agent': 'jokebot'}).json()
	title_list = ['how','why','what']
	return [(joke['data']['title'], joke['data']['selftext']) for joke in json_dict['data']['children'] if not joke['data']['over_18'] and joke['data']['title'].split(' ')[0].lower() in title_list and not joke['data']['title'].split('?')[-1]]


if __name__ == "__main__":
	run_jokebot()



