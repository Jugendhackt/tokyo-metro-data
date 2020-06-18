# Tokyo Metro Data

Data detailing Tokyo's Metro network, derived from the line plan and signs.

You can help by improving it!

# Data formats

## JSON based data
The stations.json contains all currently known information. This includes the stations names in english and japanese as well all connections departing a station.

### Data shema
The following is an example an entry in stations.json:
```json
{
  ...
  "C04" : {
        "name_en": null,
        "name_jp": null,
        "connections": [
            {
                "duration": 1,
                "target_id": "C03",
                "type": "ride"
            },
            {
                "duration": 2,
                "target_id": "C05",
                "type": "ride"
            },
            {
                "duration": 3,
                "target_id": "G02",
                "type": "walk"
            },
            {
                "duration": 3,
                "target_id": "Z02",
                "type": "walk"
            }
        ]
    },
  ...
}
```

## Matrix transition format
The transitions.csv contains the transition times in a easy to compute with matrix format.
The header contains the the station names for each column

# Projects using this data
*Feel free to add your project!*

* [Underground Meetup](https://github.com/Jugendhackt/undergroundmeetup/)

# License

None. `tokyo-metro-data` is public domain.
