moves = [i for i in input().strip()]
glasses=[1,0,0]

def getAfterMove(glasses,move):
    if move=='A':
        glasses[0],glasses[1]=glasses[1],glasses[0]
    elif move=='B':
        glasses[1],glasses[2]=glasses[2],glasses[1]
    else:
        glasses[0],glasses[2]=glasses[2],glasses[0]
    return glasses

for move in moves:
    glasses = getAfterMove(glasses,move)

print(glasses.index(1)+1)
