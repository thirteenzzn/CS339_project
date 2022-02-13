import numpy

x=3
y=19
now=[x,y]

goal_x=27
goal_y=4
goal=[goal_x,goal_y]

points=[]
points.append([1,18])
points.append([5,18])
points.append([10,18])
points.append([14,18])
points.append([16,18])
points.append([20,18])
points.append([25,18])
points.append([7,17])
points.append([7,5])
points.append([15,4])
points.append([15,3])
points.append([24,17])
points.append([24,3])

minX=100
minY=100
flag=0
print(now)
while now!=goal:
    minX=100
    minY=100
    if goal[0]>=now[0] and goal[1]>=now[1]:
        for point in points:
            if minX!=100 and minY!=100:
                if (point[0]>= now[0] and point[1]>now[1] and point[0]<=minX and point[1]<=minY) or (point[0]> now[0] and point[1]>=now[1] and point[0]<=minX and point[1]<=minY):
                    minX=point[0]
                    minY=point[1]
                    flag+=1
            else:
                if (point[0]>= now[0] and point[1]>now[1]) or (point[0]> now[0] and point[1]>=now[1]):
                    minX=point[0]
                    minY=point[1]
                    flag+=1

    elif goal[0]>=now[0] and goal[1]<=now[1]:
        for point in points:
            if minX != 100 and minY != 100:
                if (point[0]> now[0] and point[1]<=now[1] and point[0]<=minX and point[1]>=minY) or (point[0]>= now[0] and point[1]<now[1] and point[0]<=minX and point[1]>=minY) :
                    minX=point[0]
                    minY=point[1]
                    flag += 1
            else:
                if (point[0]> now[0] and point[1]<=now[1]) or (point[0]>= now[0] and point[1]<now[1]) :
                    minX=point[0]
                    minY=point[1]
                    flag += 1

    elif goal[0]<=now[0] and goal[1]<=now[1]:
        for point in points:
            if minX != 100 and minY != 100:
                if (point[0]< now[0] and point[1]<=now[1] and point[0]>=minX and point[1]>=minY) or (point[0]<= now[0] and point[1]<now[1] and point[0]>=minX and point[1]>=minY):
                    minX=point[0]
                    minY=point[1]
                    flag += 1
            else:
                if (point[0]< now[0] and point[1]<=now[1] ) or (point[0]<= now[0] and point[1]<now[1]):
                    minX=point[0]
                    minY=point[1]
                    flag += 1

    else:
        for point in points:
            if minX != 100 and minY != 100:
                if (point[0]<= now[0] and point[1]>now[1] and point[0]>=minX and point[1]<=minY) or (point[0]< now[0] and point[1]>=now[1] and point[0]>=minX and point[1]<=minY):
                    minX=point[0]
                    minY=point[1]
                    flag += 1
            else:
                if (point[0]<= now[0] and point[1]>now[1]) or (point[0]< now[0] and point[1]>=now[1]):
                    minX=point[0]
                    minY=point[1]
                    flag += 1

    if minX!=100 and minY!=100:
        now=[minX,minY]
        print(now)
    else :
        break
print(goal)