import urllib.request

def clean_extract_Images(text):
    cleaned_text = text.decode().split("\n")
    image_lines = []
    page_name = "not found"
    for line in cleaned_text:
        if '<link rel="canonical" href' in line:
            page_name = line[line.index("http"):-3]

        if 'class="image"' in line:
            image_lines.append(line)
    list_of_removed_content = []
    return (cleaned_text, page_name)

def clean_extract_Tables(text):
    pass
    cleaned_text = text
    list_of_removed_content = []
    return (cleaned_text, list_of_removed_content)

if __name__ == "__main__":
    page = urllib.request.urlopen('https://de.wikipedia.org/wiki/Normatmosph%C3%A4re')
    text = page.read()
    cleaned_text,liste = clean_extract_Images(text)