from timeit import timeit

def read_instructions(path):
    with open(path, 'r') as f:
        return f.readlines()

def checksum(inst, fancy=False):
    n = 0
    for row in inst:
        rowval = map(int, row.split())
        if fancy:
            n += divisor(rowval)
        else:
            n += minmax(rowval)
    print n

def minmax(row):
    return max(row) - min(row)

def divisor(row):
    for val in row:
        for check in row:
            if val != check:
                if check % val == 0:
                    return check / val

if __name__ == '__main__':
    instructions = read_instructions('input.txt')
    checksum(instructions)
    checksum(instructions, fancy=True)
