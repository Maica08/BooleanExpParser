from typing import List

operators = ['-', '.', '+']
delimiter = ['(', ')', ' ']
symbols = operators + delimiter

def get_operands(expression: str | List) -> List:
    operands = []
    dist_opr = []

    for e in expression:
        if e == "-":
            if expression[expression.index(e) + 1] not in symbols:
                operands.append(e + expression[expression.index(e) + 1])
        if e not in symbols:
            operands.append(e)

    dist_opr.append(operands[0])      
    for operand in operands:
        temp_var = operands[0]    
        if temp_var != operand and operand not in dist_opr:
            dist_opr.append(operand)
            temp_var = operand
            
    return dist_opr

if __name__ == "__main__":
    print(get_operands("AB + CD + CD"))