
def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y, n) = room.split()
        h = 1
        for i in range(y):
            for j in range(int (x / 3)):
                print(h, h, h, end=' ')
            print()


if __name__ == '__main__':
    read_file('level1_5.in.txt')