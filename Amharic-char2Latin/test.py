import pandas as pd
import numpy as np
import re

letter_data = pd.read_csv('letters.csv',delim_whitespace=True,index_col=0)
extra_letter_data = pd.read_csv('extra_letters.csv',delim_whitespace=True,index_col=0)
exception_list = [' ']
valid_char =["é","ê","h","l","h","m","s","r","s","sh","q","qh","b","v","t","ch","x","n","gy","a","k","kx","w","a","zh","z","y","d","d","j","g","gg","th","ch","ph","ts","tz","f","p","qw","qhw","ḫw","kw","kxw","gw","ä","u","i","a","e","í","o"]

def get_latin_char(char = 'ዩ'):
    try:
        if 4607 < ord(char) < 5018:
            return letter_data[letter_data.eq(char).any(1)].index.values[0]+letter_data[letter_data.eq(char)].dropna(how='all',axis=1).dropna().columns.values[0]
        else:
            return char
    except IndexError:
        if 4607 < ord(char) < 5018:
            return extra_letter_data[extra_letter_data.eq(char).any(1)].index.values[0]+extra_letter_data[extra_letter_data.eq(char)].dropna(how='all',axis=1).dropna().columns.values[0]
        else:
            return char

def get_latin_word(word):
    result =  map(get_latin_char, word)
    return ''.join(list(result))

def get_am_from_latin(word):
    delimiters = 'ä','u','i','a','e','í','o',' '
    regex_pattern = '|'.join('(?<={})'.format(re.escape(delim)) for delim in delimiters)
    word_list = re.split(regex_pattern, word)
    string = ''
    for i in word_list:
        if len(i.strip()) < 1:
            string = string + ' '
            continue

        i = i.strip()
        if not all(char in valid_char for char in i):
            string = string + i
            continue

        col = i[-1]
        row = i[:-1]


        string += letter_data[col][row]

    return string[0]
        
result=get_latin_word('የይርጋለም የተቀናጀ የግብርና ኢንዱስትሪ ፓርክ 11 1 ሼዶች የተጠናቀቁ ሲሆን ከነዚህ መካከል 4ቱ')
print(result)
print(get_am_from_latin(result))