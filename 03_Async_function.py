import asyncio

async def func2():
    print('Result of an async function.')
    
async def func1():
    await func2()

asyncio.run(func1())