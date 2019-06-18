class Pangram{
    public static Boolean isPangram(String sentence){
        char[] ch = sentence.toLowerCase().toCharArray();
        int[] letter_array = new int[26];
        for (int i=0 ; i< ch.length ; i++){
            try {
                letter_array[(int)ch[i] - 97] = 1;

            }
            catch(Exception e){
                continue;
            }
        }
        for (int i =0; i < 26 ; i++){
            if(letter_array[i] == 0)
                return false;
        }
        return true;
    }
    public static void main (String args[]){
        String sentence = "Pack my box with five dozen liquor jugs.";
        System.out.println("The fact that the input string is a panagram is : " +isPangram(sentence));
    }
}