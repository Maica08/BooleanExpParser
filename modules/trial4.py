from typing import List, Dict, Any

operators = {'+': 3, '*': 2, '!': 1}
delimiter = ['(', ')']

def precedence(expression: str) -> Dict:
    result = {}
    
    # initial test
    exp = expression.strip()
    if exp[0] == '(' and exp[-1] == ')':
    # Check if the expression is fully enclosed in parentheses
        if exp.count('(') == 1 and exp.count(')') == 1 and exp.index('(') == 0 and exp.rindex(')') == len(exp) - 1:
            exp = exp[1:-1]
        

            
    # check if there is parenthesis
    parenthesis_count = 0
    # base
    max_weight = 0
    current_operator = None
    current_operator_index = None
    
    
    # counter
    i = 0      
    while i in range(len(exp)):
        if exp[i] ==  '(':
            parenthesis_count += 1
        elif exp[i] == ')':
            parenthesis_count -= 1
        elif exp[i] in operators and parenthesis_count == 0:
            if operators[exp[i]] > max_weight:
                max_weight = operators[exp[i]]
                current_operator = exp[i]
                current_operator_index = i
        
        i += 1
        
                
    if not current_operator:
        return exp
            
    left_exp = exp[:current_operator_index].strip()
    right_exp = exp[current_operator_index + 1:].strip()
    
    result[current_operator] = [precedence(left_exp), precedence(right_exp)]
    
    
    # if expression[0] == "(":
    #     result[current_operator].insert(0, "(")
    #     result[current_operator].insert(1, ")")
        
    # for value in result[current_operator]:
    #     value = precedence(value)            
        
    return result

def parenthesis_pair(string:str):
    pass

if __name__ == "__main__":
    a = "A * ((A + B) + (A + C))"
    print(precedence(a))
