//Leetcode 13. Roman to Integer

class BruteForceSolution {
public:
    int romanToInt(string s) {
        int total = 0;
        for(int i = 0; i < (int)s.size(); i++){
            char current = s[i];
            switch(current) {
                case 'I':
                    if(s[i+1] == 'V') {
                        total += 4;
                        i ++;
                        break;
                    }
                    else if(s[i+1] == 'X') {
                        total += 9;
                        i++;
                        break;
                    }
                    else {
                        total += 1;
                        break;
                    }
                case 'V':
                    total += 5;
                    break;
                case 'X':
                     if(s[i+1] == 'L') {
                        total += 40;
                        i ++;
                        break;
                    }
                    else if(s[i+1] == 'C') {
                        total += 90;
                        i++;
                        break;
                    }
                    else {
                        total += 10;
                        break;
                    }
                case 'L':
                    total += 50;
                    break;
                case 'C':
                    if(s[i+1] == 'D') {
                        total += 400;
                        i ++;
                        break;
                    }
                    else if(s[i+1] == 'M') {
                        total += 900;
                        i++;
                        break;
                    }
                    else {
                        total += 100;
                        break;
                    }
                case 'D':
                    total += 500;
                    break;
                case 'M':
                    total += 1000;
                    break;
            }
        }
        return total;
    }
};

class Solution {
public:
    int romanToInt(string s) {
        //create map of the possible chars and their integer values
        unordered_map<char,int> values = { {'I', 1},
                                           {'V', 5},
                                           {'X', 10},
                                           {'L', 50},
                                           {'C', 100},
                                           {'D', 500},
                                           {'M', 1000} };
        
        //init the sum, or total, with the last number
        int sum = values[s.back()];
        //go from 2nd to last to front. if a value is greater/equal than the next, it can be added, else, subtracted
        for(int i = s.length() - 2; i >= 0; i--) {
            if(values[s[i]] >= values[s[i+1]]) {
                sum += values[s[i]];
            }
            else {
                sum -= values[s[i]];
            }
        }
        
        return sum;
        
    }
};
