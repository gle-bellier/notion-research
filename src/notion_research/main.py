from notion_research.notion import API
import textract
# from reader import Article
# from pathlib import Path
# from watchdog.observers import Observer
# import time


def is_article(path):
    print(path)
    text = str(textract.process(str(path)))
    return "arXiv" in text[:1000]


if __name__ == "__main__":

    bibtex_file = "biblio.bib"
    watch_path = Path.home() / "Téléchargements"
    destination_path = Path.home() / "Documents/research/articles"

    event_handler = MyHandler(watch_path, destination_path, is_article)
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()

    # name = "article.pdf"

    # text = str(textract.process(PATH + name))
    # article = Article(text)
    # print(article.metadata)

    # # Add bibtex to the bib file :
    # with open(SAVING_PATH + bibtex_file, "a") as file:
    #     file.write(article.metadata["bibtex"] + "\n")

    # # database_id = "db99131281c946e2b9aa50af8bc08577"
    # # data = {
    # #     "title": article.metadata["title"],
    # #     "authors": article.metadata["authors"],
    # #     "date": article.metadata["year"],
    # #     "abstract": article.metadata["abstract"],
    # # }

    # # API.addArticle(database_id, data)