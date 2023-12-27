import asyncio
import aiohttp
import httpx


class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()




async def send_request(url, client: aiohttp.ClientSession):
    response = await client.get(url)
    print("Status code", response.status_code)


async def get_comments():
    url = "http//164.92.64.76/desc/"
    async with httpx.AsyncClient() as client:
        tasks = [asyncio.create_task(send_request(url.format(i), client)) for i in range(1,300)]
        await asyncio.gather(*tasks)
for i in  range(1,10):
    with FileManager(f"descriptions/00{i}.txt",'r')
