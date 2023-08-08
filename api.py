import requests_async as requests


async def grab_scrobbles(endpoint):
    response = await requests.get(endpoint.rstrip("/") + '/apis/mlj_1/scrobbles', verify=False)
    return response.json()

def recent(response):
    if response['status'] == "ok":
        return response['list'][0]

