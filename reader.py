from logging import info
import re
import textract
from dateparser.search import search_dates
from scholarly import scholarly


class Extractor:
    def __init__(self, text):
        self.text = text
        self.article = self.isArticle()
        self.title = self.extract_title()

    def isArticle(self):
        return "arXiv" in self.text[:1000]

    def clean_title(self, title):
        cl_title = ""
        skip = False
        for i, c in enumerate(title):
            if skip:
                skip = False
            else:
                if c == "\\":
                    if i + 1 <= len(title) - 1 and title[i + 1] == "n":
                        cl_title += " "
                        skip = True
                else:
                    if i > 1 and i + 1 <= len(title) - 1 and title[
                            i - 1] == title[i + 1] == " ":
                        skip = True

                    cl_title += c
        return cl_title

    def extract_title(self):
        i_arxiv = self.text.find("arXiv")
        return self.clean_title(self.text[2:i_arxiv])

    def get_info(self):
        try:
            query = scholarly.search_pubs(self.title)
            pub = next(query)
            print(pub)
            #self.bibtex = scholarly.bibtex(pub)
            # self.author = pub["author"]
            # self.title = pub["author"]
            #print(self.bibtex)

        except:
            print("Can not acces bibtex")
