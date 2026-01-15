import asyncio
import aiohttp


URLS = URLS = ["httstartps://httpbin.org/delay/1"] * 10
MAX_CONCURRENT = 5

async def fetch(session, url, sem):
	async with sem:
		print(f'Start {url}')
		try:
			async with session.get(url) as response:
				text = await response.text()
				print(f'end {url} = {len(text)}')
				
		except Exception as e:
			print(e)


async def main():
	sem = asyncio.Semaphore(MAX_CONCURRENT)
	async with aiohttp.ClientSession() as session:
		tasks = [fetch(session, url, sem) for url in URLS]
		await asyncio.gather(*tasks)

asyncio.run(main())
