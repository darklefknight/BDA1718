import re

def cleanText(text: str):
    """
    :param text: just any string
    :return: cleaned string just containing charachters a-z and A-Z, nothing else
    """
    return re.sub('[^A-Za-z]+', ' ', text)


if __name__ == "__main__":
    FILE = "enwiki-clean-categories_1000.csv"

    with open(FILE, "r") as f:
        for line in f:
            try:  # <- something at some point will not match the pattern and we don't want our program to exit due to this ;)
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

                text = cleanText(text)  # get rid of everything else than plain text
