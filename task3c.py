
def read_file(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        rooms = int(lines[0])
        for room in lines[1:]:
            (x, y, n) = map(int, room.split())
            matrix = [[0 for i in range(x)] for j in range(y)]
            h = 1
            for i in range(y):
                for j in range(0, (x-2), 3):
                    matrix[i][j] = h
                    matrix[i][j+1] = h
                    matrix[i][j+2] = h
                    h+=1
            for i in range(x):
                for j in range(y-2):
                    if matrix[j][i] == matrix[j+1][i] == matrix[j+2][i] == 0:
                        matrix[j][i] = h
                        matrix[j+1][i] = h
                        matrix[j+2][i] = h
                        h+=1

            for i in range(y):
                for j in range(x):
                    print(matrix[i][j], end=' ')
                print("")


if __name__ == '__main__':
    read_file('level3_2.in.txt')
