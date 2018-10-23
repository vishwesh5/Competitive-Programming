data = input().strip()
cards = {"P":[],"K":[],"H":[],"T":[]}
numCards = len(data)//3
flag = True
for i in range(numCards):
    card = data[i*3:3*(i+1)]
    num = card[1:]
    suit = card[0]
    if num in cards[suit]:
        flag=False
        print("GRESKA")
        break
    else:
        cards[suit].append(num)
if flag != False:
    ans=[]
    for suit in cards.keys():
        ans.append(13-len(cards[suit]))
    print(" ".join(list(map(str,ans))))
