n = int(input())
for _ in range(n):
    l, n = [int(x) for x in input().split(" ")]
    ants = []
    while len(ants) != n:
        ants += [int(x) for x in input().split(" ")]

    # Shortest time = distance middle ant is from either end.
    # Find this ant's location
    middle = round(l / 2)
    best_distance = l
    worst_distance = 0
    best_ant = None
    worst_ant = None
    for ant in ants:
        if abs(ant - middle) < best_distance:
            best_ant = ant
            best_distance = abs(ant - middle)
        long_distance = max(abs(l - ant), ant)
        if long_distance > worst_distance:
            worst_ant = ant
            worst_distance = long_distance

    assert best_ant is not None and worst_ant is not None
    best = min(abs(l - best_ant), best_ant)
    print("%s %s" % (best, worst_distance))
