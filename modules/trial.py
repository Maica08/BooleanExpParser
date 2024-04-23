from typing import List, Dict
from tokenizer import Tokenize



# def precedence(exp: str) -> Dict[str, List[str]]:
#     order = {}
#     tokens = Tokenize(exp)
#     tokenized = tokens.tokenize()
    
#     # Handle parentheses first
#     while '(' in exp:
#         # Find innermost parentheses
#         start = exp.rfind('(')
#         end = exp.find(')', start)
        
#         # Extract expression within parentheses
#         inner_exp = exp[start + 1:end]
        
#         # Recursively call precedence to handle inner expression
#         inner_order = precedence(inner_exp)
        
#         # Replace inner expression with a placeholder
#         exp = exp[:start] + 'placeholder' + exp[end + 1:]
        
#         # Add inner expression's order to the main order
#         for op, (left, right) in inner_order.items():
#             order[op] = [left.replace('placeholder', inner_order[op][0]),
#                           right.replace('placeholder', inner_order[op][1])]
    
#     # Continue with the rest of the expression
#     operators = [row for row in Tokenize(exp).tokenize() if row["type"] == "operator"]
#     operators = sorted(operators, key=lambda x: x["weight"], reverse=True)
    
#     remaining_exp = exp
#     for operator in operators:
#         operator_value = operator["value"]
#         left, op, right = remaining_exp.partition(operator_value)
#         order[operator_value] = [left.strip(), right.strip()]
#         remaining_exp = left if len(left) > len(right) else right

#     # Handle edge case where expression doesn't have both left and right side
#     if remaining_exp:
#         order[''] = [remaining_exp, '']
    
#     return order


# def precedence(exp: str) -> Dict[str, List[str]]:
#     order = {}
#     tokens = Tokenize(exp)
#     tokenized = tokens.tokenize()
#     operators = [row for row in tokenized if row["type"] == "operator"]
#     operators = sorted(operators, key=lambda x: x["weight"], reverse=True)

#     def split_expression(expression):
#         for operator in operators:
#             operator_value = operator["value"]
#             parts = expression.split(operator_value)
#             if len(parts) > 1:
#                 return operator_value, parts
#         return None, [expression]

#     def build_tree(expression):
#         operator, parts = split_expression(expression)
#         if operator:
#             left, right = parts[0].strip(), parts[1].strip()
#             order[operator] = [build_tree(left), build_tree(right)]
#         else:
#             return expression.strip()

#     root = build_tree(exp)
#     return order


# def precedence(exp: str) -> Dict:
#     order = {}
#     tokens = Tokenize(exp)
#     tokenized = tokens.tokenize()
#     operators = [row for row in tokenized if row["type"] == "operator"]
#     operators = sorted(operators, key=lambda x: x["weight"], reverse=True)
    
#     temp_exp = exp
#     for operator in operators:
#         operator_counter = temp_exp.count(operator["value"])
#         for count in range(operator_counter):
#             operator_index = -1  
#             for i, c in enumerate(temp_exp):
#                 if c == operator["value"]:
#                     operator_index = i 
#                     print(c, operator_index)
                    
#             expressions = [temp_exp[0: operator_index]] + [temp_exp[operator_index + 1:]]
#             print(expressions)

#         cur_operator = temp_exp[operator_index]
#         if len(expressions) == 2:
#             left = expressions[0].strip()
#             right = expressions[1].strip()
#         if '' in expressions:
#             left = expressions[0] if expressions[0] != '' else expressions[1]
#             right = ''
                
            
#         order[cur_operator] = [left, right]
#         if len(left) > len(right):
#             temp_exp = left
#         else:
#             temp_exp = right
        
#         print(order)
            
#     return order
        
# expr = "!A * B + C + D"
# # expr = "(!A + C) * (B + C)"
# print(precedence(expr))    


# def precedence(exp: str) -> Dict:
#     order = {}
#     tokens = Tokenize(exp)
#     tokenized = tokens.tokenize()
#     operators = [row for row in tokenized if row["type"] == "operator"]
#     operators = sorted(operators, key=lambda x: x["weight"], reverse=True)
    
#     temp_exp = exp
#     for operator in operators:
#         expressions = temp_exp.split(operator["value"])
#         cur_operator = temp_exp[temp_exp.index(operator["value"])]
#         if len(expressions) == 2:
#             left = expressions[0].strip()
#             right = expressions[1].strip()
#         if '' in expressions:
#             left = expressions[0] if expressions[0] != '' else expressions[1]
#             right = ''
            
#         order[cur_operator] = [left, right]
#         if len(left) > len(right):
#             temp_exp = left
#         else:
#             temp_exp = right
            
#     return order


# def precedence(expressions: str) -> Dict:
#     tokens = Tokenize(expressions)
#     tokenized = tokens.tokenize()
#     operators = {'+': 3, '*':  2, '!': 1}    
    
#     cur_expression = expressions
#     order = {}
#     max_val = 0
#     cur_operator = ''
#     # getting current operator
#     for expression in cur_expression:
#         if expression in operators:
#             if operators[expression] > max_val:
#                 cur_operator = expression
                
#     div_expression = [exp.strip() for exp in cur_expression.split(cur_operator)]
    
#     order[cur_operator] = div_expression
    
#     return order

def parenthesize(exp):
    parenthesis_count = 0
    parenthesized = []
    l_parenthesis_count = 0
    start_idx = None
    last_idx = None
    
    counter = 0
    
    while counter in range(len(exp)):
        if exp[counter] == '(':
            parenthesis_count += 1
            l_parenthesis_count += 1
            if l_parenthesis_count > 1:
                pass
            else:
                start_idx = counter
        elif exp[counter] == ')':
            l_parenthesis_count -= 1
            parenthesis_count -= 1
            last_idx = counter
        
        if parenthesis_count == 0 and start_idx:
            parenthesized_exp = exp[start_idx:last_idx + 1]
            parenthesized.append(parenthesized_exp)
            start_idx = None
            last_idx = None
        
        
        counter += 1
    return parenthesized

def split_by_outermost_operator(expression, operator):
    paren_count = 0
    current_expression = ""
    split_expressions = []

    for char in expression:
        if char == '(':
            if paren_count == 0:
                split_expressions.append(current_expression.strip())
                current_expression = ""
            paren_count += 1
        elif char == ')':
            paren_count -= 1
            if paren_count == 0:
                split_expressions.append(current_expression.strip())
                current_expression = ""
        elif char == operator and paren_count == 0:
            split_expressions.append(current_expression.strip())
            current_expression = ""
        else:
            current_expression += char

    if current_expression:
        split_expressions.append(current_expression.strip())

    return split_expressions



def get_operator_paren(expressions, operators):
    paren_count = 0
    cur_operator = None
    
    temp_exp = expressions
    if temp_exp[0] == "(" and temp_exp[-1] == ")":
        temp_exp = temp_exp[1:-1]  
                
    for i in range(len(temp_exp) - 1, -1, -1):
        char = temp_exp[i]
        if char == ')':
            paren_count += 1
        elif char == '(':
            paren_count -= 1
        elif char in [operator for operator in operators] and paren_count == 0:
            cur_operator = char
            break  
    
    return cur_operator



def precedence(expressions: str) -> Dict:
    operators = {'+': 3, '*':  2, '!': 1}    
    
    if "(" and ")" in expressions:
        cur_operator = get_operator_paren(expressions=expressions, operators=operators)
        print(expressions)
        div_expression = split_by_outermost_operator(expression=expressions, operator=cur_operator)

    else:
        print(expressions)
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

expression = " !B + (D*(A + C))"
result = precedence(expression)
# result = get_operator_paren(expression, {'+': 3, '*':  2, '!': 1})
print(result)



# def precedence(expressions: str) -> Dict:
#     operators = {'+': 3, '*':  2, '!': 1}    
    
#     # Base case: if the expression is a single operand, return it
#     if len(expressions) == 1:
#         return expressions
    
#     # Find the rightmost lowest-precedence operator that is not within parentheses
#     paren_count = 0
#     for i in range(len(expressions) - 1, -1, -1):
#         char = expressions[i]
#         if char == ')':
#             paren_count += 1
#         elif char == '(':
#             paren_count -= 1
#         elif char in operators and paren_count == 0:
#             cur_operator = char
#             print(cur_operator)
#             break
#     else:
#         return precedence(expressions[1:-1])
    
#     # Split the expression by the current operator
#     div_expression = [exp.strip() for exp in expressions.split(cur_operator)]
    
#     # Recursively call precedence function for each operand
#     for i in range(len(div_expression)):
#         if isinstance(div_expression[i], str):
#             div_expression[i] = precedence(div_expression[i])
    
#     # Filter out empty strings
#     div_expression = [exp for exp in div_expression if exp]
    
#     # Construct the result
#     order = {cur_operator: div_expression}
#     return order

# expression = "!A * (B + C) + D"
# result = precedence(expression)
# print(result)

            
# exp = "!A * B + C + D"
# print(precedence(exp))

"""
{
    '+'  : [A! * B, C, D]                       1
    '+'  : [{*: [A!, B]}, C, D]                 2
    '+'  : [{*: [{!: A}, B]}, C, D]             3
}

[{+: [A! * B + C, D]}`
 {+: [A! * B, C]}
 {*: [A!, B]}
 {!: [A]}
]
"""

"""
A * B + A * C * !B
[
    {+: [A * B, A * C * !B]}
    {*: [A * B, A * C * !B]}
    
]
"""

"""
{
    '+': [{'*': [{'!': ['A']},'B']},'C','D']
}

"""

"""
()()
(())
"""