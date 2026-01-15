import asyncio 


async def worker(name, delay):
	print(f'start {name}')
	await asyncio.sleep(delay)
	print(f'end {name}')


async def main():
	t1 = asyncio.create_task(worker('A',2))
	t2 = asyncio.create_task(worker('B',1))
	
	print('tasks started')

	await t1
	await t2

	print('all done')



asyncio.run(main())

