from collections import Counter
import re

class Rooms(object):
    
    def __init__(self):
        pass

    def room_sum1(self, inst):
        reallist = map(self.check_room, inst) 
        return sum(reallist)

    def find_cipher_room(self, inst):
        for room in inst:
            string_id = room.strip()
            sect, letts, check = self.parse_room(string_id)
            shifted = self.shift_string(letts, sect)
            if 'northpole' in shifted:
                return sect
        
    def check_room(self, room):
        string_id = room.strip()
        sect, letts, check = self.parse_room(string_id)
        asdf = self.checksum(letts, check)
        if asdf:
            return int(sect)
        else:
            return 0
    
    def parse_room(self, room):
        split = room.split('[')
        check = split[1][:-1]
        split2 = split[0].split('-')
        sect = split2[-1]
        letters = ''.join(split2[:-1])
        return sect, letters, check

    def checksum(self, letts, check):
        cnt = dict(Counter(letts))
        thing = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        blah = ''.join(zip(*thing)[0])
        return blah[:5] == check 
    
    def shift_string(self, letts, shift):
        result = [self.shift_letter(letter, shift) for letter in letts]
        return ''.join(result)
    
    def shift_letter(self, letter, shift):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        return alpha[(alpha.index(letter) + int(shift)) % 26]

def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.readlines()

def main():
    #Part 1
    toy1 = ['aaaaa-bbb-z-y-x-123[abxyz]']
    toy2 = ['totally-real-room-200[decoy]']
    inst = read_instructions('input/day4.txt')
    room = Rooms()
    print room.room_sum1(toy1)
    print room.room_sum1(toy2)
    print room.room_sum1(inst)
    
    #Part 2
    print room.find_cipher_room(inst)

if __name__=='__main__':
    main()
