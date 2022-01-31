from english_words import english_words_set
import pandas as pd
import numpy as np
import func as f
import requests
from time import sleep
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def remove_notcontains(grey,df):
    df_sub = df
    for l in grey:
        df_sub = (df_sub.loc[(~df_sub['guess'].str.contains(l))])
    return df_sub

def remove_by_contains(letters,df):
    df_sub = df
    for l in letters:
        df_sub = (df_sub.loc[(df_sub['guess'].str.contains(l))])
    return df_sub

def remove_by_location(loc,letter,df):
    df_sub = df
    loc = loc-1 # for easier use 0 is positon 1
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str[loc]==l)])
    return df_sub

def remove_by_not_location(loc,letter,df):
    df_sub = df
    loc = loc-1 # for easier use 0 is positon 1
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str[loc]!=l)])
    return df_sub
    
def remove_by_letter_count(letter,count,df):
    df_sub = df
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str.count(letter)==count)])
    return df_sub

def enter_guess(results=[]):
    round = 0
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

def check_resutls(browser):
    results = []
    for n in range(6):
        qry_script = f"""return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[{n}].shadowRoot.querySelectorAll('game-tile[letter]')"""

        qry_r = browser.execute_script(qry_script)
        for i, element in enumerate(qry_r):
            try:
                sub = qry_r[i].get_attribute("outerHTML")
                letter = sub[(sub.find('letter=')+8):(sub.find('letter=')+9)]
                stat_target = (sub.find('" reveal')+1) - (sub.find('evaluation=')) - 11
                status = sub[(sub.find('evaluation='))+12:(sub.find('evaluation='))+10+stat_target]
                # store the resutls to return
                results.append((letter +','+status))
            except:
                print(f"no result for row {n}")
    return results
