#!/usr/bin/env python
 
import asyncio
import aiohttp
import re
from sys import argv
 
def get_links(body: str):
    links = re.findall('"((http)?://.*?)"', body)
    return links  
 
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
 
 
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, argv[1])
        #get_links(html)
        found_links = get_links(html)
        try:
            for links in found_links:
                print(await fetch(session, links[0]))
        except aiohttp.client_exceptions.ClientConnectorError:
            pass
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
