from concurrent import futures
import logging

import grpc
import docs_pb2
import docs_pb2_grpc


class DocsSaver(docs_pb2_grpc.DocsSaver):
    def SaveDocument(self, request, context):
        print(f"One document article_id: {request.article_id}")
        return docs_pb2.SaveDocumentReply(message="success")


    def SaveDocuments(self, request_iterator, context):
        for request in request_iterator:
            print(f"Article id: {request.article_id}")
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
