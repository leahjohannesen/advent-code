from timething import timeit
import re

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.read().split('\n')[:-1]

def make_message(s, p2=False):
    i = 0
    output = 0
    while True:
        if i == len(s):
            return output
        if s[i] == '(':
            j = s.find(')', i)
            res = s[i+1:j].split('x')
            chars, reps = int(res[0]), int(res[1])
            rep_string = s[j+1:j+chars+1]
            if p2:
                output += make_message(rep_string, p2) * reps
            else:
                output += len(rep_string)*reps
            i = j+chars+1
        else:
            output += 1
            i += 1

@timeit
def part1():
    inst = read_instructions('day9/input.txt')
    print make_message('ADVENT')
    print make_message('A(1x5)BC')
    print make_message('A(2x2)BCD(2x2)EFG')
    print make_message('(6x1)(1x3)A')
    print make_message('X(8x2)(3x3)ABCY')
    print make_message(inst[0])
@timeit
def part2():
    inst = read_instructions('day9/input.txt')
    print make_message(inst[0], True)

if __name__=='__main__':
    part1()
    part2()
