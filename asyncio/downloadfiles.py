import aiohttp
import asyncio
class SThreeConnection(object):

    def __init__(self):
        pass

    async def __aenter__(self):
        self.connection = aiohttp.ClientSession()
        return self.connection

    async def __aexit__(self, exe_type, exc, tb):
        await self.connection.close()
    
    async def download_file(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        assert response.status == 200
        return url, await response.read()

async with SThreeConnection() as s3:


        

async def download_file(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        assert response.status == 200
        # For large files use response.content.read(chunk_size) instead.
        return url, await response.read()

async def main():
    # Schedule three calls *concurrently*:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            download_file(session,'http://cnn.com'),
            download_file(session, 'http://google.com')
    )
loop = asyncio.get_event_loop()
task = loop.create_task(main())
result = loop.run_until_complete(task)
print(result)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()