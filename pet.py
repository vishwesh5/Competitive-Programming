players=[]
for i in range(5):
    score = sum(list(map(int,input().strip().split())))
    players.append(score)
maxScore=max(players)
maxPlayer=players.index(maxScore)+1
print("{} {}".format(maxPlayer,maxScore))
