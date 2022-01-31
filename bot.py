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


f = open('data/rankset.csv','r')
guesses = []

for line in f:
    guesses.append(line.strip())

print(str(len(guesses)))

def check_result(row, browser):
    ''' 
    row:  is being the game row you want data from
    browser: this needs passed the web controler you would like to use
    '''
    results = {}
    qry_script = f"""return document.querySelector('game-app').shadowRoot.querySelectorAll('game-row')[{row}].shadowRoot.querySelectorAll('game-tile[letter]')"""
    qry_r = browser.execute_script(qry_script)
    for i, element in enumerate(qry_r):
        try:
            sub = element.get_attribute("outerHTML")
            letter = sub[(sub.find('letter=')+8):(sub.find('letter=')+9)]
            stat_target = (sub.find('" reveal')+1) - (sub.find('evaluation=')) - 11
            status = sub[(sub.find('evaluation='))+12:(sub.find('evaluation='))+10+stat_target]
            # store the resutls to return
            results[letter] = [status,str(i)] 
        except:
            print(f"no result for row {row}")
    return results

# import guess dataset
value_set = pd.read_csv('data/rank_set.csv')
value_no_doubles = (value_set.loc[(value_set['double']!=True)])

max_val_guess = (value_no_doubles['guess'][value_no_doubles['total_score'].idxmax()])


try: 
    browser = webdriver.Firefox()
    browser.get('https://www.powerlanguage.co.uk/wordle/')
    assert 'Wordle' in browser.title

    elem = browser.find_element(By.CLASS_NAME, 'nightmode')
    sleep(3)
    elem.click()

    # get first best guess

    # loop
    for i in range(4):


    # get results of first guess and calculate next best
    # from the results filter the guess pool
    # try the next best guess


    results = f.check_resutls(browser)
    f.enter_guess(results)
    
    row = 0
    check_result(row=row,browser=browser)
    guess = 'ouija'
    elem.send_keys(guess + Keys.RETURN)


except:
    print('error finding webpage')
