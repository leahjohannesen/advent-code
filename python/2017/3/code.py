from timeit import timeit

def read_instructions(path):
    with open(path, 'r') as f:
        return f.readlines()

def clean_inst(inst):
    clean = int(inst[0].strip())
    return clean

def find_steps(inst):
    #find what loop you're in
    n = 0
    curr = 1
    while curr < inst:
        n += 1
        curr += (2*n + 1)**2 - (2*(n-1) + 1)**2
    #n = how far out you are
    if n == 0:
        return 0
    else:
        modval = 8*((n - 2) * (n - 1) / 2)
        p1 = 2 + (n > 1) * ( 9*(n-1) + modval)
        p2 = 4 + (n > 1) * (11*(n-1) + modval)
        p3 = 6 + (n > 1) * (13*(n-1) + modval) 
        p4 = 8 + (n > 1) * (15*(n-1) + modval)
        a = min(map(lambda x: abs(inst - x), [p1,p2,p3,p4]))
        return a + n

def next_dir(n, curr):
    if curr[0] < n:

def part_2(inst):
    n = 0
    curr = 1

if __name__ == '__main__':
    raw = read_instructions('input.txt')
    instructions = clean_inst(raw)
    #find_steps(instructions)
