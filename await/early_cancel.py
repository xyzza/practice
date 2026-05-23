import asyncio

async def worker(i):
    await asyncio.sleep(0.1)
    return i

async def main():
    tasks = [asyncio.create_task(worker(i)) for i in range(3)]
    try:
        # ранний выход из-за ошибки
        raise RuntimeError('stop early')
    except:
        for t in tasks: t.cancel()
        # важно: дождаться, чтобы не было pending
        res = await asyncio.gather(*tasks, return_exceptions=True)
        print(all(isinstance(x, asyncio.CancelledError) for x in res))

asyncio.run(main())
