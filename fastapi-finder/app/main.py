from typing import List

from fastapi import FastAPI
from pysondb import getDb
from pydantic import BaseModel

from config import settings

app = FastAPI()
db = getDb(settings.base_path)


class MultiDocumentsRequest(BaseModel):
    article_ids: List[int]


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/document/{article_id}")
def get_document(article_id: int):
    document = db.getByQuery(query={"articleId": article_id})
    return {"document": document}


@app.post("/document")
def get_documents(ids: MultiDocumentsRequest):
    documents = []
    for article_id in ids.article_ids:
        document = db.getByQuery(query={"articleId": article_id})
        documents += document
    return {"documents": documents}
