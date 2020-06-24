# Legacy Metro Data Format

This is the documentation of the original format of tokyo-metro-data which used two csv files:

## transitions.csv

Details which different identifiers one station has
and how much time it takes to change between platforms.
It is also used for connecting non-linear lines, like ring lines
or lines with forks.
The format is:

```
<line ID>;<station number>;<line ID>;<station number>;<transfer time in minutes>
```

Example:

```
F;01;Y;01;1
```

## lines.csv

Details which stations a line has and how long the it takes to travel from one to another station.
Does **not** work for line M or line E. The format is:

```
<line ID>;<first station's number>;<last station's number>;<time from first station to second>;<time from second station to third station>;…;<time from second-last to last station>
```

Example:

```
I;01;27;2;2; …;2
```

Note that empty lines and lines beginning with `#` must be ignored.

## Converting Legacy to Current Formats

### JSON based data
The script `legacy_to_json.py` converts the legacy files to the new
JSON format. All unknown values are set to `null`.

Make sure to change to this directory before running `python3 legacy_to_json.py`.

### Transition matrix based data
The script `legacy_to_matrix.py` converts the legacy files to the new
matrix transition format. All unknown values are set to `null`.

Make sure to change to this directory before running `python3 legacy_to_matrix.py`.
