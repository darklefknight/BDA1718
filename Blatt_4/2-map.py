import re

def getvalueByIndex(index:int,value:str):
    return results[value][results["ID"].index(index)]


if __name__ == "__main__":
    PATH = "/home/mpim/m300517/Downloads/"
    FILE = "enwiki-clean.csv"

    EOF = False # End of File
    content = {     "lemma":[],
                    "lemmaCount":[],
                    "stemm":[],
                    "stemmCount":[]
                }

    results = {"ID":[],
               "link":[],
                "content":content,
               "topics":[]
               }

    error_counter = 0
    with open(PATH + FILE, "r") as f:
        text = f.readline().rstrip()
        text2 = f.readline().rstrip()
        text3 = f.readline().rstrip()

        while not EOF:
            try:
                line = f.readline().rstrip()

                comma_split = line.split(",")
                results["ID"].append(int(comma_split[0]))
                results["link"].append(comma_split[1])


                klammer_split = line.split("[")
                topic_list = re.findall(r"'(.*?)'", klammer_split[-1])
                results["topics"].append(topic_list)

                # Find text:
                text = " ".join(comma_split[2:])
                text = " ".join(text.split("[")[:-1])
                text = text.replace('"','')

                # TODO: clean text
                # TODO: lemmatisation
                # TODO: steammatisation
                # TODO: wordcount
                # TODO: append to results

            except:
                # print(line)
                error_counter += 1
                if error_counter < 100:
                    continue
                else:
                    break

