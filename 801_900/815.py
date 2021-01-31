from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stops = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].append(i)
        seen_bus, seen_stop = set(), {S}
        queue = [(S, 0)]
        while queue:
            stop, count = queue.pop(0)
            if stop == T:
                return count
            for bus in stops[stop]:
                if bus in seen_bus:
                    continue
                seen_bus.add(bus)
                for nex in routes[bus]:
                    if nex in seen_stop:
                        continue
                    seen_stop.add(nex)
                    queue.append((nex, count + 1))
        return -1
