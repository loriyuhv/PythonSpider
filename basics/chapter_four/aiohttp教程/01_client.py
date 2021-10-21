import asyncio
import aiohttp

url = 'http://httpbin.org/get'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
