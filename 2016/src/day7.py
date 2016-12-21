from timeit import timeit
import re
import regex

class Abba(object):
    def __init__(self):
        self.split = re.compile(r'\[|\]')
        self.check = re.compile(r'(.)(?!\1)(.)\2\1')
        self.opp_check = regex.compile(r'\[.*?(.)(?!\1)(.)\1.*?\]')
        self.oc2 = regex.compile(r'(.)(?!\1)(.)\1')

    def __call__(self, inst):
        res1 = sum(map(self.check_row, inst))
        res2 = sum(map(self.check_row2, inst))
        return res1, res2

    def check_row(self, row):
        split = self.split.split(row)
        for inner in split[1::2]:
            if self.check.search(inner):
                return False
        for outer in split[::2]:
            if self.check.search(outer):
                return True
        return False

    def check_row2(self, row):
        #options = self.opp_check.findall(row)
        splits = self.split.split(row)
        outers = splits[::2]
        inners = splits[1::2]
        for inner in inners:
            results = self.oc2.findall(inner, overlapped=True)
            for r1,r2 in results:
                s = r2 + r1 + r2
                for outer in outers:
                    if s in outer:
                        return True
        #for a,b in options:
        #    for outer in outers:
        #        if b+a+b in outer:
        #            return True      
        return False

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')

@timeit
def part1():
    abba = Abba()
    toy1 = ['ioxxoj[asdfgh]zxcvbn']
    toy2 = ['abcd[bddb]xyyx']
    toy3 = ['zazbz[bzb]cdb']
    toy4 = ['xyx[xyx]xy']
    toy5 = ['aaa[aaa]eke[bab]baaaba']
    inst = read_instructions('input/day7.txt')
    print abba(toy1)
    print abba(toy2)
    print abba(toy3)
    print abba(toy4)
    print abba(toy5)
    print abba(inst)
    
if __name__=='__main__':
    part1()
