#!/usr/bin/python3

import wordcloud

if __name__ == "__main__":
    test_file = "/home/mpim/m300517/Downloads/enwiki-all-clean.csv"

    with open(test_file, "r") as f:
        line = f.readline()