
def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y, n) = room.split()
            h = 1
            for i in range(int(y)):
                for j in range(int( int(x) / 3)):
                    print(h, h, h, end=' ')
                    h+=1
                print("\n")


if __name__ == '__main__':
    read_file('level2_1.in.txt')