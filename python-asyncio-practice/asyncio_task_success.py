import asyncio

async def main():

    tasks = []

    if tasks:
        await asyncio.gather(*tasks)

    print("SUCCESS")

asyncio.run(main())

Output
SUCCESS

Why?
No work was required.

Think:
User had no notifications
Nothing to process
Operation completed successfully
