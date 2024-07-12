import asyncio

async def fetch_data(id, sleep_time):
    print(f"coroutine {id} is started")
    await asyncio.sleep(sleep_time)

    return {"id" : id , "data" : f"sample data from coroutine : {id}"}

async def main():
    results = await asyncio.gather(fetch_data(1,10),fetch_data(2,3),fetch_data(3,3))
    for result in results:
        print(f"recieved result : {result}")

asyncio.run(main())