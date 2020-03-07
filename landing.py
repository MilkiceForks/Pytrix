class Matrix:
    core = []

    def __init__(self):
        print('Please define this matrix. End with a \".\"')
        while True:
            raw = input().split()
            if raw[0] == '.':
                break
            self.core.append([int(i) for i in raw])


A = Matrix()
print(A.core)
