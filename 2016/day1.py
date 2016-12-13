#Advent day 1, some direction stuff
#Each part of the input is a direction + how many steps you take after that

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
            

if __name__ == '__main__':

    #inst1 = 'R2, L3'
    #test1 = distancer()
    #print test1.ret_dist(inst1)

    instructions = 'L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4'
    instruction2 = 'L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4'
    test = distancer()
    print test.total_dist(instructions)
    test = distancer()
    print test.total_dist_hist(instructions)

