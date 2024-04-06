def destination(n, travel_times):
    min_time = min(travel_times)
    count_min_time = travel_times.count(min_time)
    if count_min_time == 1:
        return travel_times.index(min_time) + 1
    else:
        return "Still Aetheria"
n = int(input())
travel_times = list(map(int, input().split()))
destination = destination(n, travel_times)
print(destination)
