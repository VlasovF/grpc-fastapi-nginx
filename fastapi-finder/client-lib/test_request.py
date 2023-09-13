from typing import List 

import aiohttp
import asyncio



async def get_documents(article_ids: List[int]):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost/api/document', json={'article_ids': article_ids}) as resp:
            res = await resp.text()
            return res

async def main():
    documents = await get_documents([12, 23])
    print(documents)


asyncio.run(main())
