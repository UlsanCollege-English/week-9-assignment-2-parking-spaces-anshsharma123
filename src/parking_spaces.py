import heapq

def min_parking_spots(intervals):
    """
    Given a list of (start, end) intervals, return the minimum number
    of parking spots needed so that no car waits.
    """
    if not intervals:
        return 0

    # Step 1: sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: use a min-heap to track end times of cars currently parked
    heap = []
    max_spots = 0

    for start, end in intervals:
        # free up spots that have been vacated
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        # add current car's end time
        heapq.heappush(heap, end)
        # update max spots needed
        max_spots = max(max_spots, len(heap))

    return max_spots


# --- Example tests ---
if __name__ == "__main__":
    assert min_parking_spots([(0,30),(5,10),(15,20)]) == 2
    assert min_parking_spots([(7,10),(2,4)]) == 1
    assert min_parking_spots([(0,10),(10,20),(20,30)]) == 1
    assert min_parking_spots([(1,5),(2,3),(4,6)]) == 2
    assert min_parking_spots([]) == 0
    assert min_parking_spots([(1,2)]) == 1
    assert min_parking_spots([(1,1),(1,1),(1,1)]) == 1
    assert min_parking_spots([(1,10),(2,7),(3,4),(5,6),(8,9)]) == 3
    intervals = [(5,8),(1,4),(6,9),(2,3),(10,13),(7,10)]
    assert min_parking_spots(intervals) == 3
    intervals = [(i, i+3) for i in range(0, 50, 2)]
    assert min_parking_spots(intervals) == 2

    print("All tests passed!")
