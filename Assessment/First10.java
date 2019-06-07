import java.util.*;
class First10{
    public static Boolean iscalculateExpression(int a ,int b,int c){
        a = math.pow(a,3);
        b = math.pow(b,3);
        c = math.pow(c,2); 
        return a + b == c;        
    }
    public static Vector generateTriples(){
        Vector triple = new Vector();
        a = 1;
        b = 2;
        c = 3;
        while(triple.size() < 10){
            if (iscalculateExpression(a,b,c)){
                Vector tripl = new Vector ();
                triple.add(tripl);

            }
            a += 1;
            b += 1;
            c += 1;
        }
        return triple;
    }
    public static void main(String[] args){
        Vector triple = new Vector();
        triple = generateTriples();
        Enumeration vEnum = triple.elements();
        while(vEnum.hasMoreElements())
            System.out.print(vEnum.nextElement() + " ");
    }
}