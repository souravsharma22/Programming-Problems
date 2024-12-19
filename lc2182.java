public class lc2182 {

    public static String repeatLimitedString(String s, int repeatLimit) {
        int[] freq = new int[26];  // Array to store frequency of each character
        StringBuilder result = new StringBuilder();  // To store the result string
        
        // Count the frequency of each character
        for (char ch : s.toCharArray()) {
            freq[ch - 'a']++;
        }
        
        int repeatCount = 0;  // Track how many times the current character is repeated
        int i = 25;  // Start from 'z'
        
        // Construct the string by selecting characters from 'z' to 'a'
        while (i >= 0) {
            // Skip if there are no more characters of the current type
            if (freq[i] == 0) {
                i--;  
                continue;
            }

            // If we can add more of the current character without exceeding the repeat limit
            int countToAdd = Math.min(freq[i], repeatLimit - repeatCount);
            for (int j = 0; j < countToAdd; j++) {
                result.append((char) (i + 'a'));
            }
            
            // Update repeatCount and frequency of the character
            repeatCount += countToAdd;
            freq[i] -= countToAdd;
            
            // If we hit the repeat limit, reset repeatCount
            if (repeatCount == repeatLimit) {
                repeatCount = 0;
            }

            // If the current character is exhausted, move to the next available character
            if (freq[i] == 0) {
                i--;
            }
        }

        return result.toString();  // Return the result string
    }

    public static void main(String[] args) {
        String str = repeatLimitedString("aababab", 2);  // Example input
        System.out.println(str.charAt(0));
        System.out.println(str);  // Output the result
    }
}
