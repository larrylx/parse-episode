from re import search


class Parse(object):
    def __init__(self, title: str, include: str = "", exclude: str = ""):
        self.title = title.upper()
        self.inc = include.upper()
        self.exc = exclude.upper()

    def get_episode(self) -> int:
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

        e = search(r"E{1}\d\d", self.title)
        if not e:
            return None

        e = e.group(0)
        e = e.strip("E")
        e = int(e)

        return e
