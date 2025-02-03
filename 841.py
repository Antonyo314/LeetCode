class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited = set()

        while True:
            changed = False
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    changed = True
                    for k in rooms[key]:
                        keys.append(k)

            if not changed:
                return len(set(keys)) == len(rooms)
