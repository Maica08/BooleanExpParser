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

