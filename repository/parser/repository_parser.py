from bs4 import BeautifulSoup
from typing import List
import requests


def parser(user_str: str) -> List:
    try:
        with requests.get(
            f'https://libeldoc.bsuir.by/simple-search?location=&query={user_str}'
            f'&rpp=1000&sort_by=dc.date.issued_dt&order=DESC&etal=0'
        ) as response:
            item_list = BeautifulSoup(response.content, "html.parser").find("div", "panel-info").find_all("tr")

            item_list.remove(item_list[0])
            repository_api = []

            for item in item_list:
                repository_api.append({
                    'year': item.findNext().getText(),
                    'author': item.find("td", {"headers": "t3"}).find_next().getText(),
                    'title': item.find("td", {"headers": "t2"}).getText(),
                    'url': f'https://libeldoc.bsuir.by/{item.find("td", {"headers": "t2"}).find("a").get("href")}',
                })

            return repository_api
    except AttributeError:
        return []
