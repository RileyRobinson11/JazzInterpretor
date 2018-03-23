#README
#Name: Daniel McGinnis, Riley Robinson
#Class: EECS3550:001 Software Engineering
#Project: Programming Assignment 1 Jaz to C++ Translator
#03/22/2018
#Description: This program takes programs written in the Jaz
# machine instruction set as input and converts them to the equivalent
# C++ code.
#Status: The program is not 100% functional. Please review the accompanying
# documentation for a complete explanation.

class StackObject:
    stack    = []

    def top(self):                                           #####Returns the value on top of the stack and then removes it.
        value = 0
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value      
    
    def secondFromTop(self):                                 #####Returns the value second from the top
        return self.stack[-2]
   
    def push(self, value):                                   #####Adds a value to the top of the stack.
        self.stack.append(value)
    
    def destroyTop(self):                                    #####Removes value from top of stack returns and nothing.
        self.stack = self.stack[:-1]
    
    def look(self):                                          #####Returns the value on top of the stack.
        return self.stack[-1]
    
class cppMain:
    main = []
    
    def __init__(self):                                      #####Initializes the C++ main file.
        self.main.append(r'#include "stdafx.h"')
        self.main.append("#include <stack>")
        self.main.append("#include <iostream>")
        self.main.append("using namespace std;")
        self.main.append("stack <int> S;")
        self.main.append("int s1 = 0;")
        self.main.append("int s2 = 0;")
        self.main.append("int StackReturn() {")
        self.main.append("int x = S.top();")
        self.main.append("S.pop();")
        self.main.append("return x;")
        self.main.append("}")
        self.main.append("int main(){")

    def addToMain(self, code):
        self.main.append(code)

    def saveFile(self):
        cppFile = open('JazCPP.cpp','w')
        
        for x in range(0, len(self.main)):
            cppFile.write(self.main[x]+"\n")
        
            cppFile.close

def subprogramModule(xValue, label, variables): 
    
    if xValue[0] in stackManipulationArray:
        if (xValue[0] == ":="):
             stackManipulationModule(xValue[0], None)
        else:
             variables[xValue[1]] = [xValue[1]]
             stackManipulationModule(xValue[0], xValue[1])
    
    elif xValue[0] in arithArray:
        arithModule(xValue[0])
    elif xValue[0] in logicArray:
        logicModule(xValue[0])
    elif xValue[0] in outputArray:
        outputModule(xValue[0], xValue[1])

        
def stackManipulationModule(operator, opInput):
    input = opInput
    code = ""
    varValue    =   ""
    varName     =   0

    if operator == "push":
        input = "S.push("+ input + ");"
        cpp.addToMain(input)
        if opInput.isdigit():
            S.push(int(opInput))
        else:
            S.push(opInput)
            
    elif operator == "rvalue":                  
        if opInput == "":
            S.push(0)
            cpp.addToMain("S.push(0);")
        else:
            S.push(varStore[opInput])
            cpp.addToMain("S.push(" + opInput + ");")
            
            
    elif operator == "lvalue": 
            S.push(opInput)
            cpp.addToMain("S.push(" + opInput + ");")
        
    elif operator == "pop":
        cpp.addToMain("S.pop();")
        S.destroyTop()
        
    elif operator == ":=":                     
        varValue    =   S.top();
        varName     =   S.top();
        varStore[varName ] = varValue
        code = "int " + str(varName) + " = " + str(varValue) +";"
        cpp.addToMain(code)
        
    elif operator == "copy":
        cpp.addToMain("S.push(S.top());")
        S.push(S.look())

def arithModule(operator):
    if operator == "+":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 + s2);")
        S.push(S.secondFromTop() + S.top())
        
    elif operator == "-":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 - s2);")
        S.push(S.secondFromTop() - S.top())
        
    elif operator == "*":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 * s2);")
        S.push(S.secondFromTop() * S.top())
        
    elif operator == "/":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 / s2);")
        S.push(S.secondFromTop() // S.top())
        
    elif operator == "div":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 % s2);")
        S.push(S.secondFromTop() % S.top())
        
def relationModule(operator):
    for x in range(0, len(cpp.main)):
        print(cpp.main[x])
    if operator == "<>":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 != s2);")
        if S.secondFromTop() == S.top():
            S.push(0)
        else:
            S.push(1)
            
    elif operator == "<=":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 <= s2);")
        if S.secondFromTop() <= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">=":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 >= s2);")
        if S.secondFromTop() >= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "<":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 < s2);")
        if S.secondFromTop() < S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 > s2);")
        if S.secondFromTop() > S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "=":
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 == s2);")
        if S.secondFromTop() == S.top():
            S.push(1)
        else:
            S.push(0)
            
def logicModule(operator):
    if operator == "&":
        S.push(S.top() and S.top())
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 & s2);")
        
    elif operator == "!":
        S.push(int(not S.top()))
        cpp.addToMain("S.push(!StackReturn());")
    elif operator == "|":
        S.push(S.top() or S.top())
        cpp.addToMain("s2 = StackReturn();")
        cpp.addToMain("s1 = StackReturn();")
        cpp.addToMain("S.push(s1 | s2);")
        
def outputModule(operator, opInput):
    code = ""
    if operator == "print":
        print(S.look())
        cpp.addToMain("cout << S.top() << endl;")
        
    elif operator == "show":
        if opInput == "":
            print("")
            #cpp.addToMain('cout << "" << endl;')
        else:
            print(opInput)
            mopInput = opInput
            
            mopInput = mopInput.replace('"','')
            
            code = ('cout <<' + '"' + mopInput + '"' + ' << endl;')
            cpp.addToMain(code)
            
with open("operatorsTest.jaz") as f:                                                    ########READS FILE LINE BY LINE
    jazzfile = f.readlines()                                                            #########SPLITS ELEMENTS AND PLACES THEM INTO ARRAY CALLED JAZZ FILE

jazzfile    = [x.strip() for x in jazzfile]               
splitLines = [x.split(' ', 1) for x in jazzfile]        

arithArray    = ["+", "-", "/", "div", "*"]                                             #######CREATE ARRAYS 
relationArray = ["<>", "<=", ">=", "<", ">", "="]
logicArray    = ["&", "!", "|"]
outputArray   = ["print", "show"]
stackManipulationArray = ["push", "rvalue", "lvalue", "pop", ":=", "copy"]
subProgramArray = ["begin", "end", "return", "call"]

S           = StackObject()                                                             #########INITIALIZE DATA STRUCUTRES
cpp         = cppMain()
variables   = {}
varStore    = {}                                        
labelIndex  = {}

num = 0
lastCall = []
    
while num < max(range(len(splitLines))) + 1:
          
    if splitLines[num][0] in stackManipulationArray:                                    #######STACK MANIPULATION ARRAY
        try:
            stackManipulationModule(splitLines[num][0], splitLines[num][1])
        except:
            stackManipulationModule(splitLines[num][0], "")
                       
    elif splitLines[num][0] == "label":                                                 #####CONTROL FLOW 
        cpp.addToMain("LABEL " + splitLines[num][1])
        lastCall = splitLines[num][1]
            
    elif splitLines[num][0] == "goto":
         cpp.addToMain("goto " + splitLines[num][1])    
    elif splitLines[num][0] == "gofalse":
        if S.top() == 0:
            num = labelIndex[splitLines[num][1]] 
            
    elif splitLines[num][0] == "gotrue":
        if S.top() != 0:
            num = labelIndex[splitLines[num][1]]
            
    elif splitLines[num][0] == "halt":
        cpp.addToMain('system("pause");')
        cpp.addToMain("return 0;")
        cpp.addToMain("}")
        break                                          
        
    elif splitLines[num][0] in arithArray:                                              ####ARITHMETIC ARRAY
        arithModule(splitLines[num][0])
                        
    elif splitLines[num][0] in logicArray:                                              ####LOGICAL ARRAY
        logicModule(splitLines[num][0])
                                                                                        ####RELATIONAL ARRAY               
    elif splitLines[num][0] in relationArray:
        relationModule(splitLines[num][0])                        
                                                                                        ####OUTPUT ARRAY                
    elif splitLines[num][0] in outputArray:
        try:
            outputModule(splitLines[num][0], splitLines[num][1])
        except:
            outputModule(splitLines[num][0], "")
                                                                                        ####SUBPROGRAM ARRAY  
    elif splitLines[num][0] in subProgramArray:
        while(splitLines[num][0] != "end"):
            subprogramModule(splitLines[num], labelIndex, variables)
            num = num + 1
        
    num = num + 1

for x in range(0, len(cpp.main)):
    print(cpp.main[x])

cpp.saveFile()


