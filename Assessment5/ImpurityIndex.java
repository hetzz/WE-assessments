class Impurity{
    public static int[] letter_occurence_computation(String sentence){
        char[] ch = sentence.toLowerCase().toCharArray();
        int[] letter_array = new int[26];
        for (int i=0 ; i< ch.length ; i++){
            try {
                letter_array[(int)ch[i] - 97] += 1;

            }
            catch(Exception e){
                continue;
            }
        }
        return letter_array;
    }

    public static int impurity_count(String sentence){
        int impurity_index = 0;
        int [] letter_array = Letter_occurence_computation(sentence);
        char [] vowels = {'a','e','i','o','u'};
        int [] impurity_increment = {0, 0.5, 0.7 ,1, 3};
        for (int i = 0; i < 26; i++){
            if(new String(vowels).indexOf(chr(i + 97)) != -1){
                if(letter_array[i] == 2) 
                    impurity_index += impurity_increment[1];
            }
            if(new String(vowels).indexOf(chr(i + 97)) == -1 && letter_array[i] == 2)
                impurity_index += impurity_increment[2];
            if(letter_array[i] == 3)
                impurity_index += impurity_increment[3];
            if(letter_array[i] > 3)
                impurity_index += impurity_increment[4];
        }
        return (impurity_index);
    }
    public static void main(String args[]){
        String s = "Old brother fox jumps over the lazy dog.";
        System.out.println(impurity_count(sentence));
    }
}