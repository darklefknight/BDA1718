import re
from functools import lru_cache


@lru_cache(maxsize=256)
def removeStuffFromString(string):
    string = string.replace("!", " ").replace("?", " ").replace(".", " ").replace(",", " ").replace(";", " ").replace(
        "-", " ").replace("[", " ").replace("]", " ").replace("*", " ").replace("(", " ").replace(")", " ").replace(":",
        " ").replace("'", " ")
    return string


if __name__ == "__main__":
    # FILE_PATH = "/home/bigdata/1/moby-dick.txt"
    FILE_PATH = "C:/Users/darkl/Dropbox/moby-dick.txt"

    words = []

    with open(FILE_PATH, "r") as f:
        lines = f.readlines()  # read whole file

    lines = [line.strip() for line in lines]  # remove EOL-charachter from each line
    lines = " ".join(lines).lower()  # Join list into one string and make everything lower case
    lines = removeStuffFromString(lines)
    words = []  # initialize empty list
    counter = {}  # initialize empty dictionary
    for word in lines.split(" "):
        word = removeStuffFromString(word)
        if not word in words:  # count every word just once
            if ((len(word) <= 1) and (word != "a") and (word != "i")): continue
            wordCount = len(re.findall(word, lines))  # count the word in the string
            if len(counter) < 11:
                counter[word] = wordCount  # append word to dictionary, with word as key and count as value
            elif min(sorted(counter.values(), reverse=True)[:-10]) \
                < wordCount:  # just append if wordCount is bigger then smallest value in counter
                counter[word] = wordCount  # append word to dictionary, with word as key and count as value
            words.append(word)
    #
    Top10 = sorted(counter, key=counter.get, reverse=True)[:10]  # get dictionary keys with 10 highest values

    for key in Top10:
        print("%s, %i" % (key, counter[key]))  # print top 10 key plus value
