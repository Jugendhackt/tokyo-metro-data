<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jugendhackt/tokyo-metro-data?style=flat-square"> <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/jugendhackt/tokyo-metro-data?style=flat-square"> <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/jugendhackt/tokyo-metro-data?style=flat-square"> <img alt="GitHub stars" src="https://img.shields.io/github/stars/jugendhackt/tokyo-metro-data?style=flat-square">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Tokyo_Metro_2_logo.svg/1200px-Tokyo_Metro_2_logo.svg.png" align="right" width="200" />

# Tokyo Metro Data

Data detailing Tokyo's Metro network, derived from the line plan and signs as well as tokyometro.jp.

You can help by improving it!

# Data formats

## JSON based data
[Stations.json](stations.json) contains all currently known information. This includes the stations names in english and japanese as well all connections departing a station.

The following should explain stations.json:
```json
{
    "lines": {
        ...
        "A": {
            "name_en": "Asakusa Line",
            "name_jp": "浅草線"
        },
        "C": {
            "name_en": "Chiyoda Line",
            "name_jp": "千代田線"
        },
        ...
    },
    "stations": {
        ...
        "E27": {
            "connections": [
                {
                    "duration": 0,
                    "target_id": "E26",
                    "type": "ride",
                    "type_id": 1
                },
                {
                    "duration": 0,
                    "target_id": "E28",
                    "type": "ride",
                    "type_id": 1
                },
                {
                    "duration": 0,
                    "target_id": "E01",
                    "type": "walk",
                    "type_id": 0
                },
                {
                    "duration": 0,
                    "target_id": "S01",
                    "type": "walk",
                    "type_id": 0
                },
                {
                    "duration": 0,
                    "target_id": "M08",
                    "type": "walk",
                    "type_id": 0
                }
            ],
            "name_en": "Shinjuku",
            "name_jp": "None"
        },
        ...
    },
    "transition_types": {
        "0": "walk",
        "1": "ride",
        "2": "ground"
    }
}
```

## Things to do

As of yet there are a few things missing:

- [x] Adding all japanese station names to [stations_jap.csv](data/stations_jap.csv)
- [ ] Replace duration with distance
- [ ] Add durations (listed on wikipedia)
- [ ] Add a transition like file for duration
- [ ] General code cleanup in generator.py (maybe some progress output?)
- [ ] Adding connections to non-metro transport systems (e.g. train stations or airports)

## Contributors

You can add yourself here after contributing something!

<a href="https://github.com/StoneLabs"><img src="https://github.com/StoneLabs.png" title="StoneLabs" width="80" height="80"></a>
<a href="https://github.com/sternenseemann"><img src="https://github.com/sternenseemann.png" title="StoneLabs" width="80" height="80"></a>

# Projects using this data
*Feel free to add your project!*

* [Cool 2D visualization by unknown](https://doc.linkurio.us/ogma/latest/resources/import-json-custom.html)
* [Underground Meetup](https://github.com/Jugendhackt/undergroundmeetup/)

# License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
