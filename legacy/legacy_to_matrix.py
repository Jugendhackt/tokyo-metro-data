# This script converts data.station.csv and data.lines.csv to
# matrix graph like data.generated.csv data format.

##### DO NOT EDIT data.generated.csv #####

import numpy as np
import csv

class StationRelation:
    def __init__(self, stationOne, stationTwo, stationTime):
        self.stationOne = stationOne
        self.stationTwo = stationTwo
        self.stationTime = stationTime

stations = []
relations = []

def station_string(station):
    return station[0] + ("0" if station[1] < 10 else "") + str(station[1])

file_lines = open('lines.csv')
for line in file_lines:
    line = line.split(';')
    prefix  = line[0]
    start   = int(line[1])
    end     = int(line[2])
    times    = line[3:]
    for i in range(start, end + 1):
        stations.append((prefix, i))

        relations.append(StationRelation((prefix, i),
                     (prefix, i),
                     0))  # 0 for itself

        if i != start:
            relations.append(StationRelation(
                             (prefix, i-1),
                             (prefix, i+0),
                             int(times[i - 1 - start])))

file_lines = open('transitions.csv')
for line in file_lines:
    if (line[0] == "#"[0]): continue;
    if (line.isspace()): continue;
    line = line.split(';')
    prefix1  = line[0]
    number1  = int(line[1])
    prefix2  = line[2]
    number2  = int(line[3])
    time     = int(line[4])
    relations.append(StationRelation((prefix1, number1), (prefix2, number2), time))

header_line = ""

for station in stations:
    header_line += station_string(station) + ";"

# Remove last simicolon from header line
header_line = header_line[:-1]

# Generate staion_size x station_size filled with -1's
matrix = np.ones(shape=(len(stations), len(stations))) * -1;

# Replace all relations in matix
for relation in relations:
    one_index = stations.index(relation.stationOne)
    two_index = stations.index(relation.stationTwo)
    matrix[one_index][two_index] = relation.stationTime;
    matrix[two_index][one_index] = relation.stationTime;

# Write the matrix in csv format
output = open('../transition-matrix.csv', "w+")
output.writelines(header_line)
output.write('\n')
for column in range(0, len(stations)):
    for row in range(0, len(stations)):
        output.write(str(matrix[column][row]))
        output.write(';' if row != len(stations) - 1 else '')
    output.write('\n')
print("Done!")
