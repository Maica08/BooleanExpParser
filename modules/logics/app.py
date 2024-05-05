from .tabular_method import *
from .truth_tables import final_table, initial_table
from typing import List, Dict

class App:
    def __init__(self, bool_exp: str) -> None:
        self.bool_exp = bool_exp
        
    def evaluate_exp(self) -> str:
        char_set = [exp.strip() for exp in self.bool_exp]
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
                        indexes.append(index + 1)
        
        for i, index in enumerate(indexes):
            char_set.insert(index + i, '*')
                            
        result = ''.join([str(char) for char in char_set])
        self.bool_exp = result
        return self.bool_exp
        
    def generate_result(self) -> str:
        self.evaluate_exp()
        operands = get_identifiers(expression=self.bool_exp)
        init_table = initial_table(identifiers=operands)
        table = final_table(init_table=init_table, bool_exp=self.bool_exp)
        
        last_column = table[self.bool_exp]
        if all(x == 0 for x in last_column):
            result = '0'
        elif all(x == 1 for x in last_column):
            result = '1'
        
        else:
        
            sop = sum_of_prod(bool_exp=self.bool_exp)
            init_match = initial_match(sop=sop)
            final_match = get_final_match(init_match=init_match)
            
            result = get_minimize_exp(final_match=final_match)
            
        return result
    
if __name__ == "__main__":
    exp = "A(B + C)"
    exp = App(exp)
    print(exp.generate_result())