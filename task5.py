import array

def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y, n) = map(int, room.split())

            reversed = False
            if x < y:
                (x, y) = (y, x)
                reversed = True

            matrix = [['.' for i in range(x)] for j in range(y)]
            last = 0

            for i in range(0, y, 2):
                for j in range(0, (x-1), 3):
                    matrix[i][j] = 'X'
                    matrix[i][j+1] = 'X'
                    last = j

            z = x - (x % 3)
            for j in range(last + 3, x, 2):
                for i in range(0, y-1, 3):
                    matrix[i][j] = 'X'
                    matrix[i+1][j] = 'X'



            if reversed:
                matrix = [list(row) for row in zip(*matrix)]
                (y, x) = (x, y)

            for i in range(y):
                for j in range(x):
                    print(matrix[i][j], end='')
                print("")
            print("")


if __name__ == '__main__':
    read_file('level5_1.in.txt')
