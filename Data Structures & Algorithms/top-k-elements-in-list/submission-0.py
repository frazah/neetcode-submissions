class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_dict = {}
        for n in nums:
            counter_dict[n] = counter_dict.get(n, 0) + 1

        freq_lists = [[] for i in range(len(nums) + 1)] #lista di liste, indice = frequenza
        for num, count in counter_dict.items():
            freq_lists[count].append(num)

        sol = []
        for i in range(len(freq_lists) - 1, 0, -1): #itero partendo dall'ultimo(più frequente)
            for num in freq_lists[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol
    