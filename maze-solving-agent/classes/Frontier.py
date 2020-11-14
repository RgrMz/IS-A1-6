import heapq

class Frontier():
    
    def __init__(self):
        self.heap = []

    def pop(self):
        
        return heapq.heappop(self.heap)
    
    def push(self, node):
        
        heapq.heappush(self.heap, node)

    def isEmpty(self):
        return len(self.heap) == 0
