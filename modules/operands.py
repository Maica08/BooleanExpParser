from typing import List

operators = ['-', '.', '+']
delimiter = ['(', ')', ' ']
symbols = operators + delimiter

def get_operands(expression: str | List) -> List:
    operands = []
    # dist_opr = []

    for e in expression:
        if e not in symbols:
            if expression.index(e) != 0 and expression[expression.index(e) - 1] == '-':
                add_opr = f"-{e}"
            elif expression.index(e) != 0 and expression[expression.index(e) - 1] != '-':
                add_opr = e
            elif expression.index(e) == 0:
                add_opr = e
                
            operands.append(add_opr)
            
    # temp_var = operands[0]
    # for operand in operands:
    #     if temp_var !=
    # print(operands)

    # dist_opr.append(operands[0])      
    # for operand in operands:
    #     temp_var = operands[0]    
    #     if temp_var != operand and operand not in dist_opr:
    #         dist_opr.append(operand)
    #         temp_var = operand
            
    return operands

if __name__ == "__main__":
    print(get_operands("-AAA"))