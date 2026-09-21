'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

#easy 4 step method for getting data from a web data json
# 1. put it into a browswer and look at it 

# 3. see what you actually need
# 4. write the code to request the data


import requests # needs to be pip installed
import json # should be native

# example url to query datamuse web json api
example_url = "https://api.datamuse.com/words?ml=duck"

# variables to query alphavantage
word = 'duck'
search_word = "dunk"

#make it obvious that it is a key by using the word key
key_word = "word"
key_score = "score"

#generate url
url = 'https://api.datamuse.com/words?ml=' + word
print(url)

#these are native libraries and are imported above
# requests stock data from data muse, web request object
request = requests.get(url) #pulls the url stored above. This does the same thing as entering the url into a browser
# print(request.text) # print to double check data from web json api is good
dct_full = json.loads(request.text) # the s stands for string in the loads word, turns all the text and turns it into python data for you. Which is stored in dct_full



#####################################################################
# programming activity
# What is the score of the associated word: mallard
# Steps: 
# 1. load json into a dictionary
# 2. search for word "mallard"
# 3. print associated score value for mallard

# answer below, try yourself before looking


# dunk

for word_2 in dct_full:
    if word_2[key_word] == search_word:
        print(word_2[key_score])



























# for dct_small in dct_full:
#     # print(dct_small) # print all values to verify data is good
#     if dct_small[key_word] == search_word:
#         print("word: ", dct_small[key_word])
#         print("value: ", dct_small[key_score])
        