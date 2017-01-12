import hashlib

def find_hash(key):
    key_len = 0
    idx = 0
    pw = [None]*8
    while key_len < 8:
        dig = hashlib.md5(key + str(idx)).hexdigest()        
        if dig[:5] == '00000':
            try:
                loc = int(dig[5])
                if not pw[loc]:
                    pw[loc] = dig[6]
                    key_len += 1
            except:
                pass
        idx += 1
    return ''.join(pw)

def main():
    #Part 1
    toy = 'abc'
    inst = 'ffykfhsq'
    print find_hash(toy)
    print find_hash(inst)

if __name__=='__main__':
    main()
