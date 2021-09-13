from notion import API
from reader import Extractor

if __name__ == "__main__":

    database_id = "db99131281c946e2b9aa50af8bc08577"
    data = {
        "title": "Diffusion",
        "authors": "Me",
        "date": "20/10/2030",
        "abstract": "Nice stuffs"
    }

    API.addArticle(database_id, data)