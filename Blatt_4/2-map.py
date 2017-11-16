#!/usr/bin/python3

"""
Mapper for task2 sheet4.
By Finn Burgemeister and Tobias Machnitzki

This Mapper takes the semi-structured data from the "enwiki-clean.csv" file and prints out for each article the
ID, title, count of all words, count of each word stemmed, count of each word lemmatized.
"""


import re
import sys
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter

stemmer = SnowballStemmer("english") # defines the stemmer language
wordnet_lemmatizer = WordNetLemmatizer()


def getvalueByIndex(results, index: int, value: str):
    """
    for testing and debugging
    """
    return results[value][results["ID"].index(index)]


def getContentByValue(results, index: int, value: str):
    """
    for testing and debugging
    """
    return results["content"][value][results["ID"].index(index)]


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


def lemmatizeWord(word: str):
    """
    :param word: a single word as string
    :return: the lemma of that word as string
    """
    lemmed = wordnet_lemmatizer.lemmatize(word)
    if (len(lemmed) > 2) or (lemmed == "a") or (lemmed == "i"):
        return lemmed.lower()
    else:  # something needs to be returned (this is due to how this function is called)
        return 's'  # since s is not a valid return it is easy to throw it out later


def countWords(word_list):
    """
    counts the string elements in the given list. The list should only include elements of single words as strings.
    :param word_list: list of strings
    :return: dictionary of words and their number of occurrences within word_list
    """
    return dict(Counter(word_list))


def quoteMe(str):
    """
    a kinda wrapper function.
    :param str: string
    :return: string wrapped into quotes
    """
    return '"' + str + '"'


def main():
    PATH = ""
    FILE = "enwiki-clean_short.csv" #for debugging
    # FILE = "enwiki-clean.csv"

    EOF = False  # End of File

    error_counter = 0 # for debugging
    for line in sys.stdin:
        try: # <- something at some point will not match the pattern and we don't want our program to exit due to this ;)
            content = {"lemma": [],
                       "stemm": []
                       }
            results = {"ID": [],
                       "link": [],
                       "content": content,
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

            # Find text: (this is just everything in between the last two)
            text = " ".join(comma_split[3:])
            text = " ".join(text.split("[")[:-1])
            text = text.replace('"', '')

            text = cleanText(text) # get rid of everything else than plain text

            wordlist = text.split(" ") # each word becomes one element in this list

            # Stemming:
            stemmed_list = [stemWord(word) for word in wordlist]
            count_stemmed = countWords(stemmed_list)
            del count_stemmed["s"]
            results["content"]["stemm"].append(count_stemmed)

            # Lemmatizing:
            lemmed_list = [lemmatizeWord(word) for word in wordlist]
            count_lemmed = countWords(lemmed_list)
            del count_lemmed["s"]

            results["content"]["lemma"].append(count_lemmed)

            # Formatting string into right format using list-comprehension:
            stemm_str = ([("stemmed " + str(x) + ":" + str(y)) for (x, y) in results["content"]["stemm"][0].items()])
            stemm_str = ", ".join(stemm_str)

            lemma_str = ([("lemma of " + str(x) + ":" + str(y)) for (x, y) in results["content"]["lemma"][0].items()])
            lemma_str = ", ".join(lemma_str)

            # gluing together the string to print:
            print_string = quoteMe(str(results["ID"][0])) + "," + \
                           quoteMe(results["title"][0]) + "," + \
                           str(len(wordlist)) + "," + \
                           quoteMe("[" + stemm_str + "]") + "," + \
                           quoteMe("[" + lemma_str + "]")
            print(print_string)

        except:
            # print(line)
            error_counter += 1
            if error_counter < 1000: # if we get more the a 1000 errors something definitly is going wrong
                continue
            else:
                break


if __name__ == "__main__":
    main()
