abc = list(map(int,input().strip().split()))
ijk = list(map(int,input().strip().split()))
ijk2= [abc[i]/ijk[i] for i in range(3)]
#max_ijk = max(ijk)
#max_ijk = max([I,J,K])
#I,J,K = I/max_ijk,J/max_ijk,K/max_ijk
abc = [abc[i] - ijk[i]*min(ijk2) for i in range(3)]
#abc = [abc[i]*(1-ijk[i]/max_ijk) for i in range(3)]
print("{:.6f} {:.6f} {:.6f}".format(abc[0],abc[1],abc[2]))
