from typing import List


class Solution:
    @staticmethod
    def f(arr):
        for a in arr:
            if a != a[::-1]:
                return False

        return True

    @staticmethod
    def generate_binary_combinations(n):
        combinations = []
        for i in range(2 ** n):
            binary_str = bin(i)[2:].zfill(n)
            combinations.append(binary_str)
        return combinations

    def partition(self, s: str) -> List[List[str]]:

        if len(s) == 1:
            return [[s]]

        all_partitions = []

        bin_combs = self.generate_binary_combinations(len(s) - 1)

        for bin_comb in bin_combs:
            partition = [s[0]]
            for ind, i in enumerate(bin_comb):
                if i == '0':
                    partition[-1] += s[ind + 1]
                else:
                    partition.extend([s[ind + 1]])

            all_partitions.append(partition)

        result = []

        for partition in all_partitions:
            if self.f(partition):
                result.append(partition)
        return result
