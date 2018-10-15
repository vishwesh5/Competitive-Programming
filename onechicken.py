N,M=list(map(int,input().strip().split()))
if N<M:
    if M-N==1:
        print("Dr. Chaz will have {} piece of chicken left over!".format(1))
    else:
        print("Dr. Chaz will have {} pieces of chicken left over!".format(M-N))
else:
    if N-M==1:
        print("Dr. Chaz needs {} more piece of chicken!".format(1))
    else:
        print("Dr. Chaz needs {} more pieces of chicken!".format(N-M))
