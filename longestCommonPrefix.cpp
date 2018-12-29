//Leetcode 14. Longest Common Prefix

class FirstSolution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) return "";
        string common = "";
        for(int i = 0; i < strs[0].length(); i++) {
            for(int j = 0; j < (int)strs.size() - 1; j++) { 
                if(strs[j][i] != strs[j+1][i]) {
                    return common;
                }
            }
            common += strs[0][i];
        }
        
        return common;
    }
};
