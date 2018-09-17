for i in range(int(input().strip())):
    n = int(input().strip())
    songs = list(map(int,input().strip().split()))
    uncleJohny = songs[int(input().strip())-1]
    songs.sort()
    print(songs.index(uncleJohny)+1)
