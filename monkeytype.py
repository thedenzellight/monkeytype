import time
import random
import os
from difflib import SequenceMatcher

equality = input("Write anything: ")

letters = ["q", "w", "e", "r", "t", "y", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", " ", "!", ":", ";"]


BestMatch = 0.0
wordsCount = 0
BestMatchWord = "Meow"


x = 10
a = 1

while x>a:
    
    length = random.randint(1, len(equality))
    
    word = random.choice(letters)
    
    generated = 0
    
    for i in range(length):
        word = word + random.choice(letters)
        similiarity = SequenceMatcher(None, equality, word).ratio()
        
    if similiarity > BestMatch:
        BestMatch = similiarity
        BestMatchWord = word
    
    
    print(word, "   ", "Match: ", similiarity)
    
    wordsCount = wordsCount + 1
    
    print("----------------------------------------------------------------")
    
    print("Best match: ")
    
    print(BestMatch)
    
    print("Best sentence match: ")
    
    print(BestMatchWord)
    
    print("Sentence generated: ")
    
    print(wordsCount)
    
    print("----------------------------------------------------------------")
    
    if similiarity == 1:
       print("100% Match!") 
    
    
       while similiarity == 1:
    
           time.sleep(1)

