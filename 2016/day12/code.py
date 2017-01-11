from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def solve(inst, p2=0):
    d = {'a': 0, 'b': 0, 'c': p2, 'd': 0}
    i = 0
    while i < len(inst):
        blah = inst[i].split()
        if blah[0] == 'cpy':
            d[blah[2]] = int(blah[1]) if blah[1].isdigit() else d[blah[1]]
        elif blah[0] == 'inc':
            d[blah[1]] += 1
        elif blah[0] == 'dec':
            d[blah[1]] -= 1
        else:
            chk = int(blah[1]) if blah[1].isdigit() else d[blah[1]]
            i += int(blah[2]) - 1 if chk != 0 else 0  
        i += 1
    return d


@timeit
def part1():
    inst = read_instructions('day12/input.txt') 
    print solve(inst)

@timeit
def part2():
    inst = read_instructions('day12/input.txt') 
    print solve(inst, 1)

if __name__=='__main__':
    part1()
    part2()
