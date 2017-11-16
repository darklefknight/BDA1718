#!/usr/bin/python3

"""
Mapper for task3 sheet4.
By Finn Burgemeister and Tobias Machnitzki

I don't think this mapper here is necessarry as it does not do very much but splitting the topic from the count...
But I want the points for it, so here it is.

The structure having a "mapMe" function is just for easier debugging.
"""

import sys

def mapMe(line):
    splitted = line.split(",")
    apps = ",".join(splitted[:4])
    counts = ",".join(splitted[4:])
    return_string = apps + "/" + counts # the returned string will have the structure "ap1,ap2,ap3,ap4/count1,count2..."
    print(return_string)


def main():
    for line in sys.stdin:
        mapMe(line)


def test():
    """
    This function is for testing the mapper with just a part of the file.
    """
    lines = []
    with open("/home/mpim/m300517/Downloads/data-energy-efficiency.csv") as f:
        for i in range(10000):
            lines.append(f.readline())

    for line in lines:
        mapMe(line)


if __name__ == "__main__":
    main()