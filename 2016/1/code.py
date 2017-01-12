from timeit import timeit

def read_instructions(path):
    with open(path, 'r') as f:
        return f.readlines()

class distancer(object):

    def __init__(self):
        self.inst = None
        self.dir_change = {1: (4, 2), 2: (1,3), 3: (2,4), 4: (3,1)}
        self.dir_step = {1: (1, 0), 2: (0, 1), 3: (-1, 0), 4: (0, -1)}
        self.curr_dir = 1
        self.dist = [0, 0]
        self.hist = set()

    def total_dist(self, s):
        self.inst = s.split(', ')
        for step in self.inst:
            update = self.calc_step(step)
            self.update_dist(update)
        return sum(map(abs,self.dist))

    def total_dist_hist(self, s):
        self.inst = s.split(', ')
        for step in self.inst:
            update = self.calc_step(step)
            if self.take_steps(update):
                break
        return sum(map(abs,self.dist))

    def calc_step(self, step):
        step_dir = step[0]
        step_len = int(step[1:])
        dist = [0,0]
        if step_dir == 'L':
            self.curr_dir = self.dir_change[self.curr_dir][0]
        else:
            self.curr_dir = self.dir_change[self.curr_dir][1]

        dist[0] += self.dir_step[self.curr_dir][0] * step_len
        dist[1] += self.dir_step[self.curr_dir][1] * step_len
        return dist

    def update_dist(self, step):
        self.dist[0] += step[0]
        self.dist[1] += step[1]
        return

    def take_steps(self, step):
        total_steps = max(map(abs, step))
        for i in xrange(total_steps):
            self.update_dist(self.dir_step[self.curr_dir])
            tupped = tuple(self.dist)
            if tupped in self.hist:
                return True
            else:
                self.hist |= set([tupped])
        return False

@timeit
def main(instructions):
    test = distancer()
    print test.total_dist(instructions)
    test = distancer()
    print test.total_dist_hist(instructions)

if __name__ == '__main__':
    instructions = read_instructions('day1/input.txt')[0]
    main(instructions)
