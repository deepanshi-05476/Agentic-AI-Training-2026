/*
LeetCode #13: Roman to Integer

Approach:
Traverse the string and compare the current value
with the next value. If current < next, subtract it;
otherwise add it.

*/
import java.util.*;

class Main {

    public static int value(char ch){
        if(ch == 'I') return 1;
        if(ch == 'V') return 5;
        if(ch == 'X') return 10;
        if(ch == 'L') return 50;
        if(ch == 'C') return 100;
        if(ch == 'D') return 500;
        if(ch == 'M') return 1000;
        return 0;
    }

    public static int romanToInt(String s){

        int ans = 0;

        for(int i = 0; i < s.length(); i++){

            int curr = value(s.charAt(i));

            if(i < s.length() - 1){
                int next = value(s.charAt(i + 1));

                if(curr < next){
                    ans -= curr;
                } else {
                    ans += curr;
                }
            } else {
                ans += curr;
            }
        }

        return ans;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Roman Numeral: ");
        String s = sc.next();

        System.out.println("Integer Value = " + romanToInt(s));
    }
}

/*Example:
Input: "MCMXCIV"

M = 1000  -> +1000
C = 100   -> -100
M = 1000  -> +1000
X = 10    -> -10
C = 100   -> +100
I = 1     -> -1
V = 5     -> +5

Output: 1994

Time Complexity: O(n)
Space Complexity: O(1)
*/
