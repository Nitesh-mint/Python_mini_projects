import json
from difflib import get_close_matches
from logging import raiseExceptions
o = open("data.json")


data = json.load(o)

word = input("Enter a word: ").lower()

def Dict(data, word):
    if word in data:
        return data[word]
    elif(len(get_close_matches(word, data))>0):
        list = get_close_matches(word,data)
        ask = input("Did you mean "+str(list[0])+"? Type y or n:").lower()
        if ask=="y":
            word = list[0]
            return data[word]
        elif(ask == 'n'):
            return "There's no word like that please double check it."
        else:
            return "I didn't understand what you're saying"
    else:
        return "I don't have that word's meaning"

print(Dict(data,word))