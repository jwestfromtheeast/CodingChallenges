//Leetcode 14. Longest Common Prefix

class FirstSolution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) return ""; //edge case: empty array
        string common = "";
        for(int i = 0; i < strs[0].length(); i++) { //iterate thru letters
            for(int j = 0; j < (int)strs.size() - 1; j++) {  //iterate thru strings
                if(strs[j][i] != strs[j+1][i]) {
                    return common; //if one fails to meet, return what you have
                }
            }
            common += strs[0][i]; //if there is a full pass, you know they all share that char
        }
        
        return common; //return final string (if you get here, will be equivalent to string 1)
    }
};
