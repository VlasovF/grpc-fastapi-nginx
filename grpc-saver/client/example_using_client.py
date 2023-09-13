from pysondb import getDb

from client import DocsSaverClient
from utils.random_document import get_document


def main():
    grpc_server_path = "localhost:80"
    docs_saver_client = DocsSaverClient(grpc_server_path)
    
    # Saving one document
    document = get_document()
    article_id = document['article_id']
    title = document['title']
    print(f"Sending document with article_id {article_id} and title {title}")
    docs_saver_client.send_document(document)

    # Saving many documents
    documents = [get_document() for _ in range(0, 10)]
    print(f"Saving many. Articles ids:")
    print([document['article_id'] for document in documents])
    docs_saver_client.send_documents(documents)


if __name__ == "__main__":
    main()
