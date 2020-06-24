import simplejson as json

# Parse CSV file and return a list of lists
def parse_csv(text, sep):
    lines = list(map(lambda t: t.strip(), text.split("\n")))
    lines = list(filter(lambda l: l != "" and l[0] != "#", lines))
    return list(map(lambda l: l.split(sep), lines))

# Makes station names uniform. For example M,1 and M,01 are turned to M01
def station_id(char, number):
    return char + ("0" if number < 10 else "") + str(number)

# Add connection to metro map structure
def add_connection(metro_map):
    def inner(fro, to, type, dis, dur):
        entry = {
            "name_en": str(stations_eng.get(fro)),
            "name_jp": str(stations_jap.get(fro)),
            "connections": []
        }
        try:
            entry = metro_map[fro]
        except KeyError:
            pass

        conn = {
            "target_id": to,
            "type_id": type,
            "type": types.get(type),
            "duration": dur,
            "distance": dis
        }
        entry["connections"] += [conn]
        metro_map[fro] = entry
        return metro_map

    return inner

# Open source files
transitions = open("data/transitions.csv", encoding="utf8")
lines = open("data/lines.csv", encoding="utf8")

# Load transition types
default_type = 1
types = {}
with open("data/types.csv", encoding="utf8") as types_file:
    for line in parse_csv(types_file.read(), ","):
        types[int(line[0])] = line[1]

# Load station names (english)
stations_eng = {}
stations_jap = {}
with open("data/stations_eng.csv", encoding="utf8") as types_file:
    for line in parse_csv(types_file.read(), ","):
        stations_eng[station_id(line[0], int(line[1]))] = line[2]
with open("data/stations_jap.csv", encoding="utf8") as types_file:
    for line in parse_csv(types_file.read(), ","):
        stations_jap[station_id(line[0], int(line[1]))] = line[2]

# Load line names (english)
lines_names = {}
with open("data/lines_eng.csv", encoding="utf8") as lines_file:
    for line in parse_csv(lines_file.read(), ","):
        lines_names[line[0]] = {}
        lines_names[line[0]]["name_en"] = line[1]
with open("data/lines_jap.csv", encoding="utf8") as lines_file:
    for line in parse_csv(lines_file.read(), ","):
        lines_names[line[0]]["name_jp"] = line[1]

# Structure to hold the read information
# This will be dumped as stations.json at the end
metro_map = {}
add_conn = add_connection(metro_map)

# Read lines.csv and append all transitions to metro_map
for line in parse_csv(lines.read(), ","):
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
        metro_map = add_conn(station_a, station_b, default_type, distance, duration)
        metro_map = add_conn(station_b, station_a, default_type, distance, duration)

# Read transitions.csv and append all transitions to metro_map
# Line format is: From Station Letter, From Station Number, To Station Letter, To Station Number, type, duration
for transition in parse_csv(transitions.read(), ","):
    station1 = station_id(transition[0], int(transition[1]))
    station2 = station_id(transition[2], int(transition[3]))
    type = int(transition[4])
    distance = float(transition[5])
    duration =   int(transition[6])

    metro_map = add_conn(station1, station2, type, distance, duration)
    metro_map = add_conn(station2, station1, type, distance, duration)

print("Dumping...")
dumpformat = {}
dumpformat["lines"] = lines_names
dumpformat["stations"] = metro_map
dumpformat["transition_types"] = types
file = open("stations.json", "w+", encoding="utf8")
file.write(json.dumps(dumpformat, indent=4, sort_keys=True, ensure_ascii=False))
file.close()

