import java.util.*;

class RockPaper{
    public static int checkWinner(String gamePlayed){
        String [] allCombinations =  {"RP" , "RS", "SP" , "SR" , "PR" , "PS" , "RR" , "PP" , "SS"};
        int [] pointsGained = {-1, 1 ,1,-1,1,-1, 0, 0, 0};
        return pointsGained[java.util.Arrays.asList(allCombinations).indexOf(gamePlayed)];
    }
    public static int[] pointsCalculatedfromGame(String PlayerString){
        int [] wonLossDrawSequence = {0,0,0};
        String [] game = PlayerString.split(",");
        for(int i=0 ; i < game.length ; i++ ){
            int point = checkWinner(game[i]);
            if(point == 1)
                wonLossDrawSequence[0] += 1;
            else if (point == -1) 
                wonLossDrawSequence[1] -= 1;
            else 
                wonLossDrawSequence[2] += 1;
        
        } 
        return wonLossDrawSequence;
    
    }
    public static void main(String args[]){

        Scanner sc = new Scanner(System.in);
        String gamePLayed = sc.nextLine();
        int [] points = new int[3];
        points = pointsCalculatedfromGame(gamePLayed);
        System.out.println(points[0]+","+points[1]+",="+points[2]);
        
    }
}