using System.Collections.Generic;

public class Solution {
    public int RomanToInt(string s) {

        Dictionary<char, int> table = new Dictionary<char, int>();
        table.Add('I', 1);
        table.Add('V', 5);
        table.Add('X', 10);
        table.Add('L', 50);
        table.Add('C', 100);
        table.Add('D', 500);
        table.Add('M', 1000);

        int prevInt = 0;
        int total = 0;
        int currentInt;

        for(int i=s.Length-1; i>=0; i--){
            currentInt = table[s[i]];

            if(currentInt >= prevInt) total += currentInt;
            else total -= currentInt;

            prevInt = currentInt;
        }

        return total;

    }
}
