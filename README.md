# Tokyo Metro Data

Data detailing Tokyo's Metro network, derived from the line plan and signs as well as tokyometro.jp.

You can help by improving it!

# Data formats

## JSON based data
The stations.json contains all currently known information. This includes the stations names in english and japanese as well all connections departing a station.

### Data shema
The following is an example an entry in stations.json:
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

# Projects using this data
*Feel free to add your project!*

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
