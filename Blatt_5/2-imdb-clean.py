#!/usr/bin/python3

import re
import os

class Quote:
    def __init__(self,title:str,year:str,content:str,episode=None):
        self.title = title
        self.year = year
        self.episode = episode
        self.quotes = self.__splitContent(content)

    def __splitContent(self,content):
        results = []
        quote_dict = {}
        for line in content:
            if len(re.findall(":",line)) > 0:
                speaker_index = line.index(":")
                speaker = line[:speaker_index]
                quote = line[speaker_index+1:]
                quote_dict[speaker] = quote
            elif line != "":
                if not "speaker" in locals():
                    continue
                quote_dict[speaker] += line
            else:
                if quote_dict != {}:
                    results.append(quote_dict)
                quote_dict = {}
                if "speaker" in locals():
                    del speaker

        return results

    def __str__(self):
        if self.episode == None:
            return self.title + "  (from %i)"%self.year
        else:
            return self.title + ",  Episode:" + self.episode + "  (from %i)"%self.year

    def appendQuoteToCsv(self,file):
        with open(file,"a") as f:
            if self.episode == None:
                f.write(self.title + ";" + ";" + str(self.year) + ";" + str(self.quotes) + "\n" )
            else:
                f.write(self.title + ";" + self.episode + ";" + str(self.year) + ";" + str(self.quotes) + "\n")



if __name__ == "__main__":

    FILE_PATH = "/home/mpim/m300517/Downloads/"
    FILE_NAME = "imdb-quotes.txt"


    OUT_FILE = "imdb-quotes-structured.csv"
    if os.path.isfile(OUT_FILE):
        os.remove(OUT_FILE)


    ID_counter = 0
    EOF = False
    with open(FILE_PATH + FILE_NAME, "rb") as f:
        while True:
            try:
                line = f.readline()
            except:
                break
            line = line.decode("utf-8","ignore") # ignore errors of weird french names
            # print(i,line)
            if line[0] == "#": # indicates next movie
                if ID_counter > 0: # dont do this for the header of the file
                    if act_episode == None: # movies dont have episodes
                        this_quote = (Quote(title=act_title, year=act_year, content=act_content))
                    else: # but series do
                        this_quote = (Quote(title=act_title, year=act_year, content=act_content,episode=act_episode))
                    this_quote.appendQuoteToCsv(OUT_FILE)

                act_title_line = line.rstrip()
                try:
                    act_title = re.findall(r'"(.*?)"',act_title_line)[0]
                except:
                    act_title = "____"
                try:
                    act_year = re.findall(r'\((.*?)\)',act_title_line)[0]
                except:
                    act_year = (9999)
                act_episode_test = re.findall(r'\{(.*?)\}',act_title_line)
                if len(act_episode_test) > 0:
                    act_episode =  act_episode_test[0]
                else:
                    act_episode = None

                act_content = []
                ID_counter += 1
            elif "act_content" in locals():
                act_content.append(line.rstrip())
            else:
                continue


