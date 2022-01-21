from english_words import english_words_set
import pandas as pd
import numpy as np

# make a list of 5 lenght words without non-alphas, and no proper nouns
words5 = []

for word in english_words_set:
    if len(word) == 5 and word[0].islower() and word.isalpha():
        words5.append(word)

df_words = pd.DataFrame(words5)
df_words.columns=['words']

df_words['first'] = df_words['words'].str.slice(0,1)
df_words['second'] = df_words['words'].str.slice(1,2)
df_words['third'] = df_words['words'].str.slice(2,3)
df_words['fourth'] = df_words['words'].str.slice(3,4)
df_words['fifth'] = df_words['words'].str.slice(4,5)


aplhas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dfalpha = pd.DataFrame(aplhas)
dfalpha.columns = ['letters']
dfalpha.set_index('letters', inplace=True)

# build the frequerncy table from each smaller dataframe
df_counts = df_words['first'].value_counts()
df_counts_second = df_words['second'].value_counts()
df_counts_third = df_words['third'].value_counts()
df_counts_fourth = df_words['fourth'].value_counts()
df_counts_fifth = df_words['fifth'].value_counts()

dfranks = pd.concat([dfalpha, df_counts], axis=1)
dfranks = pd.concat([dfranks, df_counts_second], axis=1)
dfranks = pd.concat([dfranks, df_counts_third], axis=1)
dfranks = pd.concat([dfranks, df_counts_fourth], axis=1)
dfranks = pd.concat([dfranks, df_counts_fifth], axis=1)

def freq_ranking(word):
    val = dfranks['first'][word[0]] + dfranks['second'][word[1]] +dfranks['third'][word[2]] + dfranks['fourth'][word[3]] +dfranks['fifth'][word[4]]
    return val

