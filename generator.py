import simplejson as json

def parse_csv(text, sep):
    lines = list(map(lambda t: t.strip(), text.split("\n")))
    lines = list(filter(lambda l: l != "" and l[0] != "#", lines))
    return list(map(lambda l: l.split(sep), lines))


def station_id(char, number):
    return char + ("0" if number < 10 else "") + str(number)

def add_connection(metro_map):
    def inner(fro, to, type, dur):
        entry = {
            "name_en": None,
            "name_jp": None,
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

transitions = open("data/transitions.csv")
lines = open("data/lines.csv")

metro_map = {}
add_conn = add_connection(metro_map)

for line in parse_csv(lines.read(), ","):
    char = line[0]
    first = int(line[1])
    last = int(line[2])
    rides = list(map(int, line[3:]))

    for station_number in range(first, last):
        time = rides[station_number - first]
        station_a = station_id(char, station_number)
        station_b = station_id(char, station_number + 1)
        metro_map = add_conn(station_a, station_b, "ride", time)
        metro_map = add_conn(station_b, station_a, "ride", time)

for transition in parse_csv(transitions.read(), ","):
    station1 = station_id(transition[0], int(transition[1]))
    station2 = station_id(transition[2], int(transition[3]))
    time = int(transition[4])

    # Exceptions where transitions.csv does not contain
    # a change, but a ride
    if (station1 == "Mb05" and station2 == "M06") or (station1 == "E01" and station2 == "E28"):
       type = "ride"
    else:
        type = "walk"

    metro_map = add_conn(station1, station2, type, time)

print("Dumping...")
file = open("stations.json", "w+")
file.write(json.dumps(metro_map, indent=4, sort_keys=True))
file.close()

