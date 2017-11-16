#!/usr/bin/python3

"""
Reducer for task2 sheet4.
By Finn Burgemeister and Tobias Machnitzki

This reducer uses the output from the 2-map.py script and creates overall counts from the article-conts.
Results are stored to the file "wiki-clean-frequency.csv"
"""

import sys
import re
import os
import atexit

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
    WRITE_PATH = "hdfs://abu2/user/gux/out/"
    WRITE_FILE = "wiki-clean-frequency.csv"
    if os.path.isfile(WRITE_PATH+WRITE_FILE): # check if file from previous run exists
        print("true")
        os.remove(WRITE_PATH+WRITE_FILE) # if so remove it and create an empty one
        f = open(WRITE_FILE+WRITE_PATH,"w")
        f.write("\n")
        f.close()
    else:
        f = open(WRITE_FILE+WRITE_PATH,"w")
        f.write("\n")
        f.close()


    with open(WRITE_PATH + WRITE_FILE, "w+") as f:
        for line in sys.stdin:
            # I decided on counting the stemmed words in all articles
            stemmed_words = re.findall(r'"(.*?)"', line)[2]
            stemmed_words = stemmed_words.replace("stemmed", "").replace(" ","")
            stemmed_list = stemmed_words[1:-1].split(",")

            for stemmed_word in stemmed_list:
                f.seek(0)   # got to beginning of file
                file = f.read() # and read it
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

                    # delete old content in file:
                    f.seek(0)
                    f.truncate()
                    # write new content:
                    f.write(file)
                else:
                    f.write(word + "," + count + "\n") # if the word wasnt yet in the file just append it

    return file


def panic_function(file):
    """
    this does not seem to work...
    :param file:
    :return:
    """
    print("Called panic function!")
    writefile = "tmp_save.csv"
    with open(writefile,"w") as f:
        f.write(file)

    print("wrote out results.")




if __name__ == "__main__":
    file = main()
    atexit.register(panic_function, file)

