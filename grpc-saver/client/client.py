from __future__ import print_function
from typing import List
import grpc

import docs_pb2
import docs_pb2_grpc


class DocsSaverClient:

    def __init__(self, server_url):
        self.url = server_url


    def send_document(self, document: dict) -> str:
        with grpc.insecure_channel(self.url) as channel:
            stub = docs_pb2_grpc.DocsSaverStub(channel)
            response = stub.SaveDocument(docs_pb2.SaveDocumentRequest(**document))

        return response.message


    def send_documents(self, documents: List[dict]) -> str:
        
        def document_iterator(docs):
            for doc in docs:
                yield docs_pb2.SaveDocumentRequest(**doc)

        with grpc.insecure_channel(self.url) as channel:
            stub = docs_pb2_grpc.DocsSaverStub(channel)
            iterator = document_iterator(documents)
            response = stub.SaveDocuments(iterator)

        return response.message
