class StackObject:
    stack    = []

    def top(self):                              #Returns the value on top of the stack and then removes it.
        value = 0
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value      
    
    def secondFromTop(self):                    #Returns the value second from the top
        return self.stack[-2]
   
    def push(self, value):                      #Adds a value to the top of the stack.
        self.stack.append(value)
    
    def destroyTop(self):                       #Removes value from top of stack returns and nothing.
        self.stack = self.stack[:-1]
    
    def look(self):                             #Returns the value on top of the stack.
        return self.stack[-1]
    
class cppMain:
    main = []
    
    def __init__(self):                         #Initializes the C++ main file.
        self.main.append(r'#include "stdafx.h"')
        self.main.append("#include <stack>")
        self.main.append("#include <iostream>")
        self.main.append("using namespace std;")
        self.main.append("stack <int> S;")
        self.main.append("int StackReturn() {")
        self.main.append("int x = S.top();")
        self.main.append("S.pop();")
        self.main.append("return x;")
        self.main.append("}")
        self.main.append("int main(){")

    def addToMain(self, code):
        self.main.append(code)



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def subprogramModule(xValue, label, variables): #We need to investigate this.
    
    if xValue[0] in stackManipulationArray:
        if (xValue[0] == ":="):
             stackManipulationModule(xValue[0], None)
        else:
             variables[xValue[1]] = [xValue[1]]
            # functionVar = variables[xValue[1]]
             stackManipulationModule(xValue[0], xValue[1])
        

    elif xValue[0] in arithArray:
        arithModule(xValue[0])
    elif xValue[0] in logicArray:
        logicModule(xValue[0])
    elif xValue[0] in outputArray:
        outputModule(xValue[0], xValue[1])

        

def stackManipulationModule(operator, opInput):
    input = opInput
    if operator == "push":
        input = "S.push("+ input + ");"
        cpp.addToMain(input)
        if opInput.isdigit():
            S.push(int(opInput))
        else:
            S.push(opInput)
            
    elif operator == "rvalue":                  #I am not sure what this does.
        if opInput == "":
            S.push(0)
        else:
            S.push(varStore[opInput])
            
    elif operator == "lvalue":                  #I am not sure what this does.
            S.push(opInput)
        
    elif operator == "pop":
        cpp.addToMain("S.pop();")
        S.destroyTop()
        
    elif operator == ":=":                      #I am not sure what this does.
        varStore[S.top()] = S.top()
        
    elif operator == "copy":
        cpp.addToMain("S.push(S.top());")
        S.push(S.look())

def arithModule(operator):
    if operator == "+":
        cpp.addToMain("S.push(StackReturn() + StackReturn());")
        S.push(S.secondFromTop() + S.top())
        
    elif operator == "-":
        cpp.addToMain("S.push(StackReturn() - StackReturn());")
        S.push(S.secondFromTop() - S.top())
        
    elif operator == "*":
        cpp.addToMain("S.push(StackReturn() * StackReturn());")
        S.push(S.secondFromTop() * S.top())
        
    elif operator == "/":
        cpp.addToMain("S.push(StackReturn() / StackReturn());")
        S.push(S.secondFromTop() // S.top())
        
    elif operator == "div":
        cpp.addToMain("S.push(StackReturn() % StackReturn());")
        S.push(S.secondFromTop() % S.top())
        
def relationModule(operator):
    if operator == "<>":
        cpp.addToMain("S.push(StackReturn() == StackReturn());")
        if S.secondFromTop() == S.top():
            S.push(0)
        else:
            S.push(1)
            
    elif operator == "<=":
        cpp.addToMain("S.push(StackReturn() <= StackReturn());")
        if S.secondFromTop() <= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">=":
        cpp.addToMain("S.push(StackReturn() >= StackReturn());")
        if S.secondFromTop() >= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "<":
        cpp.addToMain("S.push(StackReturn() < StackReturn());")
        if S.secondFromTop() < S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">":
        cpp.addToMain("S.push(StackReturn() > StackReturn());")
        if S.secondFromTop() > S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "=":
        cpp.addToMain("S.push(StackReturn() == StackReturn());")
        if S.secondFromTop() == S.top():
            S.push(1)
        else:
            S.push(0)
            
def logicModule(operator):
    if operator == "&":
        S.push(S.top() and S.top())
        cpp.addToMain("S.push(StackReturn() & StackReturn());")
        
    elif operator == "!":
        S.push(int(not S.top()))
        cpp.addToMain("S.push(~StackReturn());")
    elif operator == "|":
        S.push(S.top() or S.top())
        cpp.addToMain("S.push(StackReturn() | StackReturn());")
        
def outputModule(operator, opInput):
    code = ""
    if operator == "print":
        print(S.look())
        cpp.addToMain("cout << S.top() << endl;")
        
    elif operator == "show":
        if opInput == "":
            print("")
            cpp.addToMain("cout << "" << endl;")
        else:
            print(opInput)
            code = ('cout <<' + opInput + '<< endl;')
            cpp.addToMain(code)
            










with open("demo.jaz") as f:                    #This opens the file, reads it line by line, and stores
    content = f.readlines()                             #each line as an element of an array called content

content    = [x.strip() for x in content]               #This strips newline characters off the end of each line
splitLines = [x.split(' ', 1) for x in content]         #This splits each line at the first space

S           = StackObject()                             #Makes a stack called S
cpp         = cppMain()
variables   = {}
varStore    = {}                                        #Makes a key-value pair data structure (dictionary) called varStore
labelIndex  = {}

arithArray    = ["+", "-", "/", "div", "*"]
relationArray = ["<>", "<=", ">=", "<", ">", "="]
logicArray    = ["&", "!", "|"]
outputArray   = ["print", "show"]
stackManipulationArray = ["push", "rvalue", "lvalue", "pop", ":=", "copy"]
subProgramArray = ["begin", "end", "return", "call"]

#for count in range(len(splitLines)):
 #   if splitLines[count][0] == "label":
  #      labelIndex[splitLines[count][1]] = count
   # print(splitLines[count])                            #THIS IS FOR DEBUGGING
    #count = count + 1
    
num = 0
mostRecentCall = []
    
while num < max(range(len(splitLines))) + 1:
        
    ####STACK MANIPULATIONS####
        
    if splitLines[num][0] in stackManipulationArray:
        try:
            stackManipulationModule(splitLines[num][0], splitLines[num][1])
        except:
            stackManipulationModule(splitLines[num][0], "")
            
    ####CONTROL FLOW####                                #We need to look into these
            
    elif splitLines[num][0] == "label":
        pass
            
    elif splitLines[num][0] == "goto":
       # num = labelIndex[splitLines[num][1]]
         pass    
    elif splitLines[num][0] == "gofalse":
        if S.top() == 0:
            num = labelIndex[splitLines[num][1]] 
            
    elif splitLines[num][0] == "gotrue":
        if S.top() != 0:
            num = labelIndex[splitLines[num][1]]
            
    elif splitLines[num][0] == "halt":
        cpp.addToMain("return 0;")
        cpp.addToMain("}")
        break
        
    ####ARITHMETIC OPERATORS####    
        
    elif splitLines[num][0] in arithArray:
        arithModule(splitLines[num][0])
            
    ####LOGICAL OPERATORS####        
            
    elif splitLines[num][0] in logicArray:
        logicModule(splitLines[num][0])
            
    ####RELATIONAL OPERATORS####        
            
    elif splitLines[num][0] in relationArray:
        relationModule(splitLines[num][0])        
                
    ####OUTPUT####
                
    elif splitLines[num][0] in outputArray:
        try:
            outputModule(splitLines[num][0], splitLines[num][1])
        except:
            outputModule(splitLines[num][0], "")
                
    ####SUBPROGRAM CONTROL####            
    elif splitLines[num][0] in subProgramArray:
        while(splitLines[num][0] != "end"):
            subprogramModule(splitLines[num], labelIndex, variables)
            num = num + 1
        #return
    
    elif splitLines[num][0] == "begin":
        pass
        #Do the begin stuff
            
    elif splitLines[num][0] == "end":
        pass
        #Do the end stuff
            
    elif splitLines[num][0] == "return":
        num = mostRecentCall[-1]
        del mostRecentCall[-1]
            
    elif splitLines[num][0] == "call":
        mostRecentCall.append(num)
        num = labelIndex[splitLines[num][1]]
        
    num = num + 1


for x in range(0, len(cpp.main)):
    print(cpp.main[x])

print(labelIndex) #Will not be part of final code. Debugging purposes only.
print(varStore)   #Will not be part of final code. Debugging purposes only.
print(S)          #Will not be part of final code. Debugging purposes only.

