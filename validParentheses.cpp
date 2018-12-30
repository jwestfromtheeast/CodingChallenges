class InitialSolution {
public:
    bool isValid(string s) {
        stack<char> open; //stack is perfect here. LIFO, so last thing we add closes first.
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{') { //add open parentheses to the stack.
                open.push(s[i]);
            }
            else {
                if(open.empty()) return false; //avoid calling an empty stack to prevent errors.
                else {
                    if(open.top() == '(' && s[i] == ')') { //match the sets here, pop the set out.
                        open.pop();
                    }
                    else if(open.top() == '[' && s[i] == ']') {
                        open.pop();
                    }
                    else if(open.top() == '{' && s[i] == '}') {
                        open.pop();
                    }
                    else {
                        return false; //mismatched, false.
                    }
                }
            }
        }
        if(open.empty()) { //if you complete the loop and the stack is empty, valid.
            return true;
        }
        else {
            return false; //if you complete the loop and the stack is not empty, there are non-closed still. false.
        }
    }
};

//alternatively use a switch statement
class SecondSolution {
public:
     bool isValid(string s) {
        stack<char> open;
        for (char& c : s) {
            switch (c) {
                case '(': 
                case '{': 
                case '[': open.push(c); break;
                case ')': if (open.empty() || open.top()!='(') return false; else open.pop(); break;
                case '}': if (open.empty() || open.top()!='{') return false; else open.pop(); break;
                case ']': if (open.empty() || open.top()!='[') return false; else open.pop(); break;
                default: ; // pass
            }
        }
        return open.empty() ;
    }
};

