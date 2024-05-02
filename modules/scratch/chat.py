from typing import Dict

operators = {'+': 3, '*': 2, '!': 1}

def precedence(expression: str) -> Dict:
    def find_operator(exp: str, start: int, end: int) -> int:
        parenthesis_count = 0
        min_precedence = float('inf')
        min_precedence_index = -1
        
        for i in range(start, end):
            if exp[i] == '(':
                parenthesis_count += 1
            elif exp[i] == ')':
                parenthesis_count -= 1
            elif exp[i] in operators and parenthesis_count == 0:
                if operators[exp[i]] < min_precedence:
                    min_precedence = operators[exp[i]]
                    min_precedence_index = i
        
        return min_precedence_index
    
    exp = expression.strip()
    
    if exp[0] == '(' and exp[-1] == ')':
        exp = exp[1:-1]
        
    operator_index = find_operator(exp, 0, len(exp))
    
    if operator_index == -1:
        return exp
    
    operator_char = exp[operator_index]
    left_expr = precedence(exp[:operator_index].strip())
    right_expr = precedence(exp[operator_index+1:].strip())
    
    return {operator_char: [left_expr, right_expr]}

if __name__ == "__main__":
    a = "(A + C) * (B + C)"
    print(precedence(a))
