#from timething import timeit

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def part1(linelist):
    set0 = create_set(linelist[0].split(','))
    set1 = create_set(linelist[1].split(','))
    dists = min(abs(num.real) + abs(num.imag) for num in set0 & set1)
    print(set0 & set1)
    print(dists)

def create_set(line):
    blah = {
        'L': -1, 
        'R': 1,
        'D': -1j,
        'U': 1j,
        }
    coord = 0j
    cset = set()
    for inst in line:
        val = blah[inst[0]]
        for _ in range(int(inst[1:])):
            coord += val
            cset.add(coord)
    return cset

def part2(linelist):
    set0 = create_set(linelist[0].split(','))
    set1 = create_set(linelist[1].split(','))
    intersections = set0 & set1
    ints0 = create_steps(linelist[0].split(','), intersections)
    ints1 = create_steps(linelist[1].split(','), intersections)
    output = min(ints0[point] + ints1[point] for point in intersections)
    print(output)

def create_steps(line, pointset):
    blah = {
        'L': -1, 
        'R': 1,
        'D': -1j,
        'U': 1j,
        }
    coord = 0j
    counter = 0
    output = {}
    for inst in line:
        val = blah[inst[0]]
        for _ in range(int(inst[1:])):
            coord += val
            counter += 1
            if coord in pointset:
                output[coord] = counter
    return output

if __name__=='__main__':
    inst = read_instructions('text.txt')
    part1(inst)
    part2(inst)
