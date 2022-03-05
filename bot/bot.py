import pandas as pd
from time import sleep
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

rank_set_path = 'data_analysis/datasets/rank_set.csv'

f = open(rank_set_path,'r')

guesses = []

for line in f:
    guesses.append(line.strip())

print(str(len(guesses)))

# import guess dataset
value_set = pd.read_csv(rank_set_path)
value_no_doubles = (value_set.loc[(value_set['double']!=True)])
value_no_doubles_solutions = (value_no_doubles.loc[(value_no_doubles['solution']==True)])
value_solutions_doubles = (value_no_doubles.loc[(value_no_doubles['solution']==True)])

guess = (value_no_doubles['guess'][value_no_doubles['total_score'].idxmax()])
# guess = 'cumin'

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
    loc = loc # for easier use 0 is positon 1
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str[loc]==l)])
    return df_sub
def remove_by_not_location(loc,letter,df):
    df_sub = df
    loc = loc # for easier use 0 is positon 1
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str[loc]!=l)])
    return df_sub
def remove_by_letter_count(letter,count,df):
    df_sub = df
    for l in letter:
        df_sub = (df_sub.loc[(df_sub['guess'].str.count(letter)==count)])
    return df_sub
def check_result(row, browser):
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
            print(letter)
            print(status)
            print(str(i))
            results[letter+str(i)] = [status,str(i)] 
        except:
            print(f"no result for row {row}")
    return results
def next_guess(result, df):
    for v in result:
        letter = v[0] 
        status = result[v][0]
        placement = int(result[v][1])
        if status == 'correct':
            print('correct')
            # df = remove_by_contains(letter,df)
            df = remove_by_location(placement,letter,df)
        elif status == 'present':
            print('present')
            df = remove_by_contains(letter,df)
            df = remove_by_not_location(placement,letter,df)
        elif status == 'absent':
            print('absent')
            df = remove_notcontains(letter,df)

    return df

browser = webdriver.Firefox()
browser.get('https://www.powerlanguage.co.uk/wordle/')
assert 'Wordle' in browser.title

elem = browser.find_element(By.CLASS_NAME, 'nightmode')
sleep(3)
elem.click()

# get first best guess from import dataset
elem.send_keys(guess + Keys.RETURN)

# first guess is on it's own, then start loop
sleep(3)

first_result = check_result(0,browser)
df_filter = next_guess(first_result, value_no_doubles)

for i in range(1,6):
    guess = (df_filter['guess'][df_filter['total_score'].idxmax()])
    
    elem.send_keys(guess + Keys.RETURN)

    sleep(3)

    result = check_result(i,browser)

    df_filter = next_guess(result, df_filter)
    

browser.close()
