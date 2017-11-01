import urllib.request
import re

def clean_extract_Images(text):
    """
    Removes the images from a wikipedia page. Returns the removed images as links.

    :param text: decoded text as one string
    :return:    cleaned_text - string where the image-elements are removed
                list_of_removed_content - list of links to the images inside that wikipedia-page
    """

    splitted_text = text.split("\n")    # split the string at each newline char
    cleaned_text = []
    image_lines = []
    page_name = "not found"
    for line in splitted_text:
        # get Link to main article:
        if '<link rel="canonical" href' in line:
            page_name = line[line.index("http"):-3]
            page_name = page_name + "#/media/File:"

        # find the images:
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
                # The Question-book logo is not part of the articles content but of the wikipedia-main-content,
                # so it is located at a diiferent path:
                if not "Question_book" in text:
                    image_lines.append(page_name + text)
                else:
                    image_lines.append("https://en.wikipedia.org/wiki/File:" + text)
            except:
                print(line)
                print(text)
        else:
            cleaned_text.append(line + "\n")

    cleaned_text = " ".join(cleaned_text)   # make the page one string again
    list_of_removed_content = image_lines
    return (cleaned_text,list_of_removed_content)

def clean_extract_Tables(text):
    """
    Removes the tables from a wikipedia page. Returns the names of the columns of each removed table.

    :param text: decoded text as one string
    :return:    cleaned_text - string where the tables are removed
                list_of_removed_content - names of the columns of the removed tables
    """
    splitted_text = text.split("\n")

    append_line = False
    same_table = 0
    table = {}
    tableHeaders = {}
    cleaned_text = []

    for line in splitted_text:
        text = line

        # search for table elements:
        if "<table" in line:
            append_line = True
            table[str(same_table)] = []
        if "/table" in line:
            append_line = False
            same_table += 1

        # make each table a sepperate dictionary entry
        if append_line:
            table[str(same_table)].append(line)
        else:
            cleaned_text.append(line)

        # in each table-dictionary entry search for the column names:
        for key in table.keys():
            tableHeaders[str(key)] = ""
            isHeader = False
            for tableLine in table[key]:
                if "<tr" in tableLine:  # column names will be found in the first row of a table
                    isHeader = True
                    continue
                if "</tr" in tableLine:
                    isHeader = False
                    break # after the column names have been found we can jump to the next table

                if isHeader:
                    headerLine = tableLine[tableLine.index(">") + 1:]
                    headerLine = headerLine[:headerLine.index("<")]
                    tableHeaders[key] += headerLine + ";" # append an ";" after each column name


    list_of_removed_content = []
    for key in tableHeaders:
        if len(tableHeaders[key][:-1]) > 1: # get rid of empty strings
            list_of_removed_content.append(tableHeaders[key][:-1]) # exclude the last semicolon
    cleaned_text = " ".join(cleaned_text) # make the wikipedia page one string again
    return (cleaned_text, list_of_removed_content)

if __name__ == "__main__":
    # get an example wikipedia article:
    page_name = "https://de.wikipedia.org/wiki/Essigs%C3%A4ure"
    page = urllib.request.urlopen(page_name)
    text = page.read()
    text = text.decode()


    cleaned_text,liste = clean_extract_Images(text)
    print(liste)

    cleaned_text,liste = clean_extract_Tables(cleaned_text)
    print(liste)