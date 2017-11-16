#!/usr/bin/python3

import sys
import numpy as np

def main():
    means = []
    line_counter = 0
    last_apps = " "
    for line in sys.stdin:
        try:
            apps_1,count_str = line.split("/")
            counts = count_str.split(",")
            counts = [float(x) for x in counts]
        except:
            # print("error")
            # print(line)
            continue
        apps = apps_1
        if apps == last_apps:
            line_counter += 1
            means = np.divide(np.add(np.multiply(means,line_counter-1),counts),line_counter)
            last_apps = apps

        else:
            means = [str(x) for x in means]
            means = ",".join(means)
            writeToFile(apps, means)
            means = counts
            line_counter = 1
            last_apps = apps


def writeToFile(app_str,mean_str):
    write_path = ""
    write_file = "energy-efficiency-counts.csv"
    print(app_str)
    with open(write_path + write_file, "a") as f:
        f.write(app_str + " " + mean_str + "\n")



if __name__ == "__main__":
    main()