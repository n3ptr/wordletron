# wordletron

A bot that does the wordle

Wordle became wildly popular at the end of 2021 and after having fun playing the game,  I thought the next fun I would have would be to automate and try to optimise the game-play.

The effort in this bot is broken down into two phases:

Part 1. data exploration
1. what words are compatible how large is this dataset?
2. of the acceptable words, which one is the best to start with?
    * this portion itself seemed to be a popular challenge among developers and the data savvy.
    * my attempt goes through two steps
        1. creating a ranking of the words based on the frequency of letters in the five positions, and create a value set from adding the letters and position information together
        2. the more intensive attempt is to check each word against all other words for how many matches it would generate as a starting word. This gives more value to direct matches, and less value to partial matches to create this map. 

Part 2. the bot
1. pull in our dataset, and pick a starting word
2. navigate to [powerlanguage.co.uk/wordle](https://www.nytimes.com/games/wordle/index.html "or now https://www.nytimes.com/games/wordle/index.html")

3. write and read from the site the site to enter our words


# Using this bot

1. You will need to install the python packages listed in the Pipfile
2. Have firefox installed
3. The dataset that the bot.py file uses is contained within the repo, and if the dependencies are in place it will run. 
    * note that there is a larger dataset that is not included in this repo. It exceeds the file size for github, but can be generated with the check_all_solution_v_guesses.ipynb if you would like.
