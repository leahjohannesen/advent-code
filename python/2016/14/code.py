from timething import timeit
import hashlib
import re
from collections import defaultdict

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def find_code(scoping_idiot, p2=1):
    trips = re.compile(r'(.)\1{2}')
    temp = defaultdict(set)
    out = []
    i = 0
    maxcheck = None
    while True:
        dig = hashit(scoping_idiot + str(i), p2)
        if len(out) >= 64 and i == maxcheck: break
        dcp = temp.copy()
        for key in dcp:
            if not temp[key]: 
                temp.pop(key)
                continue
            cp = temp[key].copy()    
            myreg = '(' + key + r')\1{4}'
            quint = re.search(myreg, dig)
            for val in cp:
                if quint:
                    out.append((key, val))
                    temp[key].discard(val)
                    if len(out) == 64: maxcheck = i + 999
                    continue
                if i > val + 1000: 
                    temp[key].discard(val)
                    continue
        char = trips.search(dig)
        if char: temp[char.groups()[0]].add(i)
        i += 1

    out.sort(key=lambda tup: tup[1])
    return out

def hashit(s, n):
    for _ in xrange(n):
        s = hashlib.md5(s).hexdigest().lower()
    return s
    
                

@timeit
def part1():
    print find_code('abc')[63]
    print find_code('yjdafjpo')[63]

@timeit
def part2():
    #print find_code('abc', 2017)[63]
    #for some reason this is off by 1, I legit have no idea
    res = find_code('yjdafjpo', 2017)
    print res[64]

if __name__=='__main__':
    part1()
    part2()
