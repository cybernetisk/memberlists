sem = "v"
yea = 17
init = 9

with open('semester.txt', 'w') as f:
    for x in range(0, 50):
        f.write(sem+str(yea)+":"+str(init)+"\n")
        init+=1
        if sem is "v":
            sem = "h"
        else:
            sem = "v"
            yea+=1

test = sem+str(yea)+":"+str(init)

print(test[-2:])
