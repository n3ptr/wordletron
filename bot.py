from english_words import english_words_set
import pandas as pd
import numpy as np
import data as dt


round = 0
df_options = dt.df_word_ranks

print('strongest suggestions')
print(df_options.nlargest(3, 'value'))

while round <= 6:
    round += 1 
    if round == 1:

        print('initial guess')
        word = input('enter your guess:')
        pass

    if round > 1:

        not_char = input('enter eliminated letters:[l,e,t,t,e,r]')
        is_char = input('enter confirmed letters:[y,e,s]')
        loc_letters = input('enter confirmed locations: [letter,location]')

        # eliminate options, and show the reduced best 5 choices
        if len(not_char)>0:
            df_options = dt.remove_notcontains(not_char,df_options)

        if len(is_char)>0:
            df_options = dt.remove_by_contains(is_char,df_options)

        if len(loc_letters)>0:
            # remove by letters in correct location
            for i in range(0,int(len(loc_letters)),2):
                df_options = dt.remove_by_location(loc=int(loc_letters[i+1]),letter=str(loc_letters[i]),df=df_options)

        
        next_best = (df_options['word'][df_options['value'].idxmax()])
        print('from the results of the last guess')
        print('next best option is ' + str(next_best))
        print('your top remaiing options are: ')
        print(df_options.head(3))

    print(str(round))
