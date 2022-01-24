# parse-episode

Parse episode from a TV show file name or title.

## Use Example:
```Python
>>>parse = Parse("The.Book.of.Boba.Fett.S01E03.Chapter.3.2160p.WEB-DL.DDP5.1.Atmos.DV.MKV.x265")
>>>print(parse.get_episode())
3

>>>parse = Parse("The.Rookie.S04E12.The.Knock.1080p.AMZN.WEBRip.DDP5.1.x264")
>>>print(parse.get_episode())
12

# You can also use include or exclude to control keyword

>>>parse = Parse("The.Rookie.S04E12.The.Knock.1080p.AMZN.WEBRip.DDP5.1.x264", include = "2160p")
>>>print(parse.get_episode())
None

>>>parse = Parse("The.Book.of.Boba.Fett.S01E03.Chapter.3.2160p.WEB-DL.DDP5.1.Atmos.DV.MKV.x265-ShowkotKebabaGhar[rartv]", exclude = "2160P")
>>>print(parse.get_episode())
None
```