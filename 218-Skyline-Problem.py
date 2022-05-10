import heapq

# Function Definitions
class Solution:
  def getSkyline(self, buildings):
        skyline = {}
        def heap_remove(heap, value):
            skyline[value] = skyline.get(value, 0) + 1
            while len(heap) and heap[0] in skyline and skyline[heap[0]]:
                skyline[heap[0]] = skyline.get(heap[0]) - 1
                heapq.heappop(heap)
            return heap
        points = []
        for Li, Ri, Hi in buildings:
            points.append((Li, -Hi, 1))
            points.append((Ri, Hi, -1)                                                                                                                                                                      )
        points.sort()
        pq, max_height = [0], 0
        key_points = []
        for x, h, s in points:
            if s == 1: # start point
                if -h > max_height:
                    max_height = -h
                    key_points.append([x, -h])
                heapq.heappush(pq,h)
            else: # end point
                pq = heap_remove(pq,-h)
                pq_max = -pq[0]
                if pq_max < max_height:
                    max_height = pq_max
                    key_points.append([x, max_height])
        return key_points
# PyTests

# Test script
def main():
    s1 = Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
    s2 = Solution().getSkyline([[0,2,3],[2,5,3]])
    s3 = Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]])
    s4 = Solution().getSkyline([[0,3,3],[1,5,3],[2,4,3],[3,7,3]])
    s5 = Solution().getSkyline([[1,20,1],[1,21,2],[1,22,3]])
    print(f's1: {s1}') #[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(f's2: {s2}') #[[0, 3], [5, 0]]
    print(f's3: {s3}') #[[1, 3], [2, 0]]
    print(f's4: {s4}') #[[0,3],[7,0]]
    print(f's5: {s5}') #[[1,3],[22,0]]

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()