def minimumTotal(triangle) -> int:
    M, N = len(triangle), len(triangle[-1])
    
    # init DP matrix
    OPT = [[0 for _ in range(N)] for _ in range(M)]
    for n in range(N):
        OPT[M - 1][n] = triangle[-1][n]
    
    for i in range(M - 2, -1, -1):
        for j in range(N - M + i + 1):
            OPT[i][j] = min(OPT[i + 1][j], OPT[i + 1][j + 1]) + triangle[i][j]
    
    return OPT[0][0]