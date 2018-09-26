N,B = input().strip().split()
N = int(N)
refCards = {
        'A':[11,11],
        'K':[4,4],
        'Q':[3,3],
        'J':[20,2],
        'T':[10,10],
        '9':[14,0],
        '8':[0,0],
        '7':[0,0],
        }
cards=[]
for i in range(4*N):
    cards.append(input().strip())
suits = [i[1] for i in cards]
cards = [i[0] for i in cards]
totalScore=0
for index,card in enumerate(cards):
    if suits[index]==B:
        cardIndex=0
    else:
        cardIndex=1
    totalScore+=refCards[card][cardIndex]
print(totalScore)
