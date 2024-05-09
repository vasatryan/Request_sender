import sys
import asyncio
import aiohttp
import random
import string

async def send_post_request(session, url, payload):
    async with session.post(url, json=payload) as response:
        return response

def email_gen():
    sym = string.ascii_letters + string.digits
    email = ''.join(random.choice(sym) for _ in range(10))
    email += "@vault.com"
    return email

async def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <count>")
        return

    url = sys.argv[1]
    try:
        count = int(sys.argv[2])
    except ValueError:
        print("Count must be an integer.")
        return

    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(count):
            email = email_gen()
            print(email)
            payload = {} # Needed request body
            tasks.append(asyncio.create_task(send_post_request(session, url, payload)))
        responses = await asyncio.gather(*tasks)
        # print(responses)  # Print all responses if needed

if __name__ == "__main__":
    asyncio.run(main())
