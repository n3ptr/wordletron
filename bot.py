from english_words import english_words_set
import pandas as pd
import numpy as np
import data as dt

play =''
df_options = dt.df_word_ranks
while play != 'no':
    round = 1
    while round < 6:
        round +=1 
        if round == 1:
            word = input('enter your guess:')
            pass

        # try:
        if round == 2:
            not_char = input('enter eliminated letters:[l,e,t,t,e,r]')
            is_char = input('enter confirmed letters:[y,e,s]')
            loc_letters = input('enter confirmed locations: [letter,location]')

            # eliminate options, and show the reduced best 5 choices
            if len(not_char)>1:
                df_options = dt.remove_notcontains(not_char,dt.df_word_ranks)
                print(df_options.head())
            if len(is_char)>0:
                df_options = dt.remove_by_contains(is_char,df_options)
                print(df_options.head())
            
            if len(loc_letters)>0:
                # remove by letters in correct location
                for i in range(0,int(len(dt.loc_letters)),2):
                    # print(str(i))
                    # print(loc_letters[i])
                    # print(loc_letters[i+1])
                    df_options = dt.remove_by_location(loc=int(loc_letters[i+1]),letter=str(loc_letters[i]),df=df_options)
                print(df_options.head())

        next_best = (df_options['word'][df_options['value'].idxmax()])
        print(next_best)
    # except:
    #     print(word)