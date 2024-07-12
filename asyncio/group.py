import asyncio

async def fetch_data(id, sleep_time):
    print(f"coroutine {id} is started")
    await asyncio.sleep(sleep_time)

    return {"id" : id , "data" : f"sample data from coroutine : {id}"}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,4],1):
            task  = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]
    for result in results:
        print(f'Data result recieved : {result}')


asyncio.run(main())