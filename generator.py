import simplejson as json

# Parse CSV file and return a list of lists
def parse_csv(text, sep=","):
    lines = list(map(lambda t: t.strip(), text.split("\n")))
    lines = list(filter(lambda l: l != "" and l[0] != "#", lines))
    return list(map(lambda l: l.split(sep), lines))

# Makes station names uniform. For example M,1 and M,01 are turned to M01
def station_id(char, number):
    return char + ("0" if number < 10 else "") + str(number)

# Load station names (english and japanese for use in add_connections)
stations_eng = {}
stations_jap = {}
with open("data/stations_eng.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        stations_eng[station_id(line[0], int(line[1]))] = line[2]
with open("data/stations_jap.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        stations_jap[station_id(line[0], int(line[1]))] = line[2]

# Load transition types (for use in add_connections)
default_type = 1
types = {}
with open("data/types.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        types[int(line[0])] = line[1]

# Add connection to stations structure
def add_connection(container):
    def inner(origin, destination, typ, dist, dur):
        entry = {
            "name_en": str(stations_eng.get(origin)),
            "name_jp": str(stations_jap.get(origin)),
            "connections": []
        }
        try:
            entry = container[origin]
        except KeyError:
            pass

        conn = {
            "target_id": destination,
            "type_id": typ,
            "type": types.get(typ),
            "duration": dur,
            "distance": dist
        }
        entry["connections"] += [conn]
        container[origin] = entry
        return container

    return inner
# Structure to hold the read information
stations = {}
add_station = add_connection(stations)

# Add line to line structure
def add_line(container):
    def inner(station, l_key, name):
        entry = {
            "name_en": "",
            "name_jp": ""
        }
        try:
            entry = container[station]
        except KeyError:
            pass

        entry[l_key] = name
        container[station] = entry
        return container

    return inner
# Structure to hold the line information
lines = {}
add_line = add_line(lines)


# Load line names (english)
with open("data/lines_eng.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        add_line(line[0], "name_en", line[1])

# Load line names (japanese)
with open("data/lines_jap.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        add_line(line[0], "name_jp", line[1])

# Read lines.csv and append all transitions to metro_map
with open("data/lines.csv", encoding="utf8") as c_file:
    for line in parse_csv(c_file.read()):
        char = line[0]
        first = int(line[1])
        last = int(line[2])

        distances = list(map(float, line[3:3+last-first])) # first n entries are distances in km
        durations = list(map(int  , line[3+last-first:]))  # next  n entries are durations in s

        for station_number in range(first, last):
            distance = distances[station_number - first]
            duration = durations[station_number - first]
            station_a = station_id(char, station_number)
            station_b = station_id(char, station_number + 1)
            stations = add_station(station_a, station_b, default_type, distance, duration)
            stations = add_station(station_b, station_a, default_type, distance, duration)

# Read transitions.csv and append all transitions to metro_map
with open("data/transitions.csv", encoding="utf8") as c_file:
    for transition in parse_csv(c_file.read()):
        station1 = station_id(transition[0], int(transition[1]))
        station2 = station_id(transition[2], int(transition[3]))
        type = int(transition[4])
        distance = float(transition[5])
        duration =   int(transition[6])

        stations = add_station(station1, station2, type, distance, duration)
        stations = add_station(station2, station1, type, distance, duration)

print("Dumping...")
dumpformat = {}
dumpformat["lines"] = lines
dumpformat["stations"] = stations
dumpformat["transition_types"] = types
file = open("stations.json", "w+", encoding="utf8")
file.write(json.dumps(dumpformat, indent=4, sort_keys=True, ensure_ascii=False))
file.close()

