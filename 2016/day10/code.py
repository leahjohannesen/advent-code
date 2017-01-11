from timething import timeit
from collections import defaultdict

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

class Robot(object):
    def __init__(self, low, high):
        self.out = (low, high)
        self.curr = [] 

    def take(self, i):
        self.curr.append(i)
        if len(self.curr) == 2:
            return self.give()
    
    def give(self):
        a,b = self.curr
        self.curr = []
        if a > b:
            return b, a, self.out[0], self.out[1]
        else:
            return a, b, self.out[0], self.out[1]

class CrazyRoom(object):
    def __init__(self):
        self.robot_dict = {}
        self.val_list = []
        self.output_dict = defaultdict(list) 

    def run_inst(self, inst):
        map(self.create, inst)
        self.run_vals()
        return self.output_dict
        
    
    def create(self, line):
        line_list = line.split()
        if line_list[0] == 'bot':
            bot = line_list[0] + line_list[1]
            low = line_list[5] + line_list[6]
            high = line_list[10] + line_list[11]
            self.robot_dict[bot] = Robot(low, high)
        else:
            val_bot, val = line_list[4] + line_list[5], int(line_list[1]) 
            self.val_list.append((val_bot, val))

    def run_vals(self):
        for b, v in self.val_list:
            self.dist(b, v)

    def dist(self, bot, val):
        give = self.robot_dict[bot].take(val)
        if give:
            #if give[0] == 17 and give[1] == 61: print bot
            if give[2][0] == 'o':
                self.output_dict[give[2]].append(give[0])
            else:
                self.dist(give[2], give[0])
            if give[3][0] == 'o':
                self.output_dict[give[3]].append(give[1])
            else:
                self.dist(give[3], give[1])

@timeit
def part1():
    inst = read_instructions('day10/input.txt')
    cr = CrazyRoom()
    cr.run_inst(inst)
    

@timeit
def part2():
    inst = read_instructions('day10/input.txt')
    cr = CrazyRoom()
    out = cr.run_inst(inst) 
    print out['output0'],out['output1'],out['output2']

if __name__=='__main__':
    part1()
    part2()
