''' Matrix_MN '''

def matrix():
    ''' print matrix m x n '''
    m_row = int(input())    #แถว
    n_col = int(input())    #หลัก
    #num_in_matrix = m * n
    #numlist = [int(input()) for _ in range(num_in_matrix)]
    mat = []
    for i in range(m_row):
        row = []
        for j in range(n_col):
            num = input()
            row.append(num)
        mat.append(row)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=' ')
        print()
matrix()
