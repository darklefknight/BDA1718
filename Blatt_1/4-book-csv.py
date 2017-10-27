import numpy as np
import re
from functools import lru_cache

@lru_cache(maxsize=256)
def removeStuffFromString(string):
    string = string.replace("!", " ").replace("?", " ").replace(".", " ").replace(",", " ").replace(";", " ").replace(
        "-", " ").replace("[", " ").replace("]", " ").replace("*", " ").replace("(", " ").replace(")", " ").replace(":",
        " ").replace("'", " ")
    return string

def countWordsInChapter(chapter):
    chapter = [line.strip() for line in chapter]  # remove EOL-charachter from each line
    chapter = " ".join(chapter).lower()  # Join list into one string and make everything lower case
    chapter = removeStuffFromString(chapter)
    chapterLength = len(chapter.split(" "))
    words = []  # initialize empty list
    counter = {}  # initialize empty dictionary
    for word in chapter.split(" "):
        if not word in words:  # count every word just once
            if ((len(word) <= 1) and (word != "a") and (word != "i")): continue
            wordCount = len(re.findall(word, chapter))  # count the word in the string
            counter[word] = wordCount  # append word to dictionary, with word as key and count as value
            words.append(word)
    return counter, chapterLength

if __name__ == "__main__":
    FILE_PATH = "/home/bigdata/1/moby-dick.txt"
    # FILE_PATH = "C:/Users/darkl/Dropbox/moby-dick.txt"

    with open(FILE_PATH, "r") as f:
        lines = f.readlines()  # read whole file

    counter = 1
    last_i = 0
    chapters = {}
    for i, line in enumerate(lines):
        if "CHAPTER %i" % counter in line:  # Find the chapter title
            Key = "Chapter%i" % (counter - 1)  # make dictionary key
            chapters[Key] = lines[last_i:i]  # add lines to dictionary

            counter += 1
            last_i = i

    del chapters["Chapter0"]  # chapter 0 does not belong to the story, but is everything before chapter 1

    chapterDict = {}
    chapterLength = {}
    for key in chapters.keys():
        chapterDict[key],chapterLength[key] = countWordsInChapter(chapters[key])

    with open("out.csv","w") as f:
        f.write("chapter-name,chapter-length,word-occurrences")
        for key in chapterDict.keys():
            json = " ".join(['"%s" : %i,'%(k,chapterDict[key][k]) for k in chapterDict[key].keys()])
            f.write(str(key) + "," + str(chapterLength[key]) + ",{" + json + "}")
