from sympy.logic import simplify_logic
from sympy.abc import *

class Minimize:
    def __init__(self, expression: str):
        self.expression = expression
        
    def evaluate(self) -> str:
        char_set = [exp.strip() for exp in self.expression]
        for char in char_set:
            if not char:
                char_set.remove(char)
        
        indexes = []
        
        for index in range(len(char_set)):
            if index != len(char_set) - 1:
                if char_set[index] == ")" and (char_set[index + 1].isalpha() or char_set[index + 1] == "(" or char_set[index + 1].isnumeric()):
                    indexes.append(index + 1)
                elif char_set[index] != ")":
                    if (char_set[index].isalpha() or char_set[index].isnumeric()) and (char_set[index + 1].isalpha() or char_set[index + 1] == "(" or char_set[index + 1] == "!" or char_set[index + 1].isnumeric()):
                        print(True)
                        indexes.append(index + 1)
        
        for i, index in enumerate(indexes):
            char_set.insert(index + i, '*')
                            
        result = ''.join([str(char) for char in char_set])
        self.expression = result
        return self.expression
        
    def translate_expression(self):
        self.evaluate()
        self.expression = self.expression.replace('*', '&')
        self.expression = self.expression.replace('+', '|')
        self.expression = self.expression.replace('!', '~')
        self.expression = self.expression.replace('1', 'True')
        self.expression = self.expression.replace('0', 'False')
        
        return self.expression
    
    # @staticmethod
    def retranslate_expression(self, bool_exp:str):
        bool_exp = str(bool_exp)
        bool_exp = bool_exp.replace(' & ', '')
        bool_exp = bool_exp.replace('|', '+')
        bool_exp = bool_exp.replace('~', '!')
        bool_exp = bool_exp.replace('True', '1')
        bool_exp = bool_exp.replace('False', '0')

        
                
        return bool_exp
        
    def minimize_expression(self) -> str:
        input_exp = self.translate_expression()
        result = simplify_logic(input_exp)
        
        if result == True:
            result = "1"
        elif result == False:
            result = "0"
        
        result = self.retranslate_expression(result)
        
        return result
        

def evaluate(expression: str) -> str:
    char_set = [exp.strip() for exp in expression]
    for char in char_set:
        if not char:
            char_set.remove(char)
    
    indexes = []
    
    for index in range(len(char_set)):
        if index != len(char_set) - 1:
            if char_set[index] == ")" and (char_set[index + 1].isalpha() or char_set[index + 1] == "("):
                indexes.append(index + 1)
            elif char_set[index] != ")":
                if char_set[index].isalpha() and (char_set[index + 1].isalpha() or char_set[index + 1] == "(" or char_set[index + 1] == "!"):
                    indexes.append(index + 1)
                        
    for i, index in enumerate(indexes):
        char_set.insert(index + i, '*')
                
    result = ''.join([str(char) for char in char_set])
    return result

if __name__ == "__main__":
    print(simplify_logic(True & A))  
