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

None. `tokyo-metro-data` is public domain.
