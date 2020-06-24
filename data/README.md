# Legacy Metro Data Format

This is the documentation for the data used to generate `stations.json`

##Notes:

All transition times that have numerical duration 0 are considered unknown.

## transitions.csv

Details which transitions are possible from a given station.
It is also used for connecting non-linear lines, like ring lines
or lines with forks.
The format is:

```
From Station Letter, From Station Number, To Station Letter, To Station Number, Transition Type, Distance (km), Duration (s)
```

Example for a train based connection from F01 to Y01 that takes 60 seconds.

```
F,01,Y,01,1,0.0,80
```

## lines.csv

Details which stations a line has and how long the it takes to travel from one to another station. This system is suboptimal.
The format is:

```
Line Name, First station's number, Last station's number, distance from first station to second, distance from second station to third station, ..., distance from second-last to last station, time from first station to second, time from second station to third station, ..., time from second-last to last station
```

Example:

```
I,01,27, 0.3,0.2, ...,0.1, 60,120, ...,60
```

## types.csv

Lists known types of connections for `transitions.csv`.

## lines_eng/jap.csv

List with names of Lines in english and japanese.

## stations_eng/jap.csv

List with names of stations in english and japanese.
