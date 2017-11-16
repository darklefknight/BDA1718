import sys
import re
import os

def getInputbyFile():
    FILE = "example.txt"

    with open(FILE) as f:
        lines = f.readlines()
        return lines


def getInput():
    """
    At some point this will get the Input from std_in
    :return:
    """
    pass

def main():
    WRITE_PATH = ""
    WRITE_FILE = "wiki-clean-frequency.csv"
    if os.path.isfile(WRITE_PATH+WRITE_FILE):
        print("true")
        os.remove(WRITE_PATH+WRITE_FILE)
        f = open(WRITE_FILE+WRITE_PATH,"w")
        f.write("\n")
        f.close()

    with open(WRITE_PATH + WRITE_FILE, "w+") as f:
        # lines = getInputbyFile() #TODO: get the Input from map-function with hadoop
        for line in sys.stdin:
            stemmed_words = re.findall(r'"(.*?)"', line)[2]
            stemmed_words = stemmed_words.replace("stemmed", "").replace(" ","")
            stemmed_list = stemmed_words[1:-1].split(",")

            for stemmed_word in stemmed_list:


                f.seek(0)
                file = f.read()
                try:
                    word,count = stemmed_word.split(":")
                except:
                    continue

                check_word = "\n" + word + ","
                if check_word in file:
                    index = file.index(check_word) + 1
                    index2 = file[index:].index("\n") + index
                    act_word, act_count = file[index:index2].split(",")
                    act_count = int(act_count)
                    new_count = act_count + int(count)
                    count_str = str(new_count)
                    file = file.replace(act_word+",%i"%act_count,act_word+",%i"%new_count)
                    # print(word,count,act_word,count_str)
                    f.seek(0)
                    f.truncate()
                    f.write(file)
                else:
                    f.write(word + "," + count + "\n")


if __name__ == "__main__":
    main()