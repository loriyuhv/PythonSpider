import aiohttp
import asyncio

# url = 'http://python.org'
#
#
# async def fetch(client):
#     async with client.get(url) as resp:
#         assert resp.status == 200
#         return await resp.text()
#
#
# async def main():
#     async with aiohttp.ClientSession() as client:
#         html = await fetch(client)
#         print(html)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# client_session = aiohttp.ClientSession(raise_for_status=False)
# resp = await client_session.get(url, raise_for_status=False)
# async with resp:
#     assert resp.status == 200


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print(resp.status)
            print(type(await resp.text()))
            print(type(await resp.read()))

asyncio.run(main())
