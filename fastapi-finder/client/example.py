import asyncio

from api_client import ApiClient


api = ApiClient('http://localhost/api')

async def get_documents(ids):
    res = await api.get_documents(ids)
    print(res['documents'][0]['articleId'])


asyncio.run(get_documents([3024790]))
