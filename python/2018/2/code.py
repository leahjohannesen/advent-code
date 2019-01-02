#from timething import timeit
from collections import Counter

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def part1(inst):
    twos, threes = 0, 0
    for ln in inst:
        ctr = Counter(ln)
        if 2 in ctr.values():
            twos += 1
        if 3 in ctr.values():
            threes += 1
    return twos * threes

def part2(inst):
    for i, ln0 in enumerate(inst):
        for j, ln1 in enumerate(inst):
            if i <= j:
                continue
            ctr = 0
            for l1, l2 in zip(ln0, ln1):
                if l1 != l2:
                    ctr += 1
            if ctr == 1:
                return ln0, ln1

if __name__=='__main__':
    inst = read_instructions('text.txt')
    print(part1(inst))
    #print(part2(['+3', '+3', '+4', '-2', '-4']))
    print(part2(inst))

