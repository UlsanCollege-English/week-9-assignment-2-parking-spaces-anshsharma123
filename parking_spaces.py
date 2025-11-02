# parking_spaces.py
import heapq

def min_parking_spots(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    max_spots = 0
    for start, end in intervals:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        max_spots = max(max_spots, len(heap))
    return max_spots
