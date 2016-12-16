class Keypad(object):

    def __init__(self, key_layout):
        self.dirs = {'U':0, 'R':1, 'D':2, 'L':3}
        self.last_digit = '5'
        self.code = []
        self.keypad = self.parse_keypad(key_layout)
    
    def parse_keypad(self, kp):
        #layout  = {1: (1,2,4,1), 2: (2,3,5,1), 3: (3,3,6,2),
        #               4: (1,5,7,4), 5: (2,6,8,4), 6: (3,6,9,5),
        #               7: (4,8,7,7), 8: (5,9,8,7), 9: (6,9,9,8)} 
        key_dict = {}
        k = kp.split('\n')
        k.pop(-1)
        for i, line in enumerate(k):
            for j, char in enumerate(line):
                if char == ' ':
                    continue
                else:
                    key_dict[char] = self.get_neighbors(k, i, j)

        return key_dict 

    def get_neighbors(self, kp, i, j):
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        out = []
        for v, h in dirs:
            tempx, tempy = v + i, h + j 
            xidx = i if tempx < 0 or tempx >= len(kp) else tempx 
            yidx = j if tempy < 0 or tempy >= len(kp[0]) else tempy
            char = kp[xidx][yidx]
            if char == ' ':
                out.append(kp[i][j])
            else:
                out.append(char)
        return tuple(out)
        

    def find_code(self, inst):
        for sequence in inst:
            result = self.find_digit(sequence, self.last_digit)
            self.last_digit = result
            self.code.append(result) 
        return self.code

    def find_digit(self, seq, curr):
        seq = seq.strip()
        for step in seq:
            curr = self.keypad[curr][self.dirs[step]]
        return curr 

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.readlines()

def main(inst):
    #Part 1
    kp1 = '123\n456\n789\n'
    kp = Keypad(kp1)
    print kp.find_code(inst)
    
    #Part 2
    kp2 = '  1  \n 234 \n56789\n ABC \n  D  \n'  
    kp = Keypad(kp2)
    print kp.find_code(inst)

if __name__ == '__main__':
    toy = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    main(toy)
    instructions = read_instructions('input/day2.txt')
    main(instructions)
    
