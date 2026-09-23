'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

#easy 4 step method for getting data from a web data json
# 1. put it into a browswer 
# figure out how the data works
# 3. see what you actually need, get the keys.
# 4. write the code to request the data and process the data


import requests # needs to be pip installed
import json # should be native



# variables to query alphavantage
word = 'aggies'
search_word = "usu"

#make it obvious that it is a key by using the word key
key_word = "word"
key_score = "score"

#generate url
url = 'https://api.datamuse.com/words?ml=' + word
print(url)




#these are native libraries and are imported above
# requests stock data from data muse, web request object
request = requests.get(url) #pulls the url stored above. This does the same thing as entering the url into a browser
print(request.text)


# print(request.text) # print to double check data from web json api is good
dct_full = json.loads(request.text) # the s stands for string in the loads word, turns all the text and turns it into python data for you. Which is stored in dct_full
print(dct_full)

for dct in dct_full: 
    if dct["word"] == search_word:
        val = dct["score"]


print(val)
