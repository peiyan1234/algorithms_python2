states_needed = set(["mt", "wa", "or", "id", "nv", "ut"]) # make a list of the states you want to cover

# A set is like a list, except that each item can show up only once in a set
# Set can't have duplicates.

# arr = [1, 2, 2, 3, 3, 3]
# print """for example:
# arr = [1, 2, 2, 3, 3, 3].
# And you converted it to a set:
# set(arr):"""
# print set(arr)

# You also need the list of stations that you're choosing from

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

# You need to go through every station and pick the one that covers the most uncovered states
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print final_stations
