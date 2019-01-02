class Triangles(object):
    
    def __init__(self):
        pass

    def count_triangles(self, inst):
        return sum(map(self.tri_1, inst))

    def count_tri2(self, inst):
        total = 0
        for i in xrange(0,len(inst),3):
            group = inst[i:i+3]
            total += self.tri_2(group)
        return total

    def tri_1(self, tri):
        sides = tri.strip().split() 
        return self.is_triangle(sides)

    def tri_2(self, group):
        form = map(lambda x: x.strip().split(), group)
        print form
        total = sum(map(self.is_triangle, zip(*form)))
        print total
        return total

    def is_triangle(self, tri):
        tri = map(int, tri)
        s = sorted(tri)
        if s[0] + s[1] > s[2]:
            return 1
        else:
            return 0


def read_instructions(fp):
    with open(fp, 'r') as f:
        return f.readlines()

def main():
    tri = Triangles()

    #Part 1
    inst = read_instructions('input/day3.txt')
    toy = ['10 5 25']
    toy2 = ['5 6 7']
    print tri.count_triangles(toy)
    print tri.count_triangles(toy2)
    print tri.count_triangles(inst)
    print tri.count_tri2(inst)
    

if __name__=='__main__':
    main()
