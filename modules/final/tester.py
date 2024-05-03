from truth_tables import get_identifiers, initial_table
from typing import List, Dict

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

# expression = {'+': [{'*': ['A', 'B']}, {'*': ['A', 'C']}]}

expression = {'+': [{'*': ['A', 'B']}, {'*': ['A', {'+': ['C', 'D']}]}]}
height = tree_height(expression)
innermost_dicts = get_innermost_dicts(expression, 1, height)
# expr = '(A * B) + (A * C)'
expr = "A*B + (A*(C + D))"
# expression = {'+': [[1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0]]}
# height = tree_height(expression)
# innermost_dicts = get_innermost_dicts(expression, 1, height)

# print(innermost_dicts)
# print(height)


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
                if str(value[0]).isalpha() and str(value[1]).isalpha():
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in initial_table[value[0]]]]
                elif all(isinstance(val, list) for val in value):
                    bool_val = [1 if a else 0 for a in [not bool(x) for x in value[0]]]

        new_bool_val.append(bool_val)
        
    return new_bool_val

# new_bool_val = perform_operation(innermost_dicts, initial_table(get_identifiers(expr)))
# print(new_bool_val)


def loop_through(tokenized_expression: Dict, max_height: int, bool_value: List[List[int]], current_height: int = 1) -> Dict | List[int]:
    if isinstance(tokenized_expression, dict):
        if current_height == max_height:
            # Replace innermost dictionary with boolean value
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
    # for value in tokenized_expression.values():
    #     count = 0
    #     for val in value:
    #         cur_height = 1
    #         if isinstance(val, dict):
    #             cur_height += 1
    #             if cur_height != height:
    #                 loop_through(val, height, bool_value)
    #             elif cur_height == height:
    #                 value[value.index(val)] = bool_value[count]
    #                 count += 1
    #         elif height == 1:
    #             return bool_value[count]
    #         elif isinstance(val, str):
    #             break
            
    #         print(cur_height, height, val, len(val))
            
    # return tokenized_expression

# print(f"Bool value: {new_bool_val}")
            
# print(loop_through(expression, height, new_bool_val))

def last_column(tokenized_expression: dict, expression: str) -> List[int]:
    cur_max_height = tree_height(tokenized_expression=tokenized_expression)
    current_dicts = get_innermost_dicts(tokenized_expression=tokenized_expression, current_height=1, max_height=cur_max_height)
    init_table = initial_table(identifiers=get_identifiers(expression=expression))
    bool_val = perform_operation(innermost_dicts=current_dicts, initial_table=init_table)
    cur_expression = loop_through(tokenized_expression=tokenized_expression, max_height=cur_max_height, bool_value=bool_val) 
    
    print(cur_max_height)
    print(current_dicts)
    print(bool_val)
    print(cur_expression)
    
    if cur_max_height > 1:
        return last_column(tokenized_expression=cur_expression, expression=expression)
    
    elif cur_max_height == 1 and isinstance(cur_expression, list):
        return cur_expression
    
t_expr = {'+': [{'*': ['A', 'B']}, {'*': ['A', {'+': ['C', 'D']}]}]}
expr = "A*B + (A*(C + D))"
print(last_column(tokenized_expression=t_expr, expression=expr)) 
    

"""
algo for getting final column boolean values

functions:
tree_height
get_innermost_dicts
perform_operation
loop_through


need to do:
recurse, combine all
"""