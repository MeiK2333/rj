import hashlib
import random
import string
import time

from config.errcode import BadRequestException


def cf_url(method: str, params: dict, api_key: str, secret: str):
    base_url = "https://codeforces.com/api"
    rand = "".join(random.choice(string.hexdigits) for _ in range(6))
    params.update({"apiKey": api_key, "time": int(time.time())})
    uri = f"/{method}"
    for idx, key in enumerate(sorted(params.keys())):
        if idx == 0:
            uri += f"?{key}={params[key]}"
        else:
            uri += f"&{key}={params[key]}"
    hashcode = hashlib.sha512(f"{rand}{uri}#{secret}".encode()).hexdigest()
    api_sig = rand + hashcode
    url = base_url + uri + f"&apiSig={api_sig}"
    return url


def cf_response(resp: dict) -> dict:
    if resp["status"] == "OK":
        return resp["result"]
    raise BadRequestException(resp["comment"])
