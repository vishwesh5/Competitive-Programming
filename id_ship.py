# problem link: https://www.codechef.com/problems/FLOW010

for i in range(int(input().strip())):
    ship_id = input().strip().upper()
    if ship_id == 'B':
        print("BattleShip")
    elif ship_id == 'C':
        print("Cruiser")
    elif ship_id == 'D':
        print("Destroyer")
    elif ship_id == 'F':
        print("Frigate")
