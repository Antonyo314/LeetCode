from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players = sorted(players)
        trainers = sorted(trainers)

        p = 0
        t = 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                res += 1
                p += 1
                t += 1
            else:
                t += 1
        return res
