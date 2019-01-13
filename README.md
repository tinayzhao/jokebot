# Jokebot
My submisson for the take-home assignment for the Spring 2019 CSM Tech Committee Application.

## Functionality
The purpose of the Jokebot is to deliver prompts and punchlines to the user. Then, the user can type `next` to hear another joke or `quit` to stop the program. If the Jokebot runs out of jokes, the program stops. 

You can run program from the command line with Option 1: `python jokebot.py` or Option 2: `python jokebot.py file_name.csv`. Option 1 reads jokes from /r/dadjokes. Option 2 reads jokes from a provided csv file. The file must be in the same directory as `jokebot.py`.

Read Edge Cases section for more details.

## Edges Cases
### Involving System Arguments
* **Incorrect formatting of CSV file name:** prints "Please reference a CSV file" and ends program
* **More than 2 arguments passed in:** prints "Unable to interpret command" and ends program

### Involving CSV file
* **Does not exist/Not in current directory:** prints "Not in current directory" and ends program
* **Corrupted file/Incorrect format(i.e. empty row, missing columm)/No complete jokes:** prints "Unable to read CSV file" and ends program
* **Empty prompt or punchline:** Skips joke

### Involving Reddit Jokes 
* **No Internet Connection/Changes made to Reddit JSON:** prints "Unable to process jokes from Reddit" and ends program
* **No jokes match guidelines:** prints "No jokes available. Check back later." and ends program

## Resources
* [Jokebot Spec](https://github.com/csmberkeley/tech-comm-takehome-exercise)
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)





