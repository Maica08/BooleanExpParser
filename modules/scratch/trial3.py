from typing import Dict, List

def split_by_outermost_operator(expression, operator):
    paren_count = 0
    current_expression = ""
    split_expressions = []

    for char in expression:
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1

        if paren_count == 0 and char == operator:
            split_expressions.append(current_expression)
            current_expression = ""
        else:
            current_expression += char

    split_expressions.append(current_expression)
    
    return split_expressions


def get_operator_paren(expressions, operators):
    paren_count = 0
    cur_operator = None
    max_value = 0
        
    if expressions[0].strip() == '(':
        expressions = expressions[1:-1]
        
    for i in range(len(expressions) - 1, -1, -1):
        char = expressions[i]
        if char == ')':
            paren_count += 1
        elif char == '(':
            paren_count -= 1
        elif char in operators and paren_count == 0:
            if operators[char] > max_value:
                max_value = operators[char]
                cur_operator = char  
            
            
    return cur_operator


def precedence(expressions: str) -> Dict:
    operators = {'+': 3, '*':  2, '!': 1}    
    
    if "(" and ")" in expressions:
        cur_operator = get_operator_paren(expressions=expressions, operators=operators)
        div_expression = [exp for exp in split_by_outermost_operator(expression=expressions, operator=cur_operator)]

    else:
        max_val = 0
        cur_operator = None
    
        for expression in expressions:
            if expression in operators:
                if operators[expression] > max_val:
                    cur_operator = expression
                    
        div_expression = [exp.strip() for exp in expressions.split(cur_operator)]
                
    if not cur_operator:
        return expressions
            
    
    for i in range(len(div_expression)):
        if isinstance(div_expression[i], str):
            div_expression[i] = precedence(div_expression[i])
    
    div_expression = [exp for exp in div_expression if exp]
    
    order = {cur_operator: div_expression}
    return order

a = "!B * (D * (A + C))"    
result = precedence(a)

b = "((A + C) * D)"
operators = {'+': 3, '*':  2, '!': 1}
# print(get_operator_paren(a, operators))
print(precedence(a))
# print(split_by_outermost_operator(a, '*'))