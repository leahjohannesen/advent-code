class Keypad(object):

    def __init__(self, key_layout):
        self.dirs = {'U':0, 'R':1, 'D':2, 'L':3}
        self.last_digit = 5
        self.code = []
        self.keypad = self.parse_keypad(key_layout)
    
    def parse_keypad(self, kp):
        #layout  = {1: (1,2,4,1), 2: (2,3,5,1), 3: (3,3,6,2),
        #               4: (1,5,7,4), 5: (2,6,8,4), 6: (3,6,9,5),
        #               7: (4,8,7,7), 8: (5,9,8,7), 9: (6,9,9,8)} 
        
        return layout

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
    kp1 = '1 2 3\n4 5 6\n7 8 9\n'
    kp = Keypad(kp1)
    print kp.find_code(inst)
    
    #Part 2
    kp2 = '   1    \n  2 3 4  \n5 6 7 8 9\n  A B C  \n    D    \n'  
    kp = Keypad(kp2)
    print kp.find_code(inst)

if __name__ == '__main__':
    toy = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    main(toy)
    instructions = read_instructions('input/day2.txt')
    main(instructions)
    
