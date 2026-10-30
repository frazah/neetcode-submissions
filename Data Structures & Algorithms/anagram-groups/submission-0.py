class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for i, phrase in enumerate(strs):
            sol[tuple(sorted(phrase))].append(phrase)

        return list(sol.values())

