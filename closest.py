from math import sqrt
from heapq import heappush, heappop

def get_distance(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    
    return (sqrt((x1 - x2)**2) + sqrt((y1 - y2)**2))

if "__main__" == __name__:
    pairs = [(0,0),(-2,1),(3,0),(4,-1),(-25,32)]
    distances = []
    
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            distance = get_distance(pairs[i], pairs[j])
            heappush(distances, (distance, (pairs[i], pairs[j])))
    
    j = 0
    k = 1
    shortest_k = []
    while j < k:
        shortest_k.append(heappop(distances))
        j += 1
    
    print(shortest_k)