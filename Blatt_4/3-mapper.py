#!/usr/bin/python3
import sys

def mapMe(line):
    splitted = line.split(",")
    apps = ",".join(splitted[:4])
    counts = ",".join(splitted[4:])
    return_string = apps + "/" + counts
    print(return_string)


def main():
    for line in sys.stdin:
        mapMe(line)


def test():
    lines = []
    with open("/home/mpim/m300517/Downloads/data-energy-efficiency.csv") as f:
        for i in range(10000):
            lines.append(f.readline())

    for line in lines:
        mapMe(line)


if __name__ == "__main__":
    main()