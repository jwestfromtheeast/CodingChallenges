class InitialSolution {
public:
    bool isValid(string s) {
        stack<char> open;
        unsorted
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
                open.push(s[i]);
            }
            else {
                if(open.empty()) return false;
                else {
                    if(open.top() == '(' && s[i] == ')') {
                        open.pop();
                    }
                    else if(open.top() == '[' && s[i] == ']') {
                        open.pop();
                    }
                    else if(open.top() == '{' && s[i] == '}') {
                        open.pop();
                    }
                    else {
                        return false;
                    }
                }
            }
        }
        if(open.empty()) {
            return true;
        }
        else {
            return false;
        }
    }
};
