import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / "env")


class API:
    ENDPOINT = "https://api.notion.com/v1"
    HEADERS = {
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": f'Bearer {os.getenv("NOTION_KEY")}'
    }

    @staticmethod
    def addArticle(database_id, data):
        createUrl = 'https://api.notion.com/v1/pages'
        newPageData = {
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "Title": {
                    "title": [{
                        "text": {
                            "content": data["title"]
                        }
                    }]
                },
                "Done": {
                    "checkbox": False
                },
                "Authors": {
                    "rich_text": [{
                        "text": {
                            "content": data["authors"]
                        }
                    }]
                },
                "Year": {
                    "rich_text": [{
                        "text": {
                            "content": data["date"]
                        }
                    }]
                },
                "Abstract": {
                    "rich_text": [{
                        "text": {
                            "content": data["abstract"]
                        }
                    }]
                }
            }
        }

        data = json.dumps(newPageData)
        # print(str(uploadData))
        res = requests.request("POST",
                               createUrl,
                               headers=API.HEADERS,
                               data=data)
        print(res.status_code)
        print(res.text)


if __name__ == "__main__":
    database_id = "db99131281c946e2b9aa50af8bc08577"
    data = {
        "title": "Diffusion",
        "authors": "Me",
        "date": "20/10/2030",
        "abstract": "Nice stuffs"
    }

    API.addArticle(database_id, data)