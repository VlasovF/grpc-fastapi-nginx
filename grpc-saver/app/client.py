from __future__ import print_function

import logging
import grpc

from utils.random_document import get_document
import docs_pb2
import docs_pb2_grpc


def generate_document(n: int = 10):
    for _ in range(0, n):
        document = get_document()
        print(f"article_id: {document['article_id']}")
        yield docs_pb2.SaveDocumentRequest(**document)


def send_documents(stub):
    document_iterator = generate_document()
    response = stub.SaveDocuments(document_iterator)
    print(f"message: {response.message}")


def run():
    with grpc.insecure_channel("localhost:80") as channel:
        stub = docs_pb2_grpc.DocsSaverStub(channel)
        doc = get_document()
        response = stub.SaveDocument(docs_pb2.SaveDocumentRequest(**doc))
        print("message: " + response.message)
        send_documents(stub)


if __name__ == "__main__":
    logging.basicConfig()
    run()
