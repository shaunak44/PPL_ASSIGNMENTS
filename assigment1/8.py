MAX = 100
def LU_DECOM(mat, n) :
    l_mat = [[0 for x in range(n)] for y in range(n)]
    u_mat = [[0 for x in range(n)] for y in range(n)]
    #print(l_mat)
    for i in range(n) :
        for k in range(i, n) :
            sum = 0
            for j in range(i) :
                sum += l_mat[i][j] * u_mat[j][k]
            u_mat[i][k] = mat[i][k] - sum
        for k in range(i, n) :
            if(i == k) :
                l_mat[i][i] = 1
            else :
                sum = 0
                for j in range(i) :
                    sum += l_mat[k][j] * u_mat[j][i]
                l_mat[k][i] = int((mat[k][i] - sum) / u_mat[i][i])
    print("UPPER MAT:")
    for i in range(n) :
        for j in range(n) :
            print(l_mat[i][j]),
        print("")
    print(" ")
    print("LOWER MAT:")
    for i in range(n) :
        for j in range(n) :
            print(u_mat[i][j]),
        print("")
mat = [[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]
LU_DECOM(mat, 3)
