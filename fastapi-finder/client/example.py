import asyncio

from api_client import ApiClient


api = ApiClient('http://localhost/api')


async def get_documents(ids):
    res = await api.get_documents(ids)
    print([document['articleId'] for document in res['documents']])


asyncio.run(get_documents([8297165, 1793841, 8671600]))
