from re import search
from typing import Union


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

        e = search(r"E(\d\d)", self.title)
        if e:
            return int(e.group(1))

        e = search(r"【 *(\d\d)】", self.title)
        if e:
            return int(e.group(1))

        e = search(r"EP(\d\d)", self.title)
        if e:
            return int(e.group(1))

        e = search(r"第(\d+)集", self.title)
        if e:
            return int(e.group(1))

        e = search(r"\W(\d\d)\W", self.title)
        if e:
            return int(e.group(1))

        e = search(r" (\d\d) ", self.title)
        if e:
            return int(e.group(1))

        return ""
