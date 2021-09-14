from notion import API
import textract
from reader import Article

if __name__ == "__main__":
    PATH = ""
    SAVING_PATH = "articles/"

    bibtex_file = "biblio.bib"

    name = "article.pdf"

    text = str(textract.process(PATH + name))
    article = Article(text)
    print(article.metadata)

    # Add bibtex to the bib file :
    with open(SAVING_PATH + bibtex_file, "a") as file:
        file.write(article.metadata["bibtex"] + "\n")

    # database_id = "db99131281c946e2b9aa50af8bc08577"
    # data = {
    #     "title": article.metadata["title"],
    #     "authors": article.metadata["authors"],
    #     "date": article.metadata["year"],
    #     "abstract": article.metadata["abstract"],
    # }

    # API.addArticle(database_id, data)