
def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y) = room.split()
            print(int(int(x) * int(y) / 3))

if __name__ == '__main__':
    read_file('level1_1.in.txt')
