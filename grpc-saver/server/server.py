from concurrent import futures
import logging

import grpc
import docs_pb2
import docs_pb2_grpc
from google.protobuf.json_format import MessageToDict
from pysondb import getDb


db = getDb('storage/data.json')


class DocsSaver(docs_pb2_grpc.DocsSaver):
    def SaveDocument(self, request, context):
        document = MessageToDict(request)
        db.add(document)
        return docs_pb2.SaveDocumentReply(message="success")

    def SaveDocuments(self, request_iterator, context):
        documents = []
        for request in request_iterator:
            document = MessageToDict(request)
            documents.append(document)
        db.addMany(documents)
        return docs_pb2.SaveDocumentReply(message="success")


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    docs_pb2_grpc.add_DocsSaverServicer_to_server(DocsSaver(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on" + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
