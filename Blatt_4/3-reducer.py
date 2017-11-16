#!/usr/bin/python3

"""
Reducer for task3 sheet4.
By Finn Burgemeister and Tobias Machnitzki

This reducer uses the output from the 3-mapper.py script and calculates the mean of the columns.
It is doing it on the run, so that it is not necassary to store all the values from previous lines.
"""


import sys
import numpy as np

def main():
    means = []
    line_counter = 0
    last_apps = " "
    for line in sys.stdin:
        try: #<- sometimes the mapper returns an empty line, then this will catch an error and exit of the program
            apps_1,count_str = line.split("/")
            counts = count_str.split(",")
            counts = [float(x) for x in counts]
        except:
            # print("error")
            # print(line)
            continue
        apps = apps_1
        if apps == last_apps: # checking if we are still in the same test-run
            line_counter += 1
            means = np.divide(np.add(np.multiply(means,line_counter-1),counts),line_counter)
            last_apps = apps

        else: # if we are not in the same test-case anymore, write out the results:
            means = [str(x) for x in means]
            means = ",".join(means)
            writeToFile(apps, means)
            means = counts
            line_counter = 1
            last_apps = apps


def writeToFile(app_str,mean_str):
    """
    This function just writes out the results, one at a time
    :param app_str: string of the test-case (e.g.: ntc,ntc,ntc,ntc)
    :param mean_str: string containing the mean of each column
    """
    write_path = ""
    write_file = "energy-efficiency-counts.csv"
    print(app_str)
    with open(write_path + write_file, "a") as f:
        f.write(app_str + " " + mean_str + "\n")



if __name__ == "__main__":
    main()