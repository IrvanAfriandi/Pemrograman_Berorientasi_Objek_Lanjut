import asyncio
async def my_async_generator():
    data = [1, 2, 3]
    for item in data:
        yield item
    raise StopAsyncIteration

async def main():
    async for value in my_async_generator():
        print(value)

asyncio.run(main())
