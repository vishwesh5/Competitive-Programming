cards = input().strip().split()
suits = [i[1] for i in cards]
cards = [i[0] for i in cards]
if suits.count(suits[0]) == 5:
    flag=True
else:
    flag=False
if flag:
    cards = ' '.join(cards)
    cards = cards.replace('T','10')
    cards = cards.replace('J','11')
    cards = cards.replace('Q','12')
    cards = cards.replace('K','13')
    cards1 = cards.replace('A','14')
    cards2 = cards.replace('A','1')
    cards1 = list(map(int,cards1.split()))
    cards2 = list(map(int,cards2.split()))
    cards1.sort()
    cards2.sort()
    if cards1 == [i for i in range(min(cards1),max(cards1)+1)] or cards2 == [i for i in range(min(cards2),max(cards2)+1)]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
