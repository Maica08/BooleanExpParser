from typing import List, Dict
from .tokens import Tokenizer


operators = ['+', '*', '!']
delimiters = ['(', ')', ' ']
non_operands = operators + delimiters

def get_identifiers(expression: str) -> List[str]:
    """
    Gets identifiers in an expression for table construction
    
    Args:
        expression (str): boolean expression

    Returns:
        List[str]: variabels/identifiers for initial table
    """
    identifiers = []
    operands = []
    
    for char in expression:
        if char not in non_operands and char.isalpha():
            operands.append(char)
            
    for operand in operands:
        for char in operand:
            if char not in identifiers:
                identifiers.append(char)
    
    identifiers.sort()
    return identifiers

def initial_table(identifiers: List[str]) -> Dict:
    """
    Constructs initial table with identifiers
    Args:
        identifiers (List[str]): identifiers in an expression

    Returns:
        Dict: initial table
    """
    n_rows =  2 ** len(identifiers)
    columns = {identifier: [] for identifier in identifiers}
    
    alternate_count = int(n_rows / 2)
    switch_count = int(n_rows / alternate_count)
    loop = 0
    for key in columns:
        while loop in range(switch_count):
            for count in range(alternate_count):
                if loop % 2 == 0:
                    columns[key] += [0]
                else:
                    columns[key] += [1]
            
            loop += 1
            
        alternate_count //= 2
        if alternate_count >= 1:
            switch_count *= 2
        else:
            switch_count = 0
        loop = 0
            
    return columns


def tree_height(tokenized_expression:str) -> int:
    if isinstance(tokenized_expression, dict):
        max_height = 0
        for value in tokenized_expression.values():
            if isinstance(value, list):
                height = 1 + max(tree_height(operand) for operand in value)
            else:
                height = 1 + tree_height(value)
            max_height = max(max_height, height)
        return max_height
    else:
        return 0
    
def get_innermost_dicts(tokenized_expression: Dict, current_height: int, max_height: int) -> List[Dict]:
    if isinstance(tokenized_expression, dict):
        if current_height == max_height:
            return [tokenized_expression]
        innermost_dicts = []
        for value in tokenized_expression.values():
            if isinstance(value, list):
                for operand in value:
                    innermost_dicts.extend(get_innermost_dicts(operand, current_height + 1, max_height))
            elif isinstance(value, dict):
                innermost_dicts.extend(get_innermost_dicts(value, current_height + 1, max_height))
        return innermost_dicts
    else:
        return []


def perform_operation(innermost_dicts: List[Dict] | List[int], initial_table: Dict) -> List[List[int]]:
    new_bool_val = []

    for i in range(len(innermost_dicts)):
        bool_val = []
        for key, value in innermost_dicts[i].items():
            if key == '+':
                # if value is a list containing operands
                if str(value[0]).isalpha() and str(value[1]).isalpha():
                    bool_val = [a or b for a, b in zip(initial_table[value[0]], initial_table[value[1]])]
                    # print(bool_val)
                # if value[0] is an operand and value[1] is a list containing 1's and 0's
                elif str(value[0]).isalpha() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a or b for a, b in zip(initial_table[value[0]], value[1])]
                # if value[1] is an operand and value[0] is a list containing 1's and 0's
                elif str(value[1]).isalpha() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a or b for a, b in zip(value[0], initial_table[value[1]])]
                # if value contains a list of lists of 1's and 0's
                elif all(isinstance(val, list) for val in value):
                    bool_val = [a or b for a, b in zip(value[0], value[1])]
                    
            elif key == '*':
                if str(value[0]).isalpha() and str(value[1]).isalpha():
                    bool_val = [a and b for a, b in zip(initial_table[value[0]], initial_table[value[1]])]
                elif str(value[0]).isalpha() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a and b for a, b in zip(initial_table[value[0]], value[1])]
                elif str(value[1]).isalpha() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a and b for a, b in zip(value[0], initial_table[value[1]])]
                elif all(isinstance(val, list) for val in value):
                    bool_val = [a and b for a, b in zip(value[0], value[1])]

            elif key == '!':
                if str(value[0]).isalpha():
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in initial_table[value[0]]]]
                elif all(isinstance(val, list) for val in value):
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in value[0]]]

        new_bool_val.append(bool_val)
        
    return new_bool_val


def loop_through(tokenized_expression: Dict, max_height: int, bool_value: List[List[int]], current_height: int = 1) -> Dict | List[int]:
    if isinstance(tokenized_expression, dict):
        if current_height == max_height:
            return bool_value.pop(0)
        new_expr = {}
        for key, value in tokenized_expression.items():
            if isinstance(value, list):
                new_expr[key] = [loop_through(sub_expr, max_height, bool_value, current_height + 1) if isinstance(sub_expr, dict) else sub_expr for sub_expr in value]
            elif isinstance(value, dict):
                new_expr[key] = loop_through(value, max_height, bool_value, current_height + 1)
        return new_expr
    else:
        return tokenized_expression

def last_column(tokenized_expression: dict, expression: str) -> List[int]:
    cur_max_height = tree_height(tokenized_expression=tokenized_expression)
    current_dicts = get_innermost_dicts(tokenized_expression=tokenized_expression, current_height=1, max_height=cur_max_height)
    init_table = initial_table(identifiers=get_identifiers(expression=expression))
    bool_val = perform_operation(innermost_dicts=current_dicts, initial_table=init_table)
    cur_expression = loop_through(tokenized_expression=tokenized_expression, max_height=cur_max_height, bool_value=bool_val) 
    
    if cur_max_height > 1:
        return last_column(tokenized_expression=cur_expression, expression=expression)
    
    elif cur_max_height == 1 and isinstance(cur_expression, list):
        return cur_expression


def final_table(init_table: Dict, bool_exp: str) -> Dict:
    final_table = {key: value for key, value in init_table.items()}
    if len(bool_exp) > 1:
        final_table[bool_exp] = last_column(tokenized_expression=Tokenizer.precedence(bool_exp), expression=bool_exp)
    
    return final_table
        

if __name__ == "__main__":
    # print(initial_table(['A', 'B', 'C']))
    # t_expr = {'+': [{'*': ['A', 'B']}, {'*': ['A', {'+': ['C', 'D']}]}]}
    # expr = "A*B + (A*(C + D))"
    # print(last_column(tokenized_expression=t_expr, expression=expr)) 
    
    expr = "A"
    table = initial_table(get_identifiers(expr))
    res = final_table(table, expr)
    
    print(res)
    
    # exp = "A + 1"
    # print(get_identifiers(exp))