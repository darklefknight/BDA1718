#!/usr/bin/python3

"""
Reducer for task2 sheet4.
By Finn Burgemeister and Tobias Machnitzki

This reducer uses the output from the 2-map.py script and creates overall counts from the article-conts.
"""

import sys
import re

def getInputbyFile():
    """
    This function is just for testing and debugging
    :return:
    """
    FILE = "example.txt"

    with open(FILE) as f:
        lines = f.readlines()
        return lines


def main():
    file = "\n"
    for line in sys.stdin:
        # I decided on counting the stemmed words in all articles
        stemmed_words = re.findall(r'"(.*?)"', line)[2]
        stemmed_words = stemmed_words.replace("stemmed", "").replace(" ","")
        stemmed_list = stemmed_words[1:-1].split(",")

        for stemmed_word in stemmed_list:
            try:
                word,count = stemmed_word.split(":") # if empty line was returned by map use next input
            except:
                continue

            check_word = "\n" + word + "," # if we would just check for the word itself,
                                           # we would get the result that "air" is in airbag and so on...
            if check_word in file:
                # Adding the count from the actual line to the overall-count:
                index = file.index(check_word) + 1
                index2 = file[index:].index("\n") + index
                act_word, act_count = file[index:index2].split(",")
                act_count = int(act_count)
                new_count = act_count + int(count)
                count_str = str(new_count)
                file = file.replace(act_word+",%i"%act_count,act_word+",%i"%new_count) #replace old result with new one
            else:
                file += word + "," + count + "\n" # if the word wasnt yet in the file just append it
    print(file)

if __name__ == "__main__":
    main()


