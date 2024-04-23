# detecting variables

# operators = ['-', '.', '+']
# delimiter = ['(', ')', ' ']
# symbols = operators + delimiter

# expression = "AB + AC"
        
# def get_operands(expression):
#     operands = []
#     dist_opr = []

#     for e in expression:
#         if e not in symbols:
#             operands.append(e)

#     dist_opr.append(operands[0])      
#     for operand in operands:
#         temp_var = operands[0]    
#         if temp_var != operand:
#             dist_opr.append(operand)
#             temp_var = operand
            
#     return dist_opr

# print(get_operands(expression))


# var = ['-A', 'B']
# letter = '-B'

# if letter[-1] in var[-1]:
#     print(True)
# else:
#     print(False)

# from sympy.logic import simplify_logic
# from sympy.abc import a, b, c

# exp = " a | a & b | a & c | b & c | d & c"
# print(simplify_logic(exp))

# var = ['-A', 'BC']
# if 'CB' not in var:
#     print(True)

# def extract_distributive(expression):
#     # Split the expression by '+' to get individual terms
#     terms = expression.split('+')
#     result = []

#     for term in terms:
#         # Split each term by '*' to get individual variables
#         variables = term.split('*')

#         # Check if the term contains more than one variable
#         if len(variables) > 1:
#             common_variables = set(variables[0])

#             # Find common variables among terms
#             for var in variables[1:]:
#                 common_variables.intersection_update(var)

#             # If common variables found, apply the distributive property
#             if common_variables:
#                 common_str = ''.join(common_variables)
#                 rest = '+'.join([var.replace(common_str, '') for var in variables])
#                 result.append(common_str + '*' + rest)
#             else:
#                 result.append(term)
#         else:
#             result.append(term)

#     return '+'.join(result)

# print(extract_distributive("AB + AC + D"))

# dic = {'a': 1, 'b': 2, 'c': 2}

# max_value = max(dic.values())
# keys = [key for key in dic if dic[key] == max_value]
# print(keys)

# a = "AC"
# b = "A"
# print(set(a).intersection(set(b)))

# x = not(1 | 0)

# var = "!A * (B + C) + (A + D)"
# vars = var.split('+')


# def parenthesize(exp):
#     parenthesis_count = 0
#     parenthesized = []
#     l_parenthesis_count = 0
#     start_idx = None
#     last_idx = None
    
#     counter = 0
    
#     while counter in range(len(exp)):
#         if exp[counter] == '(':
#             parenthesis_count += 1
#             l_parenthesis_count += 1
#             if l_parenthesis_count > 1:
#                 pass
#             else:
#                 start_idx = counter
#         elif exp[counter] == ')':
#             l_parenthesis_count -= 1
#             parenthesis_count -= 1
#             last_idx = counter
        
#         if parenthesis_count == 0 and start_idx:
#             parenthesized_exp = exp[start_idx:last_idx + 1]
#             parenthesized.append(parenthesized_exp)
#             start_idx = None
#             last_idx = None
        
        
#         counter += 1
#     return parenthesized

# print(parenthesize(var))
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


expression = "(A * (B + C)) + (A + D) + A"
split_expressions = split_by_outermost_operator(expression, '+')
print(split_expressions)
