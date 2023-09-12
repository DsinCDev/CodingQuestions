import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create count dict of nums
        count = {}
        heap = []
        res = []
        for n in nums:
            count[n] = count.get(n,0) + 1
        # push {count:num} pair to heap
        for item in count.items():
            num, c = item
            heapq.heappush(heap,(c*-1,num))
        # pop k highest counts and append num to result
        for i in range(k):
            top = heapq.heappop(heap)
            _, num = top
            res.append(num)
        return res