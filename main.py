import asyncio
import random
import aiohttp
import json
import time


async def get_json(id: int, api_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        url = f'https://reqres.in/api/{api_name}/{id}'
        async with session.get(url) as response:
            json_data = await response.json()
            if not json_data:
                print('Big id', id)
                return
            return json_data


async def main():
    tasks = []
    api_names = ['unknown', 'users']

    for api_name in api_names:
        for id in range(1, 11):
            tasks.append(asyncio.create_task(get_json(id, api_name)))

    result = []

    for task in tasks:
        result.append(await task)

    return result


def create_files(data_files):
    for data in data_files:
        with open(f'json_test/json_data_{time.time() * random.randint(1, 25)}', 'w') as file:
            json.dump(data, file, indent=3)


if __name__ == '__main__':
    res = asyncio.run(main())
    create_files(res)
