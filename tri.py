nums = list(map(int,input().strip().split()))
if nums[0]+nums[1]==nums[2]:
    print("{}+{}={}".format(nums[0],nums[1],nums[2]))
elif nums[0]*nums[1]==nums[2]:
    print("{}*{}={}".format(nums[0],nums[1],nums[2]))
elif nums[0]-nums[1]==nums[2]:
    print("{}-{}={}".format(nums[0],nums[1],nums[2]))
elif nums[0]/nums[1]==nums[2]:
    print("{}/{}={}".format(nums[0],nums[1],nums[2]))
elif nums[1]+nums[2]==nums[0]:
    print("{}={}+{}".format(nums[0],nums[1],nums[2]))
elif nums[1]*nums[2]==nums[0]:
    print("{}={}*{}".format(nums[0],nums[1],nums[2]))
elif nums[1]/nums[2]==nums[0]:
    print("{}={}/{}".format(nums[0],nums[1],nums[2]))
elif nums[1]-nums[2]==nums[0]:
    print("{}={}-{}".format(nums[0],nums[1],nums[2]))
