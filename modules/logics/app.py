from .tabular_method import *
from .truth_tables import final_table, initial_table, get_identifiers
from .tokenizer import Tokenize
from typing import List, Dict
import os

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
        
        try:
            tokenize = Tokenize(self.bool_exp).tokenize()
        except ValueError:
            return "Invalid expression"
        else:
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
                final_match = get_final_match(init_match=init_match, exemption=[])
                
                result = get_minimize_exp(final_match=final_match, operands=operands)
                
            return result
    
def main() -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        prompt = input("Enter the boolean expression: ")
        result = App(bool_exp=prompt)
        print(f"Result: {result.generate_result()}")
        print()
        
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
            break
        
def alt_main() -> None:
    expressions = [
        "A0", "A1", "A + 0", "A + A", "AA", "A + !A", "!(AB)", "!(A + B)", "A + AB", "A(A+B)", "A + !AB", "A(!A + B)", "!(!A)", "A(B+C)",
        "AB + B!C  + AC", "A!B + BC + AC", "(A + B)(!A + C)(B + C)", "(A + B)(!B + C)(A + C)", "!A!B + A!C + !B!C", 
        "A((A + !A) + !B)", "AB + A(B + C) + B(B + C)", "!(!A(B + C))", "(A + !B + !C)(A + !B + C)(A + B + !C)"     
    ]
    
    for i in range(len(expressions)):
        print(f"{i + 1}. {expressions[i]}")
        result = App(bool_exp=expressions[i])
        print(f"Result: {result.generate_result()}")
        result = None
        print()

if __name__ == "__main__":
    alt_main()
