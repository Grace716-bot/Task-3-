import heapq

pq = []

heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)

print("Priority Queue:", pq)

while pq:
    print("Removed:", heapq.heappop(pq))
