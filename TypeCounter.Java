import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
//import org.apache.log4j.Logger;



class Result {

    /*
     * Complete the 'typeCounter' function below.
     *
     * The function accepts STRING sentence as parameter.
     */

 // private static final Logger logger = Logger.getLogger(Result.class);

   public static void typeCounter(String sentence) {
  // Check if the input is empty or null
  if (sentence == null || sentence.isEmpty()) {
    // Print zero counts for all data types
    System.out.println("string 0");
    System.out.println("integer 0");
    System.out.println("double 0");
    // Return from the function
    return;
  }
  // Trim the input to remove leading or trailing spaces
  sentence = sentence.trim();
  // Split the input string by one or more spaces
  String[] substrings = sentence.split("\\s+");
  // Initialize the count variables
  int stringCount = 0;
  int integerCount = 0;
  int doubleCount = 0;
  // Loop through the substrings
  for (String s : substrings) {
    try {
      // Try to parse as an Integer
      Integer.parseInt(s);
      // If successful, increment integerCount
      integerCount++;
    } catch (NumberFormatException e1) {
      try {
        // Try to parse as a Double
        Double.parseDouble(s);
        // If successful, increment doubleCount
        doubleCount++;
      } catch (NumberFormatException e2) {
        // If both parsing fail, check if the substring is a valid string
        if (isValidString(s)) {
          // If yes, increment stringCount
          stringCount++;
        } else {
          // If no, ignore the substring
          continue;
        }
      }
    }
  }
  // Print the results
  System.out.println("string " + stringCount);
  System.out.println("integer " + integerCount);
  System.out.println("double " + doubleCount);
}

// A helper method to check if a substring is a valid string
public static boolean isValidString(String s) {
  // Loop through the characters of the substring
  for (char c : s.toCharArray()) {
    // Check if the character is a lowercase English letter
    if (c < 'a' || c > 'z') {
      // If not, return false
      return false;
    }
  }
  // If all characters are lowercase English letters, return true
  return true;
}
   
   
   

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String sentence = bufferedReader.readLine();

        Result.typeCounter(sentence);

        bufferedReader.close();
    }
}
