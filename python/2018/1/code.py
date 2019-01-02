#from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def part1(inst):
    return sum(map(int, inst))

def part2(inst):
    nummed = list(map(int, inst))
    past_freq = set()
    freq = 0
    while True:
        for num in nummed:
            freq += num
            if freq in past_freq:
                return freq
            past_freq.add(freq)

def part2a(inst):
    #cool improvement, make a generator rather than while
    pass

if __name__=='__main__':
    inst = read_instructions('text.txt')
    print(part1(inst))
    #print(part2(['+3', '+3', '+4', '-2', '-4']))
    print(part2(inst))

