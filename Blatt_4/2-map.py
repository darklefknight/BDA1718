#!/usr/bin/python3
import re
import sys
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter

stemmer = SnowballStemmer("english")
wordnet_lemmatizer = WordNetLemmatizer()


def getvalueByIndex(results, index: int, value: str):
    return results[value][results["ID"].index(index)]


def getContentByValue(results, index: int, value: str):
    return results["content"][value][results["ID"].index(index)]


def cleanText(text: str):
    return re.sub('[^A-Za-z]+', ' ', text)


def stemWord(word: str):
    stemmed = stemmer.stem(word)
    if (len(stemmed) > 2) or (stemmed == "a") or (stemmed == "i"):
        return stemmed.lower()
    else:
        return 's'


def lemmatizeWord(word: str):
    lemmed = wordnet_lemmatizer.lemmatize(word)
    if (len(lemmed) > 2) or (lemmed == "a") or (lemmed == "i"):
        return lemmed.lower()
    else:
        return 's'


def countWords(word_list):
    return dict(Counter(word_list))


def quoteMe(str):
    return '"' + str + '"'


def main():
    PATH = ""
    FILE = "enwiki-clean_short.csv"
    # FILE = "enwiki-clean.csv"

    EOF = False  # End of File

    error_counter = 0
    for line in sys.stdin:
        try:
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
            comma_split = line.split(",")
            results["ID"].append(int(comma_split[0]))
            results["link"].append(comma_split[1])
            results["title"].append(comma_split[2])

            klammer_split = line.split("[")
            topic_list = re.findall(r"'(.*?)'", klammer_split[-1])
            results["topics"].append(topic_list)

            # Find text:
            text = " ".join(comma_split[3:])
            text = " ".join(text.split("[")[:-1])
            text = text.replace('"', '')

            text = cleanText(text)

            wordlist = text.split(" ")

            stemmed_list = [stemWord(word) for word in wordlist]
            count_stemmed = countWords(stemmed_list)
            del count_stemmed["s"]
            results["content"]["stemm"].append(count_stemmed)

            lemmed_list = [lemmatizeWord(word) for word in wordlist]

            count_lemmed = countWords(lemmed_list)
            del count_lemmed["s"]

            results["content"]["lemma"].append(count_lemmed)

            stemm_str = ([("stemmed " + str(x) + ":" + str(y)) for (x, y) in results["content"]["stemm"][0].items()])
            stemm_str = ", ".join(stemm_str)

            lemma_str = ([("lemma of " + str(x) + ":" + str(y)) for (x, y) in results["content"]["lemma"][0].items()])
            lemma_str = ", ".join(lemma_str)

            print_string = quoteMe(str(results["ID"][0])) + "," + \
                           quoteMe(results["title"][0]) + "," + \
                           str(len(wordlist)) + "," + \
                           quoteMe("[" + stemm_str + "]") + "," + \
                           quoteMe("[" + lemma_str + "]")
            print(print_string)

        except:
            # print(line)
            error_counter += 1
            if error_counter < 100:
                continue
            else:
                break


if __name__ == "__main__":
    main()
