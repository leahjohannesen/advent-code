from timeit import timeit
from collections import Counter

@timeit
def decode(inst):
    columns = zip(*inst)
    output = []
    for column in columns:
        c = Counter(column)
        output.append(c.most_common()[0][0])
    return ''.join(output)

@timeit
def decode2(inst):
    columns = zip(*inst)
    output = []
    for column in columns:
        c = Counter(column)
        output.append(c.most_common()[-1][0])
    return ''.join(output)

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.readlines()

def part1():
    toy = read_instructions('input/day6toy.txt')
    print decode(toy)
    inst = read_instructions('input/day6.txt')
    print decode(inst)
    
def part2():
    toy = read_instructions('input/day6toy.txt')
    print decode2(toy)
    inst = read_instructions('input/day6.txt')
    print decode2(inst)
    
if __name__=='__main__':
    part1()
    part2()
