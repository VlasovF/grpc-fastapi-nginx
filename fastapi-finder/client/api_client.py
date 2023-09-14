from typing import List
import json

import aiohttp


class ApiClient:

    def __init__(self, api_url):
        self.url = api_url

    async def get_documents(self, article_ids: List[int]):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url + '/document',
                                    json={'article_ids': article_ids}) as resp:
                res = await resp.text()
                return json.loads(res)
