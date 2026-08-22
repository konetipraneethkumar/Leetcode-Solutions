class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        #h_map = {}
        total = 0
        while n >0:
            total += n%10
            #if dig not in h_map:
            #    h_map[dig] = 1
            #else:
                #h_map[dig] +=1
            n = n // 10
        #sum = 0
        #for key, val in h_map.items():
        #    sum = sum + (key * val)
        return total
        