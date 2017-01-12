from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def solve(inst, p2=False):
    slots, pos = parse(inst)
    if p2:
        slots.append(11)
        pos.append(0)
    i = 0
    while True:
        check = 0 
        for a,b in enumerate(pos):
            num = a+b+i+1
            den = slots[a]
            check += num%den
        if check == 0: return i    
        i += 1

def parse(inst):
    s, p = [], []
    for i in inst:
        blah = i.split()
        s.append(int(blah[3]))
        p.append(int(blah[-1][:-1]))
    return s, p

@timeit
def part1():
    toy = read_instructions('15/toy.txt')
    print solve(toy)
    inst = read_instructions('15/input.txt')
    print solve(inst)
    print solve(inst, True)

@timeit
def part2():
    pass

if __name__=='__main__':
    part1()
    part2()
