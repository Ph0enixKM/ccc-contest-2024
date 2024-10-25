
def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y) = room.split()
            print(int(int(x) * int(y) / 3))

if __name__ == '__main__':
<<<<<<< HEAD
    read_file('level1_5.in.txt')
=======
    read_file('level1_3.in.txt')
>>>>>>> e4957c744fc116e816d2f8eaedb05b30d2aec128
