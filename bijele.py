chess_ideal = [1,1,2,2,2,8]
chess = list(map(int,input().strip().split()))
print(' '.join(list(map(str,[chess_ideal[i]-chess[i] for i in range(len(chess_ideal))]))))
