import re
import numpy as np


from sklearn.neighbors import NearestNeighbors

def split_line(line):
    results = {"ID": [],
               "link": [],
               "topics": [],
               "title": []
               }
    line = line.rstrip()
    # print(line)
    # By splitting the line at the comma we can easy extract the ID, link and title:
    comma_split = line.split(",")
    results["ID"].append(int(comma_split[0]))
    results["link"].append(comma_split[1])
    results["title"].append(comma_split[2])

    # By finding the last [ we can find where the "topics-section" is:
    klammer_split = line.split("[")
    topic_list = re.findall(r"'(.*?)'", klammer_split[-1])
    results["topics"].append(topic_list)

    return results

def get_lines_of_file(file):
    with open(file,"r") as f:
        for i, _ in enumerate(f):
            pass
    return i


if __name__ == "__main__":
    FILE = "enwiki-clean-categories_1000.csv"

    lines = get_lines_of_file(FILE)

    sep = int(lines/3)

    training = sep
    test = sep*2
    validation = lines

    # ========================
    # TRAINING:
    # ========================
    with open(FILE, "r") as f:
        for i,line in enumerate(f):
            if i > training:
                break

            results = split_line(line)

            with open(FILE,"r") as f2:
                for j,line2 in enumerate(f2):
                    if j > training:
                        break
                    if j<=i:
                        continue


                    results2 = split_line(line2)
                    inter_set = set(results["topics"][0]).intersection(results2["topics"][0])
                    if len(inter_set) >=2:
                        print(inter_set,i,j)





