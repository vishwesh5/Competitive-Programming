for i in range(int(input().strip())):
    n,m = list(map(int,input().strip().split()))
    tasks_completed = input().strip().split()[:m]
    tasks_chef = []
    tasks_ass = []
    tasks = [str(k) for k in range(1,n+1) if str(k) not in tasks_completed]
    for j in range(len(tasks)):
        if j%2==0:
            tasks_chef.append(tasks[j])
        else:
            tasks_ass.append(tasks[j])
    print(" ".join(tasks_chef))
    print(" ".join(tasks_ass))
