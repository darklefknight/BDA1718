import numpy as np
import re

if __name__ == "__main__":
    # FILE_PATH = "/home/bigdata/1/moby-dick.txt"
    FILE_PATH = "C:/Users/darkl/Dropbox/moby-dick.txt"

    words = []

    with open(FILE_PATH, "r") as f:
        lines = f.readlines()   # read whole file

    lines = [line.strip() for line in lines]    # remove EOL-charachter from each line
    lines = " ".join(lines).lower() # Join list into one string and make everything lower case

    words = [] # initialize empty list
    counter = {} # initialize empty dictionary
    for word in lines.split():
        word = word.replace(",","").replace(".","").replace("?","").replace("!","") # replace delimiters.
        if not word in words:   # count every word just once
            wordCount = len(re.findall(word,lines)) # count the word in the string
            counter[word] = wordCount # append word to dictionary, with word as key and count as value
            words.append(word)

    Top10 = sorted(counter, key=counter.get, reverse=True)[:10]     # get dictionary keys with 10 highest values

    for key in Top10:
        print("%s, %i" %(key, counter[key]))    # print top 10 key plus value