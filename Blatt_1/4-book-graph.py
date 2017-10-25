import numpy as np
import re
import matplotlib.pyplot as plt
import argparse

def countWordInChapter(word, string):
    return len(re.findall(word.lower(), string.lower()))

if __name__ == "__main__":
    FILE_PATH = "/home/bigdata/1/moby-dick.txt"
    # FILE_PATH = "C:/Users/darkl/Dropbox/moby-dick.txt"

    parser = argparse.ArgumentParser(description='Add a word you want to count in Moby Dick.')
    parser.add_argument(type=str,dest="word",
                        help='Add a word you want to count in Moby Dick.')
    word = parser.parse_args().word
    print(word)

    words = []
    with open(FILE_PATH, "r") as f:
        lines = f.readlines()  # read whole file

    counter = 1
    last_i = 0
    dictionary = {}
    for i, line in enumerate(lines):
        if "CHAPTER %i" % counter in line:  # Find the chapter title
            Key = "Chapter%i" % (counter - 1)  # make dictionary key
            dictionary[Key] = lines[last_i:i]  # add lines to dictionary

            counter += 1
            last_i = i

    del dictionary["Chapter0"]  # chapter 0 does not belong to the story, but is everything before chapter 1
    for lastKey in dictionary.keys():
        pass # get the key of the last chapter

    dictionary[lastKey]


    count = {}
    for key in dictionary.keys():
        joined = " ".join(dictionary[key])
        joined = joined.replace("\n", "").replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(
            "--", " ").replace('"', '').replace(";", "")    # Remove everything that is not usefull for counting

        count[key] = countWordInChapter(word,joined)

    values = []
    for key in sorted(count.keys()):
        values.append(count[key])

    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Number of the occurrences of the word '%s' in each chapter."%word)
    ax1 = fig.add_subplot(111)

    ax1.bar(np.linspace(1,len(values),len(values)),values)
    ax1.set_xlim(0,len(count.keys())+1)
    ax1.set_ylim(0,max(values)+5)
    ax1.grid()

    ax1.set_ylabel("Number of occurrences of the word '%s'" %word)
    ax1.set_xlabel("Number of the Chapter")
    # plt.savefig()