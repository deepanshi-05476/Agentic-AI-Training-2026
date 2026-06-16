import asyncio

async def task1():
    await asyncio.sleep(1)
    return "Task1"

async def task2():
    await asyncio.sleep(1)
    raise Exception("Task2 Failed")

async def task3():
    await asyncio.sleep(1)
    return "Task3"

async def task4():
    await asyncio.sleep(1)
    return "Task4"

async def main():
    try:
        results = await asyncio.gather(
            task1(),
            task2(),
            task3(),
            task4()
        )
        print(results)

    except Exception as e:
        print("ALL FAILED:", e)

asyncio.run(main())

Output
ALL FAILED: Task2 Failed

Rule
1 fail -> whole operation fail
4 pass -> success
