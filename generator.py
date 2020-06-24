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
    def inner(fro, to, type, dur):
        entry = {
            "name_en": str(names_eng.get(fro)),
            "name_jp": str(names_jap.get(fro)),
            "connections": []
        }
        try:
            entry = metro_map[fro]
        except KeyError:
            pass

        conn = {
            "target_id": to,
            "type": type,
            "duration": dur
        }
        entry["connections"] += [conn]
        metro_map[fro] = entry
        return metro_map

    return inner

# Open source files
transitions = open("data/transitions.csv")
lines = open("data/lines.csv")

# Load transition types
default_type = 1
types = {}
with open("data/types.csv") as types_file:
    for line in parse_csv(types_file.read(), ","):
        types[int(line[0])] = line[1]

# Load station names (english)
names_eng = {}
names_jap = {}
with open("data/names_eng.csv") as types_file:
    for line in parse_csv(types_file.read(), ","):
        names_eng[station_id(line[0], int(line[1]))] = line[2]

# Structure to hold the read information
# This will be dumped as stations.json at the end
metro_map = {}
add_conn = add_connection(metro_map)

# Read lines.csv and append all transitions to metro_map
for line in parse_csv(lines.read(), ","):
    char = line[0]
    first = int(line[1])
    last = int(line[2])
    rides = list(map(int, line[3:]))

    for station_number in range(first, last):
        time = rides[station_number - first]
        station_a = station_id(char, station_number)
        station_b = station_id(char, station_number + 1)
        metro_map = add_conn(station_a, station_b, types[default_type], time)
        metro_map = add_conn(station_b, station_a, types[default_type], time)

# Read transitions.csv and append all transitions to metro_map
# Line format is: From Station Letter, From Station Number, To Station Letter, To Station Number, type, duration
for transition in parse_csv(transitions.read(), ","):
    station1 = station_id(transition[0], int(transition[1]))
    station2 = station_id(transition[2], int(transition[3]))
    type = int(transition[4])
    time = int(transition[5])

    metro_map = add_conn(station1, station2, types[type], time)
    metro_map = add_conn(station2, station1, types[type], time)

print("Dumping...")
file = open("stations.json", "w+")
file.write(json.dumps(metro_map, indent=4, sort_keys=True))
file.close()

