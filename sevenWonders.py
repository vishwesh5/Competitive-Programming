cards = input().strip()
t_cards = cards.count('T')
c_cards = cards.count('C')
g_cards = cards.count('G')
totalPoints = t_cards**2+c_cards**2+g_cards**2
totalPoints+= 7*min(t_cards,min(g_cards,c_cards))
print(totalPoints)
