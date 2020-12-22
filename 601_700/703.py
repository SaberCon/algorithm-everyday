import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums, reverse=True)[:min(k, len(nums))]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
