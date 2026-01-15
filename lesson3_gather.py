import asyncio 
import time 


async def worker(name, delay):
	print(f'start {name}')
	await asyncio.sleep(delay)
	print(f'end {name}')
	return name

async def main():
	start_time = time.time()
	results = await asyncio.gather(
	worker('A',2),
	worker('B',1),
	worker('C',3),
	)
	
	end_time = time.time()
	print('resutls:',results)
	print('time:', round(end_time - start_time,2), 'seconds')

asyncio.run(main())
