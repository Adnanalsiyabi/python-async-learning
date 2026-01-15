import asyncio
import aiohttp
""" 
async with session.get(url) safely opens and closes a network connection without blocking, and await response.text() pauses the task while data arrives instead of freezing the program.

"""

URLS = [
    "https://example.com",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/get",
]

async def fetch(session, url):
		async with session.get(url) as response: # without async we cannot make the opition for cnneciont or closing may waitrequests.get 
			text = await response.text()
			print(f'{url} = {len(text)} chars')


async def main():
	async with aiohttp.ClientSession() as session:
		await asyncio.gather(
			*(fetch(session, url) for url in URLS)
		)



asyncio.run(main())
