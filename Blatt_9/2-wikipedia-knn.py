import re
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.neighbors import NearestNeighbors

stemmer = SnowballStemmer("english") # defines the stemmer language


def split_line(results, line):
    """
    :param results: result dict
    :param line: wiki content line
    :return results: structurized data with stemmed words with frequency
    """

    # Split:
    line = line.rstrip()

    # By splitting the line at the comma we can easy extract the ID, link and title:
    comma_split = line.split(",")
    results["ID"].append(int(comma_split[0]))
    results["link"].append(comma_split[1])
    results["title"].append(comma_split[2])

    # By finding the last [ we can find where the "topics-section" is:
    klammer_split = line.split("[")
    topic_list = re.findall(r"'(.*?)'", klammer_split[-1])
    results["topics"].append(topic_list)

    # Find text: (this is just everything in between the last two)
    text = " ".join(comma_split[3:])
    text = " ".join(text.split("[")[:-1])
    text = text.replace('"', '')

    text = cleanText(text)  # get rid of everything else than plain text

    wordlist = text.split(" ")  # each word becomes one element in this list

    # Stemming:
    results["content"].append([stemWord(word) for word in wordlist])
    #count_stemmed = countWords(stemmed_list)
    #del count_stemmed["s"]
    #results["content"].append(count_stemmed)

    return results


def cleanText(text: str):
    """
    :param text: just any string
    :return: cleaned string just containing charachters a-z and A-Z, nothing else
    """
    return re.sub('[^A-Za-z]+', ' ', text)


def stemWord(word: str):
    """
    :param word: a single word as string
    :return: the stemm of that word as string
    """
    stemmed = stemmer.stem(word)
    if (len(stemmed) > 2) or (stemmed == "a") or (stemmed == "i"):
        return stemmed.lower()
    else: # something needs to be returned (this is due to how this function is called)
        return 's' # since s is not a valid return it is easy to throw it out later


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

    wiki_struc = {"ID": [],
               "link": [],
               "topics": [],
               "title": [],
               "content": []
    }

    with open(FILE, "r") as f:
        for i, line in enumerate(f):
            if i > training:
                break
            wiki_struc = split_line(wiki_struc, line)

    print(len(wiki_struc["content"]))

    """
    # IDEA
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
    """




