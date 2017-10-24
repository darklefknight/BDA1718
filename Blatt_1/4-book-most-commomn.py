import numpy as np
import re

if __name__ == "__main__":
    # FILE_PATH = "/home/bigdata/1/moby-dick.txt"
    FILE_PATH = "C:/Users/darkl/Dropbox/moby-dick.txt"

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



    # Top10 = sorted(counter, key=counter.get, reverse=True)[:10]     # get dictionary keys with 10 highest values
    #
    # for key in Top10:
    #     print("%s, %i" %(key, counter[key]))    # print top 10 key plus value