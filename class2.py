class cppMain:
    main = []
    
    def __init__(self):                         #Initializes the C++ main file.
        main.append(r'#include "stdafx.h"')
        main.append("#include <stack>")
        main.append("#include <iostream>")
        main.append("using namespace std;")
        main.append("stack <int> S;")
        main.append("int StackReturn() {")
        main.append("int x = S.top();")
        main.append("S.pop();")
        main.append("return x;")
        main.append("}")
        main.append("int main(){")

    def addToMain(self, code):
        main.append(code)
