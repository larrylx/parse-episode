import requests
from bs4 import BeautifulSoup
from re import search
from typing import Union


class Scraper(object):
    def __init__(self,
                 search_title: str,
                 source_url: str = "https://dmhy.org",
                 header=None):
        self.url = source_url + "/topics/list/page/1?keyword="
        self.title = search_title
        if header is None:
            self.header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/81.0.4044.92 Safari/537.36 '
            }

    def get_series_list(self) -> list:
        try:
            respond = requests.get(self.url + self.title, self.header, timeout=0.01)
        except requests.exceptions.RequestException as e:
            print("Using Backup dmhy URL")
            respond = requests.get("https://dmhy.b168.net" + self.title, self.header, timeout=5)

        if respond.status_code != 200:
            print('Uable to Connect to dmhy')
            return []
        html = respond.content
        soup = BeautifulSoup(html, 'lxml')
        match = soup.find_all('tr')
        series_list = []
        for row in match[1:]:
            episode_dict = {}
            for link in row.find_all('a'):
                if not link:
                    continue
                elif 'html' in link['href'] and 'magnet' not in link['href']:
                    title = link.text.strip()
                    episode_dict["title"] = title
                elif 'magnet' in link['href'] and 'arrow-magnet' in link['class']:
                    episode_dict["link"] = link['href']
            series_list.append(episode_dict)
        return series_list


class Parse(object):
    def __init__(self, title: str, include: str = "", exclude: str = ""):
        self.title = title.upper()
        self.inc = include.upper()
        self.exc = exclude.upper()

    def get_episode(self) -> Union[None, int]:
        if self.inc:
            inc_list = self.inc.split(".")
            for keyword in inc_list:
                if keyword not in self.title:
                    return None

        if self.exc:
            exc_list = self.exc.split(".")
            for keyword in exc_list:
                if keyword in self.title:
                    return None

        e = search(r"【 *(\d\d)】", self.title)
        if e:
            return int(e.group(1))

        e = search(r"EP(\d\d)", self.title)
        if e:
            return int(e.group(1))

        return None
