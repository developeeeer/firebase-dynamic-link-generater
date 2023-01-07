import requests
from config import settings


def update_link(link: str):
    params = settings.DEFAULT_PARAMS
    params["dynamicLinkInfo"]["link"] = link
    return params


def generate_dynamic_link(link: str) -> str:
    try:
        if not("https://" in link or "http://" in link):
            raise Exception("require https:// or http://")

        params = update_link(link)
        response = requests.post(
            url=settings.END_POINT,
            headers=settings.HEADERS,
            json=params
        ).json()
        return response["shortLink"]
    except Exception as err:
        print(err)


def generate_long_dynamic_link(link) -> str:
    try:
        params = settings.DEFAULT_PARAMS_LONG_DYNAMIC_LINK
        params["longDynamicLink"] =f'{params["longDynamicLink"]}&link={link}'
        p = update_link("https://service.onereco.jp/")
        response = requests.post(
            url=settings.END_POINT,
            headers=settings.HEADERS,
            json=p
        ).json()
        return response["shortLink"]
    except Exception as err:
        print(err)
