from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')

class Keypad(object):
    def __init__(self):
        self.kp = [[0]*50 for _ in range(6)]
    
    def print_kp(self):
        for i in range(6):
            pretty = ['X' if x == 1 else ' ' for x in self.kp[i]] 
            print ''.join(pretty)
   
    def solve(self, inst):
        map(self.parse_inst, inst)
        return sum(map(sum, self.kp))

    def parse_inst(self, instr):
        blah = instr.split()
        if len(blah[0]) == 4:
            self.rect(blah[1])
        elif len(blah[1]) == 3:
            self.row(blah[2], int(blah[4]))
        else:
            self.column(blah[2], int(blah[4]))
            
    def rect(self, rect_inst):
        cols, rows = rect_inst.split('x')
        for x in range(int(rows)):        
            for y in range(int(cols)):
                self.kp[x][y] = self.kp[x][y] ^ 1

    def row(self, row_num, rot_num):
        blah = row_num.split('=')
        row = int(blah[-1])
        rot_num = 50 - rot_num
        self.kp[row] = self.kp[row][rot_num:] + self.kp[row][:rot_num]
    
    def column(self, col_num, rot_num):
        blah = col_num.split('=')
        col = int(blah[-1])
        rot_num = 6-rot_num
        temp = [0]*6
        for i in xrange(6):
            temp[i] = self.kp[i][col]
        temp = temp[rot_num:] + temp[:rot_num]
        for i in xrange(6):
            self.kp[i][col] = temp[i]

@timeit
def part1():
    inst = read_instructions('day8/input.txt')
    #kp_r = Keypad()
    #print kp_r.solve(['rect 3x2'])
    #print kp_r.solve(['rotate row x=1 by 1'])
    #print kp_r.solve(['rotate column y=1 by 1'])
    #print kp_r.print_kp()
    kp = Keypad()
    print kp.solve(inst[:-1]) 
    kp.print_kp()

@timeit
def part2():
    pass

if __name__=='__main__':
    part1()
    part2()
