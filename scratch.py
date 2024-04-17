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

# from sympy.logic import 

var = ['-A', 'B']
for i in range(len(var)):
    print(i)

