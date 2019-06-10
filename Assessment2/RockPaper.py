def checkWinner(playedValue):
    playedString = ["RP" , "RS", "SP" , "SR" , "PR" , "PS" , "RR" , "PP" , "SS"]
    pointsGained = [-1, 1 ,1,-1,1,-1, 0, 0, 0]
    return pointsGained[playedString.index(playedValue)]

###################################################################

def GamePlay(PlayersString):
    playersString = list(PlayersString.split(","))
    wonLossDrawSequence = [0 for i in range(3)]
    for i in playersString :
        point = checkWinner(i)
        if(point == 1):
            wonLossDrawSequence[0] += 1
        elif (point == -1) :
            wonLossDrawSequence[1] -= 1
        else :
            wonLossDrawSequence[2] += 1
    return wonLossDrawSequence

########################################################

game = input()
wonLossDrawSequence = GamePlay(game)
print(str(wonLossDrawSequence[0]) + ","+str(wonLossDrawSequence[1]) + "," + str(wonLossDrawSequence[2]))

