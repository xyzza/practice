import asyncio


async def work(i, delay=0.001):
    await asyncio.sleep(delay)
    print(f"job {i} done")


async def main():
    t1 = asyncio.create_task(work(1))
    t2 = asyncio.create_task(work(2, 0))
    t3 = asyncio.create_task(work(3))
    await asyncio.sleep(0.1)
    await t2


asyncio.run(main())