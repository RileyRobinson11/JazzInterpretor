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

def stackManipulation(operator, opInput):
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

def arith(operator):
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
        
def relation(operator):
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
            
def logic(operator):
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
        
def output(operator, opInput):
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

def subprogram(xValue, label): 
    varA = ""
    if xValue[0] == "call":
       if (len(variablesA)>1):
          for x in range(1, len(variablesA)):
            variablesA[x] = ',' + variablesA[x]
          for x in range(0, len(variablesA)):
            varA = varA + variablesA[x]
          cpp.addToMain(xValue[1] + "(" + varA + ");")
       else:
            varA = variablesA[0]
            cpp.addToMain(xValue[1] + "(" + varA + ");")


    elif xValue[0] == "rvalue":                  
        variablesA.append(xValue[1])
 
    elif xValue[0] == "lvalue": 
        variablesF.append(xValue[1])

    elif xValue[0] in stackManipulationArray:
        pass

    elif xValue[0] in arithArray:
        arith(xValue[0])
    elif xValue[0] in logicArray:
        logic(xValue[0])
    elif xValue[0] in outputArray:
        output(xValue[0], xValue[1]) 
            
JAZfile = open(input("Enter Filename: "),'r')
jazInput = JAZfile.readlines()                                                          #########SPLITS ELEMENTS AND PLACES THEM INTO ARRAY CALLED JAZZ FILE

jazInput   = [x.strip() for x in jazInput]               
jazzLines = [x.split(' ', 1) for x in jazInput]        

varStore    = {} 
variablesF = []
variablesA = []
S           = StackObject()                                                             #########INITIALIZE DATA STRUCUTRES
cpp         = cppMain()                                       
labelIndex  = {}

subProgramArray = ["begin", "end", "return", "call"]
arithArray    = ["+", "-", "/", "div", "*"]                                             #######CREATE ARRAYS 
outputArray   = ["print", "show"]
stackManipulationArray = ["push", "rvalue", "lvalue", "pop", ":=", "copy"]
logicArray    = ["&", "!", "|"]
relationArray = ["<>", "<=", ">=", "<", ">", "="]

num = 0
lastCall = []
    
while num < max(range(len(jazzLines))) + 1:
          
    if jazzLines[num][0] in stackManipulationArray:                                    #######STACK MANIPULATION ARRAY
        try:
            stackManipulation(jazzLines[num][0], jazzLines[num][1])
        except:
            stackManipulation(jazzLines[num][0], "")
                       
    elif jazzLines[num][0] == "label":                                                 #####CONTROL FLOW 
        cpp.addToMain("LABEL " + jazzLines[num][1])
        lastCall = jazzLines[num][1]
            
    elif jazzLines[num][0] == "goto":
         cpp.addToMain("goto " + jazzLines[num][1])    
    elif jazzLines[num][0] == "gofalse":
        if S.top() == 0:
            num = labelIndex[jazzLines[num][1]] 
            
    elif jazzLines[num][0] == "gotrue":
        if S.top() != 0:
            num = labelIndex[jazzLines[num][1]]
            
    elif jazzLines[num][0] == "halt":
        cpp.addToMain('system("pause");')
        cpp.addToMain("return 0;")
        cpp.addToMain("}")                                          
        
    elif jazzLines[num][0] in arithArray:                                              ####ARITHMETIC ARRAY
        arith(jazzLines[num][0])
                        
    elif jazzLines[num][0] in logicArray:                                              ####LOGICAL ARRAY
        logic(jazzLines[num][0])
                                                                                        ####RELATIONAL ARRAY               
    elif jazzLines[num][0] in relationArray:
        relation(jazzLines[num][0])                        
                                                                                        ####OUTPUT ARRAY                
    elif jazzLines[num][0] in outputArray:
        try:
            output(jazzLines[num][0], jazzLines[num][1])
        except:
            output(jazzLines[num][0], "")
                                                                                        ####SUBPROGRAM ARRAY  
    elif jazzLines[num][0] in subProgramArray:
        while(jazzLines[num][0] != "end" and jazzLines[num][0] !="return"):
            subprogram(jazzLines[num], labelIndex)
            num = num + 1
        
    num = num + 1

for x in range(0, len(cpp.main)):
    print(cpp.main[x])

cpp.saveFile()

