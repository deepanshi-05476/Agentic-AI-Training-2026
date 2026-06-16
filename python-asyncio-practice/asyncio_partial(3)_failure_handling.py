import asyncio

async def task1():
    return "Task1"

async def task2():
    raise Exception("Task2 failed")

async def task3():
    raise Exception("Task3 failed")

async def task4():
    raise Exception("Task4 failed")

async def main():

    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        task4(),
        return_exceptions=True
    )

    success_count = sum(
        1 for r in results
        if not isinstance(r, Exception)
    )

    if success_count >= 2:
        print("SUCCESS")
    else:
        print("FAILED")

    print(results)

asyncio.run(main())

Output
FAILED
['Task1', Exception(...), Exception(...), Exception(...)]

Because:
Success = 1
Failure = 3

Need at least 2 successes.
