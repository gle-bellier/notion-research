from notion import API
import textract
from reader import Article

if __name__ == "__main__":

    bibtex_file = ""
    PATH = ""
    name = "article2.pdf"

    text = str(textract.process(PATH + name))
    article = Article(text)
    print(article.metadata)

    database_id = "db99131281c946e2b9aa50af8bc08577"
    data = {
        "title": article.metadata["title"],
        "authors": article.metadata["authors"],
        "date": article.metadata["year"],
        "abstract": article.metadata["abstract"],
    }

    API.addArticle(database_id, data)