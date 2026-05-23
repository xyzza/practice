import asyncio

async def slow():
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        return 'cancelled'


async def main():
    t1 = asyncio.create_task(slow())
    t2 = asyncio.create_task(slow())

    try:
        # Устанавливаем очень короткий timeout
        res = await asyncio.wait_for(
            asyncio.gather(t1, t2, return_exceptions=True),
            timeout=0.1
        )
    except asyncio.TimeoutError:
        # При timeout задачи автоматически отменяются
        res = await asyncio.gather(t1, t2, return_exceptions=True)

    print(all(r == 'cancelled' for r in res))
    return res

print(asyncio.run(main()))
