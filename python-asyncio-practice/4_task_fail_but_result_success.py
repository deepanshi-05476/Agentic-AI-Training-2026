import asyncio

async def task():
    raise Exception("failed")

async def main():

    results = await asyncio.gather(
        task(),
        task(),
        task(),
        task(),
        return_exceptions=True
    )

    print("SUCCESS")
    print(results)

asyncio.run(main())

Output
SUCCESS
[
 Exception('failed'),
 Exception('failed'),
 Exception('failed'),
 Exception('failed')
]

Why?
Because the business rule says:
Ignore task failures
System success is independent
