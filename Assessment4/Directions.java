import java.util.*;

class terminus{
    public static int step_increment(char direction){
        String direct = direction + "";
        HashMap<String,Integer> direction_step_dict = new HashMap<String,Integer>();
        direction_step_dict.put("N",1);
        direction_step_dict.put("S",-1);
        direction_step_dict.put("E",1);
        direction_step_dict.put("W",-1);
        return direction_step_dict.get(direct);
    }
    public static int get_num(String dir){
        int  i=0;
        String num = "";
        while (Character.isDigit(dir.charAt(i))) {
			num += dir.charAt(i);
			i += 1;
		}


        return Integer.parseInt(num);
    }
    public static int [] step_NSEW(int[] point, char direction , int mul_value){
        if(direction == 'N' || direction == 'S'){
            point[1] += mul_value * step_increment(direction);
        }
        else {
            point[0] += mul_value * step_increment(direction);
        }
        return point;
    }

    public static int [] terminus1(int[] point , Vector steps){
        Enumeration e=steps.elements(); 
        int i=0; 
        while(e.hasMoreElements()){  
         String direction = steps.get(i).toString();
         System.out.println(direction);
         i++;
         char dir_char = direction.charAt(direction.length()-1);
         char dir_char2 = direction.charAt(direction.length()-2);
         if(Character.isDigit(dir_char)){
            point = step_NSEW(point,dir_char,get_num(direction));
         }
         else {
            point = step_NSEW(point,dir_char,get_num(direction)); 
            point = step_NSEW(point,dir_char2,get_num(direction));
         }
        }  
        for (int j=0 ;j < 2 ; j++)
            System.out.println(point[j]);

        return point;
    }
    public static void main(String args[]){
        int [] point = {1,1};
        Vector dir = new Vector();
        dir.add("1N");
        dir.add("10NW");
        point = terminus1(point,dir);
        for (int i=0 ;i < 2 ; i++)
            System.out.println(point[i]);

    }
}