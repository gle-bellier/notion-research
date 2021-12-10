from logging import info
import re
import textract
from dateparser.search import search_dates
from scholarly import scholarly


class Article:
    def __init__(self, path):
        self.text = str(textract.process(path))
        self.title = self.extract_title()
        self.metadata = self.get_metadata()

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

    def get_metadata(self):
        try:
            query = scholarly.search_pubs(self.title)
            pub = next(query)
            bibtex = scholarly.bibtex(pub)

            infos = scholarly.fill(pub)
            title = infos["bib"]["title"]
            authors = infos["bib"]["author"]
            year = infos["bib"]["pub_year"]
            abstract = infos["bib"]["abstract"]

            return {
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "year": year,
                "bibtex": bibtex
            }
        except:
            print("Can not acces bibtex")


if __name__ == "__main__":
    path = "article2.pdf"
    article = Article(path)
    print(article.metadata)