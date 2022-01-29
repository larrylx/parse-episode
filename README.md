# parse-episode

- Parse episode from a TV show file name or title.
- Scrape TV series from DMHY.

You can install this package from [test.pipy.org](https://test.pypi.org/project/parse-episode/).

## Useage Example:
```Python
>>>from parse_episode import rarbg

>>>parse = rarbg.Parse("The.Book.of.Boba.Fett.S01E03.Chapter.3.2160p.WEB-DL.DDP5.1.Atmos.DV.MKV.x265")
>>>print(parse.get_episode())
3

>>>parse = rarbg.Parse("The.Rookie.S04E12.The.Knock.1080p.AMZN.WEBRip.DDP5.1.x264")
>>>print(parse.get_episode())
12

# You can also use include and/or exclude to specify what you want
# Put all keywords in single string and seprate by "."，case-insensitive.
# Example string: "S02.2160p.H264"

>>>parse = rarbg.Parse("The.Rookie.S04E12.The.Knock.1080p.AMZN.WEBRip.DDP5.1.x264", include = "2160p.H264")
>>>print(parse.get_episode())
None

>>>parse = rarbg.Parse("The.Book.of.Boba.Fett.S01E03.Chapter.3.2160p.WEB-DL.DDP5.1.Atmos.DV.MKV.x265-ShowkotKebabaGhar", exclude = "2160P")
>>>print(parse.get_episode())
None
```