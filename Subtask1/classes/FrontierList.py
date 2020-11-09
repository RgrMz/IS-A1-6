from operator import itemgetter

class FrontierList():
    def __init__(self):
        self.list_frontier = list()

    def pop(self):
        
        return self.list_frontier.pop()
    
    def push(self, node):
        
        self.list_frontier = sorted(self.list_frontier, reverse = True)
        self.list_frontier.append(node)

    def isEmpty(self):
        return len(self.list_frontier) == 0