import urllib.request
import re
def clean_extract_Images(text):
    splitted_text = text.split("\n")
    cleaned_text = []
    image_lines = []
    page_name = "not found"
    for line in splitted_text:
        if '<link rel="canonical" href' in line:
            page_name = line[line.index("http"):-3]
            page_name = page_name + "#/media/File:"

        if 'class="image"' in line:
            try:
                text = line
                text = text[text.index("src") + 5:]
                if ".svg.png" in text:
                    text = text[:text.index(".svg") + 4]
                elif ".jpg" in text:
                    text = text[:text.index('.jpg') + 4]
                elif ".JPG" in text:
                    text = text[:text.index('.JPG') + 4]
                elif ".png" in text:
                    text = text[:text.index('.png') + 4]
                elif ".gif" in text:
                    text = text[:text.index('.gif') + 4]
                indices = [i for i, x in enumerate(text) if x == "/"]
                text = text[indices[-1] + 1 :]
                if not "Question_book" in text:
                    image_lines.append(page_name + text)
                else:
                    # print(text)
                    image_lines.append("https://en.wikipedia.org/wiki/File:" + text)
            except:
                print(line)
                print(text)
        else:
            cleaned_text.append(line + "\n")

    cleaned_text = " ".join(cleaned_text)
    list_of_removed_content = image_lines
    return (cleaned_text,list_of_removed_content)

def clean_extract_Tables(text):
    splitted_text = text.split("\n")

    append_line = False
    same_table = 0
    table = {}
    tableHeaders = {}
    cleaned_text = []

    for line in splitted_text:
        text = line

        if "<table" in line:
            append_line = True
            table[str(same_table)] = []
        if "/table" in line:
            append_line = False
            same_table += 1

        if append_line:
            table[str(same_table)].append(line)
        else:
            cleaned_text.append(line)

        for key in table.keys():
            tableHeaders[str(key)] = ""
            isHeader = False
            for tableLine in table[key]:
                if "<tr" in tableLine:
                    isHeader = True
                    continue
                if "</tr" in tableLine:
                    isHeader = False
                    break

                if isHeader:
                    # print(tableLine)
                    headerLine = tableLine[tableLine.index(">") + 1:]

                    headerLine = headerLine[:headerLine.index("<")]
                    tableHeaders[key] += headerLine + ";"


    list_of_removed_content = []
    for key in tableHeaders:
        if len(tableHeaders[key][:-1]) > 1:
            list_of_removed_content.append(tableHeaders[key][:-1])
    cleaned_text = " ".join(cleaned_text)
    return (cleaned_text, list_of_removed_content)

if __name__ == "__main__":
    page_name = "https://de.wikipedia.org/wiki/Essigs%C3%A4ure"
    page = urllib.request.urlopen(page_name)
    text = page.read()
    text = text.decode()
    cleaned_text,liste = clean_extract_Images(text)
    print(liste)

    cleaned_text,liste = clean_extract_Tables(cleaned_text)
    print(liste)