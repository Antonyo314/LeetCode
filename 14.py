class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min([len(s) for s in strs])

        for i in range(l, -1, -1):
            prefixes = [s[:i] for s in strs]

            if len(set(prefixes)) == 1:
                return prefixes[0]

