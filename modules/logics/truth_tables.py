from typing import List, Dict
from parse import Precedence_Tree


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


def tree_height(parsed_expression: Dict) -> int:
    """
    Gets the tree height of the parsed_expression
    for later use in finding innermost dicts

    Args:
        parsed_expression (Dict): expression parsed with determined precedence

    Returns:
        int: height of the parsed expression
    """
    if isinstance(parsed_expression, dict):
        max_height = 0
        for value in parsed_expression.values():
            if isinstance(value, list):
                height = 1 + max(tree_height(operand) for operand in value)
            else:
                height = 1 + tree_height(value)
            max_height = max(max_height, height)
        return max_height
    else:
        return 0
    
def get_innermost_dicts(parsed_expression: Dict, current_height: int, max_height: int) -> List[Dict]:
    """
    Gets the innermost dict/s or the operands that needed to get the truth values first

    Args:
        parsed_expression (Dict): expression parsed with determined precedence
        current_height (int): curren height in the tree or the starting height
        max_height (int): the height of the parsed expression

    Returns:
        List[Dict]: list of the innermost dict/s
    """
    if isinstance(parsed_expression, dict):
        if current_height == max_height:
            return [parsed_expression]
        innermost_dicts = []
        for value in parsed_expression.values():
            if isinstance(value, list):
                for operand in value:
                    innermost_dicts.extend(get_innermost_dicts(operand, current_height + 1, max_height))
            elif isinstance(value, dict):
                innermost_dicts.extend(get_innermost_dicts(value, current_height + 1, max_height))
        return innermost_dicts
    else:
        return []


def perform_operation(innermost_dicts: List[Dict] | List[int], initial_table: Dict) -> List[List[int]]:
    """
    Gets the truth values of the expression to in the innermost dicts through performing operations

    Args:
        innermost_dicts (List[Dict] | List[int]): list that contains the innermost dict/s
        initial_table (Dict): initial truth table that contains the identifiers only

    Returns:
        List[List[int]]: list of truth values for each innermost dict
    """
    new_bool_val = []

    for i in range(len(innermost_dicts)):
        bool_val = []
        for key, value in innermost_dicts[i].items():
            if key == '+':
                # if value is a list containing operands
                if str(value[0]).isalpha() and str(value[1]).isalpha():
                    bool_val = [a or b for a, b in zip(initial_table[value[0]], initial_table[value[1]])]
                # if value[0] is an operand and value[1] is a list containing 1's and 0's
                elif str(value[0]).isalpha() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a or b for a, b in zip(initial_table[value[0]], value[1])]
                # if value[1] is an operand and value[0] is a list containing 1's and 0's
                elif str(value[1]).isalpha() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a or b for a, b in zip(value[0], initial_table[value[1]])]
                # if value contains a list of lists of 1's and 0's
                elif all(isinstance(val, list) for val in value):
                    bool_val = [a or b for a, b in zip(value[0], value[1])]
                
                # involves numerical operand
                elif str(value[0]).isnumeric() and str(value[1]).isnumeric():
                    bool_val = [a or b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], [int(value[1]) for i in range(len(list(initial_table.values())[0]))])]
                elif str(value[0]).isnumeric() and str(value[1]).isalpha():
                    bool_val = [a or b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], initial_table[value[1]])]
                elif str(value[1]).isnumeric() and str(value[0]).isalpha():
                    bool_val = [a or b for a, b in zip([int(value[1]) for i in range(len(list(initial_table.values())[0]))], initial_table[value[0]])]
                elif str(value[0]).isnumeric() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a or b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], value[1])]
                elif str(value[1]).isnumeric() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a or b for a, b in zip([int(value[1]) for i in range(len(list(initial_table.values())[0]))], value[0])]
                    
            elif key == '*':
                if str(value[0]).isalpha() and str(value[1]).isalpha():
                    bool_val = [a and b for a, b in zip(initial_table[value[0]], initial_table[value[1]])]
                elif str(value[0]).isalpha() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a and b for a, b in zip(initial_table[value[0]], value[1])]
                elif str(value[1]).isalpha() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a and b for a, b in zip(value[0], initial_table[value[1]])]
                elif all(isinstance(val, list) for val in value):
                    bool_val = [a and b for a, b in zip(value[0], value[1])]
                
                elif str(value[0]).isnumeric() and str(value[1]).isnumeric():
                    bool_val = [a and b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], [int(value[1]) for i in range(len(list(initial_table.values())[0]))])]
                elif str(value[0]).isnumeric() and str(value[1]).isalpha():
                    bool_val = [a and b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], initial_table[value[1]])]
                elif str(value[1]).isnumeric() and str(value[0]).isalpha():
                    bool_val = [a and b for a, b in zip([int(value[1]) for i in range(len(list(initial_table.values())[0]))], initial_table[value[0]])]
                elif str(value[0]).isnumeric() and all(isinstance(elem, int) for elem in value[1]):
                    bool_val = [a and b for a, b in zip([int(value[0]) for i in range(len(list(initial_table.values())[0]))], value[1])]
                elif str(value[1]).isnumeric() and all(isinstance(elem, int) for elem in value[0]):
                    bool_val = [a and b for a, b in zip([int(value[1]) for i in range(len(list(initial_table.values())[0]))], value[0])]

            elif key == '!':
                if str(value[0]).isalpha():
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in initial_table[value[0]]]]
                elif all(isinstance(val, list) for val in value):
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in value[0]]]
                elif str(value[0]).isnumeric():
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in [int(value[0]) for i in range(len(list(initial_table.values())[0]))]]]

        new_bool_val.append(bool_val)
        
    return new_bool_val


def sub_through(parsed_expression: Dict, max_height: int, bool_value: List[List[int]], current_height: int = 1) -> Dict | List[int]:
    """
    Recursive function that substitutes boolean values to the innermost expressions

    Args:
        parsed_expression (Dict): parsed expression in terms of precedence
        max_height (int): height of the parsed expression
        bool_value (List[List[int]]): boolean values for the innermost expression/s
        current_height (int, optional): Defaults to 1; starting height

    Returns:
        Dict | List[int]: The parsed expression with the replaced boolean value
    """
    if isinstance(parsed_expression, dict):
        if current_height == max_height:
            return bool_value.pop(0)
        new_expr = {}
        for key, value in parsed_expression.items():
            if isinstance(value, list):
                new_expr[key] = [sub_through(sub_expr, max_height, bool_value, current_height + 1) if isinstance(sub_expr, dict) else sub_expr for sub_expr in value]
            elif isinstance(value, dict):
                new_expr[key] = sub_through(value, max_height, bool_value, current_height + 1)
        return new_expr
    else:
        return parsed_expression

def last_column(parsed_expression: dict, expression: str) -> List[int]:
    """
    Gets the final truth values for the boolean expression

    Args:
        parsed_expression (dict): parsed expression in terms of precedence
        expression (str): boolean expression

    Returns:
        List[int]: truth values for the expression
    """
    cur_max_height = tree_height(parsed_expression=parsed_expression)
    current_dicts = get_innermost_dicts(parsed_expression=parsed_expression, current_height=1, max_height=cur_max_height)
    init_table = initial_table(identifiers=get_identifiers(expression=expression))
    bool_val = perform_operation(innermost_dicts=current_dicts, initial_table=init_table)
    cur_expression = sub_through(parsed_expression=parsed_expression, max_height=cur_max_height, bool_value=bool_val) 
    
    if cur_max_height > 1:
        return last_column(parsed_expression=cur_expression, expression=expression)
    
    elif cur_max_height == 1 and isinstance(cur_expression, list):
        return cur_expression


def final_table(init_table: Dict, bool_exp: str) -> Dict:
    """
    Combines the initial table to the expression and its truth values 
    to construct a final table

    Args:
        init_table (Dict): initial truth table that consists of the identifiers
        bool_exp (str): boolean expression

    Returns:
        Dict: final truth table
    """
    final_table = {key: value for key, value in init_table.items()}
    if len(bool_exp) > 1:
        final_table[bool_exp] = last_column(parsed_expression=Precedence_Tree.precedence(bool_exp), expression=bool_exp)
    
    return final_table
        

if __name__ == "__main__":
    expr = "(X + Y) * Z"
    table = initial_table(get_identifiers(expr))
    res = final_table(table, expr)
    
    print(res)
