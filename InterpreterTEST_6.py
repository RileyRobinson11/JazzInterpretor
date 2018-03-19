# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 19:09:11 2017

@authors: Alex Kneisel and James Vince
"""

from queue_stack import Stack

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def subprogramModule(xValue, label, variables):
    
    if xValue[0] in stackManipulationArray:
        if is_number(xValue[1]):
             stackManipulationModule(xValue[0], xValue[1])
        else:
            functionVar = variables[xValue[1]]
            stackManipulationModule(xValue[0], functionVar)
       
    elif xValue[0] in arithArray:
        arithModule(xValue[0])
    elif xValue[0] in logicArray:
        logicModule(xValue[0])
    elif xValue[0] in outputArray:
        outputModule(xValue[0], xValue[1])

        

def stackManipulationModule(operator, opInput):
    if operator == "push":
        if opInput.isdigit():
            S.push(int(opInput))
        else:
            S.push(opInput)
            
    elif operator == "rvalue":
        if opInput == "":
            S.push(0)
        else:
            S.push(varStore[opInput])
            
    elif operator == "lvalue":
        S.push(opInput)
        
    elif operator == "pop":
        S.destroyTop()
        
    elif operator == ":=":
        varStore[S.top()] = S.top()
        
    elif operator == "copy":
        S.push(S.look())

def arithModule(operator):
    if operator == "+":
        S.push(S.top() + S.top())
        
    elif operator == "-":
        S.push(S.secondFromTop() - S.top())
        
    elif operator == "*":
        S.push(S.top() * S.top())
        
    elif operator == "/":
        S.push(S.secondFromTop() // S.top())
        
    elif operator == "div":
        S.push(S.secondFromTop() % S.top())
        
def relationModule(operator):
    if operator == "<>":
        if S.secondFromTop() == S.top():
            S.push(0)
        else:
            S.push(1)
            
    elif operator == "<=":
        if S.secondFromTop() <= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">=":
        if S.secondFromTop() >= S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "<":
        if S.secondFromTop() < S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == ">":
        if S.secondFromTop() > S.top():
            S.push(1)
        else:
            S.push(0)
            
    elif operator == "=":
        if S.secondFromTop() == S.top():
            S.push(1)
        else:
            S.push(0)
            
def logicModule(operator):
    if operator == "&":
        S.push(S.top() and S.top())
        
    elif operator == "!":
        S.push(int(not S.top()))
        
    elif operator == "|":
        S.push(S.top() or S.top())
        
def outputModule(operator, opInput):
    if operator == "print":
        print(S.look())
        
    elif operator == "show":
        if opInput <> "":
            print(opInput)
        else:
            print("")

with open("recFact.jaz") as f:                              #This opens the file, reads it line by line, and stores
    content = f.readlines()                             #each line as an element of an array called content

content    = [x.strip() for x in content]               #This strips newline characters off the end of each line
splitLines = [x.split(' ', 1) for x in content]         #This splits each line at the first space

S          = Stack()    #Makes a stack called S
varStore   = {}         #Makes a key-value pair data structure (dictionary) called varStore
labelIndex = {}

arithArray    = ["+", "-", "/", "div", "*"]
relationArray = ["<>", "<=", ">=", "<", ">", "="]
logicArray    = ["&", "!", "|"]
outputArray   = ["print", "show"]
stackManipulationArray = ["push", "rvalue", "lvalue", "pop", ":=", "copy"]
subProgramArray = ["begin", "end", "return", "call"]

for count in range(len(splitLines)):
    if splitLines[count][0] == "label":
        labelIndex[splitLines[count][1]] = count
    print(splitLines[count])                        #THIS IS FOR DEBUGGING
    count = count + 1
    
num = 0
mostRecentCall = []
    
while num < max(range(len(splitLines))) + 1:
        
    ####STACK MANIPULATIONS####
        
    if splitLines[num][0] in stackManipulationArray:
        try:
            stackManipulationModule(splitLines[num][0], splitLines[num][1])
        except:
            stackManipulationModule(splitLines[num][0], "")
            
    ####CONTROL FLOW####
            
    elif splitLines[num][0] == "label":
        pass
            
    elif splitLines[num][0] == "goto":
        num = labelIndex[splitLines[num][1]]
            
    elif splitLines[num][0] == "gofalse":
        if S.top() == 0:
            num = labelIndex[splitLines[num][1]]
            
    elif splitLines[num][0] == "gotrue":
        if S.top() != 0:
            num = labelIndex[splitLines[num][1]]
            
    elif splitLines[num][0] == "halt":
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
        while(splitLines[num][0] != "return"):
            subprogramModule(splitLines[num], labelIndex, varStore)
            num = num + 1
        return
        
        
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

print(labelIndex) #Will not be part of final code. Debugging purposes only.
print(varStore)   #Will not be part of final code. Debugging purposes only.
print(S)          #Will not be part of final code. Debugging purposes only.