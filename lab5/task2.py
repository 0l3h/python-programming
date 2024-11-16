N = 7
A = []

for i in range(N):
    A.append([]);
    for j in range(N):
        A[i] += [N-i]
        print("{:4d}".format(A[i][j]), end="")
    print("\n")
