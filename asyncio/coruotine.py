import asyncio

async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data":"Some Data"} 
async def main():
    result = await fetch_data(4)
    print(f"hello world this is asyncio : {result}")

asyncio.run(main())