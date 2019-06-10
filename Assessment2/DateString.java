import java.util.*;
class DateString{
    public static Boolean isAmbiguous(int firstParam, int secondParam){
        return (firstParam <= 12 && secondParam <= 12);
    }

    public static Boolean dateAmbiguity(String dateString){
        String [] date = dateString.split("/");
        return (isAmbiguous(Integer.parseInt(date[0]),Integer.parseInt(date[1])));

    }
    public static void main(String[] args){
        
        Scanner sc = new Scanner(System.in);
        String  dateString = sc.nextLine();
        System.out.println("The fact that the string is ambiguous is :" +dateAmbiguity(dateString));

    }
}