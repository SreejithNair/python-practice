import asyncio, time

async def do_async():
    print(f'{time.ctime()} hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} goodbye!')

asyncio.run(do_async())
