from timething import timeit
from itertools import product
from collections import deque, defaultdict

class Maze(object):
    def __init__(self, code, end=(1,1), n=50):
        self.code = code
        self.end = end 
        self.n = n
        self.maze = defaultdict(int)
        self.create_maze()

    def __str__(self):
        out = ''
        for a in xrange(self.n):
            for b in xrange(self.n):
                char = self.maze[(b,a)]
                if char == True:
                    out += '.'
                elif char == False:
                    out += 'X'
            out += '\n'
        return out
    
#    def create_maze(self, n):
#        arr = [[False]*n for _ in range(n)]
#        for x,y in product(range(n), repeat=2):
#            res = x*x + 3*x + 2*x*y + y + y*y + self.code
#            res = sum(map(int, bin(res)[2:]))
#            if res % 2 == 0:
#                arr[y][x] = True
#        arr[1][1] = 's'
#        arr[self.end[1]][self.end[0]] = 'e' 
#        return arr

    def create_maze(self):
        for x,y in product(range(self.n), repeat=2):
            res = x*x + 3*x + 2*x*y + y + y*y + self.code
            res = sum(map(int, bin(res)[2:]))
            if res % 2 == 0:
               self.maze[(x,y)] = True 
            self.maze[(1,1)] = True
            self.maze[self.end] = True
       

    def bfs(self):
        start = (1,1)
        q = deque()
        q.append(start)
        path = defaultdict(list)
        path[start] = [start]
        while q:
            curr = q.popleft()
            x,y = curr
            if curr == self.end: return len(path[curr]) - 1
            neighbors = self.check_neighbors(x,y) 
            for nbr in neighbors:
                if nbr not in path.keys():
                    if nbr[0] < 0 or nbr[1] < 0: continue
                    blah = list(path[curr])
                    blah.append(nbr)
                    path[nbr] = blah
                    q.append(nbr)
        return None

    def unique(self):
        start = (1,1)
        q = deque()
        q.append(start)
        path = defaultdict(list)
        path[start] = [start]
        while q:
            curr = q.popleft()
            x,y = curr
            neighbors = self.check_neighbors(x,y) 
            for nbr in neighbors:
                if nbr not in path.keys():
                    if nbr[0] < 0 or nbr[1] < 0: continue
                    blah = list(path[curr])
                    blah.append(nbr)
                    path[nbr] = blah
                    if len(blah) <= 50: q.append(nbr)
        return len(path) 

    def check_neighbors(self, a, b):
        nbrs = []
        if self.maze[(a+1,b)]: nbrs.append((a+1,b))
        if self.maze[(a-1,b)]: nbrs.append((a-1,b))
        if self.maze[(a,b+1)]: nbrs.append((a,b+1))
        if self.maze[(a,b-1)]: nbrs.append((a,b-1))
        return nbrs 

@timeit
def part1():
    test = Maze(10, end=(7,4), n=10)
    print test 
    print test.bfs()
    mz = Maze(1352, end=(31,39))
    print mz.bfs()

@timeit
def part2():
    mz = Maze(1352, end=(31,39))
    print mz.unique()

if __name__=='__main__':
    part1()
    part2()
