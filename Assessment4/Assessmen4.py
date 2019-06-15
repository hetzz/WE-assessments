def step_increment(direction):
    direction_step_dict = {"N" :"1" , "S" : "-1" ,"E" : "1" , "W" : "-1"}
    return direction_step_dict[direction]

##############################################################

def step_NSEW(point,direction):
    if(direction[-1] == "N" or direction[-1] == "S"):
        point[1] += int(direction[:-1])* int(step_increment(direction[-1]))
    else :
        point[0] += int(direction[:-1])* int(step_increment(direction[-1]))
    return point

################################################################

def terminus(point , directions) :
    for direction in directions :
        if(direction[-2].isdigit()):
            point = step_NSEW(point , direction)
        else :
            point = step_NSEW(point , str(direction[:-2] + str(direction[-2])))
            point = step_NSEW(point , str(direction[:-2] + str(direction[-1])))
    return point

###################################################
point = [1,1]
direction = ["1N", "10NW"]

print(terminus(point, direction))