# Tokyo Metro Data

Data detailing Tokyo's Metro network, derived from the line plan and signs.

You can help by improving it! For example, transfer times for example are only placeholders for now.

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
