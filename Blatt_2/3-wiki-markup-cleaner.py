import urllib.request
import re
def clean_extract_Images(text):
    decoded_text = text.decode().split("\n")
    cleaned_text = []
    image_lines = []
    page_name = "not found"
    for line in decoded_text:
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
                elif ".png in text":
                    text = text[:text.index('.png') + 4]
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
    pass
    cleaned_text = text
    list_of_removed_content = []
    return (cleaned_text, list_of_removed_content)

if __name__ == "__main__":
    page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Election')
    text = page.read()
    cleaned_text,liste = clean_extract_Images(text)
    print(liste)

    cleaned_text,liste = clean_extract_Tables(text)
