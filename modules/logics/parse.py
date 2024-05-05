from typing import List, Dict, Any

class Precedence_Tree:
    operators = {'+': 3, '*': 2, '!': 1}
    delimiter = ['(', ')']

    @staticmethod
    def precedence(expression: str) -> Dict:
        """
        Determines the expression's precedence
        Args:
            expression (str): boolean expression

        Returns:
            Dict: contains a list that may contain nested lists and dictionaries
        """
        result = {}
        
        # initial test
        exp = expression.strip()
        if "(" in exp:
            if exp[0] == '(' and exp[-1] == ')':
                if exp.count('(') == 1 and exp.count(')') == 1 and exp.index('(') == 0 and exp.rindex(')') == len(exp) - 1:
                    exp = exp[1:-1]
            
        # check if there is parenthesis
        parenthesis_count = 0
        # base
        max_weight = 0
        current_operator = None
        current_operator_index = None
        
        # counter
        i = 0      
        while i in range(len(exp)):
            if exp[i] ==  '(':
                parenthesis_count += 1
            elif exp[i] == ')':
                parenthesis_count -= 1
            elif exp[i] in Precedence_Tree.operators and parenthesis_count == 0:
                if Precedence_Tree.operators[exp[i]] > max_weight:
                    max_weight = Precedence_Tree.operators[exp[i]]
                    current_operator = exp[i]
                    current_operator_index = i
            
            i += 1         
                    
        if not current_operator:
            if "(" in exp:
                if exp[0] == '(' and exp[-1] == ')':
                    exp = exp[1:-1]
                    
                    i = 0      
                    while i in range(len(exp)):
                        if exp[i] ==  '(':
                            parenthesis_count += 1
                        elif exp[i] == ')':
                            parenthesis_count -= 1
                        elif exp[i] in Precedence_Tree.operators and parenthesis_count == 0:
                            if Precedence_Tree.operators[exp[i]] > max_weight:
                                max_weight = Precedence_Tree.operators[exp[i]]
                                current_operator = exp[i]
                                current_operator_index = i
                    
                        i += 1
            else:
                return exp
            
        if current_operator == '!':
            operand = exp[current_operator_index + 1:].strip()
            result[current_operator] = [Precedence_Tree.precedence(operand)]
            
        else:
            left_exp = exp[:current_operator_index].strip()
            right_exp = exp[current_operator_index + 1:].strip()
        
            result[current_operator] = [Precedence_Tree.precedence(left_exp), Precedence_Tree.precedence(right_exp)]
            
        return result


if __name__ == "__main__":
    a = "(A + B) * (A + C)"
    print(Precedence_Tree.precedence(a))
    
