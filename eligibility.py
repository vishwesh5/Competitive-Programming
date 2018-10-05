for i in range(int(input().strip())):
    student,postSec,dob,courses = input().strip().split(" ")
    courses = int(courses)
    postSecYr = list(map(int,postSec.split("/")))[0]
    dobYr = list(map(int,dob.split("/")))[0]
    eligible=False
    coachPet=False
    if postSecYr >= 2010:
        eligible=True
    elif dobYr >= 1991:
        eligible=True
    elif courses>=41:
        eligible=False
    else:
        coachPet=True
    if coachPet==True:
        print("{} coach petitions".format(student))
    elif eligible==False:
        print("{} ineligible".format(student))
    elif eligible==True:
        print("{} eligible".format(student))
