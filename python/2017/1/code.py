from timeit import timeit

def read_instructions(path):
    with open(path, 'r') as f:
        return f.readlines()

def same_digit(dlist):
    cumsum = 0
    n = len(dlist)
    for i in range(n):
        if dlist[i] == (dlist[(i + 1) % n]):
            cumsum += int(dlist[i])
    return cumsum

def same_half_digit(dlist):
    cumsum = 0
    n = len(dlist)
    for i in range(n - 1):
        if dlist[i] == (dlist[(i + n/2) % n]):
            cumsum += int(dlist[i])
    return cumsum

if __name__ == '__main__':
    instructions = read_instructions('input.txt')[0].strip()
    #print same_digit('1122')
    #print same_digit('1111')
    #print same_digit('1234')
    #print same_digit('91212129')
    print same_digit(instructions)

    #print same_half_digit('1212')
    #print same_half_digit('1221')
    #print same_half_digit('123425')
    #print same_half_digit('123123')
    #print same_half_digit('12131415')
    print same_half_digit(instructions)
