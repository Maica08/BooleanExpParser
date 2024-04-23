from typing import List, Dict


operators = ['+', '*', '!']
delimiters = ['(', ')', ' ']
non_operands = operators + delimiters

def get_identifiers(expression: str) -> str:
    identifiers = []
    operands = []
    
    for char in expression:
        if char not in non_operands:
            operands.append(char)
            
    for operand in operands:
        for char in operand:
            if char not in identifiers:
                identifiers.append(char)
    
    identifiers.sort()
    return identifiers

def initial_table(identifiers: List) -> Dict:
    n_rows =  2 ** len(identifiers)
    columns = {identifier: [] for identifier in identifiers}
    
    alternate_count = int(n_rows / 2)
    switch_count = int(n_rows / alternate_count)
    loop = 0
    for key in columns:
        while loop in range(switch_count):
            for count in range(alternate_count):
                if loop % 2 == 0:
                    columns[key] += [1]
                else:
                    columns[key] += [0]
            
            loop += 1
            
        alternate_count //= 2
        if alternate_count >= 1:
            switch_count *= 2
        else:
            switch_count = 0
        loop = 0
            
    return columns

def final_table(initial_table: List, bool_exp: List) -> Dict:
    # truth_table = initial_table
    # for expression in bool_exp:
    #     truth_table[expression] = []
        
    # start_column = len(initial_table) - 1
    # keys = bool_exp
    
    # for key in keys:
    
    pass
        
        

if __name__ == "__main__":
    print(initial_table(['A', 'B', 'C']))