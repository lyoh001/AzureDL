import asyncio
import json
import logging

import aiohttp
import azure.functions as func


async def fetch(session, page):
    async with session.get(url=f"https://swapi.dev/api/people?page={page}") as resp:
        return (await resp.json())["results"]

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    async with aiohttp.ClientSession() as session:
        # result = await asyncio.gather(*(fetch(session, page) for page in range(1, 10)))
        return func.HttpResponse(
            status_code=200,
            body=f"{(req.get_json())}",
        )
        # return func.HttpResponse(
        #     body=json.dumps({"text": f"{result}"}, indent=4)
        # )
