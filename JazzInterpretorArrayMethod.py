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