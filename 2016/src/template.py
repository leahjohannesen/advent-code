from timeit import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.readlines()

@timeit
def part1():
    pass

@timeit
def part2():
    pass
    
if __name__=='__main__':
    part1()
    part2()
