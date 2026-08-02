class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        
        result = []
    
        sorted_frequency = sorted(frequency.items(),key=lambda x: x[1],reverse = True)

        for i in range(k):
            result.append(sorted_frequency[i][0])

        return result

        
        