import aiohttp
from bs4 import BeautifulSoup

from platforms.codeforces.schema import UserInfo
from platforms.codeforces.util import cf_url, cf_response


async def login(handle: str, password: str):
    async with aiohttp.ClientSession() as session:
        login_url = "https://codeforces.com/enter?back=%2F"
        # 获取 csrf
        async with session.get(login_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, "html.parser")
            csrf = soup.find(class_="csrf-token").attrs["data-csrf"]
        async with session.post(
            login_url,
            data={
                "csrf_token": csrf,
                "action": "enter",
                "handleOrEmail": handle,
                "password": password,
                "_tta": "716",
            },
        ) as resp:
            content = await resp.text()
    return f'var handle = "{handle}";' in content

async def userinfo_async(handle: str, api_key: str, secret: str) -> UserInfo:
    url = cf_url("user.info", {"handles": handle}, api_key, secret)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.json()
    return UserInfo(**cf_response(result)[0])
