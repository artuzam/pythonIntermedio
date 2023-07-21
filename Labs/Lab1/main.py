import concurrent.futures
import aiohttp
import asyncio
import time
import api
import ids


async def get_all_users_async():
    async with aiohttp.ClientSession() as session:
        tasks = [api.get_user_async(session, item) for item in ids.ids]
        await asyncio.gather(*tasks, return_exceptions=True)


def get_all_users_sync():
    for item in ids.ids:
        api.get_one_user(item)


def get_all_users_threading():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(api.get_one_user, ids.ids)


if __name__ == "__main__":
    start_time = time.time()
    # get_all_users_sync()
    # get_all_users_threading()
    asyncio.get_event_loop().run_until_complete(get_all_users_async())
    duration = time.time() - start_time
    print(f'La operación tardó: {format(duration, ".2f")} segundos')
