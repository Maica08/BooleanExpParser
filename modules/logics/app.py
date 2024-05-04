from .tabular_method import *
from .backup.minimize import Minimize
from typing import List, Dict

class App:
    def __init__(self, bool_exp: str) -> None:
        self.bool_exp = bool_exp
        
    def evaluate_exp(self):
        exp = Minimize(self.bool_exp)
        self.bool_exp = exp.evaluate()
        return self.bool_exp
        
    def generate_result(self) -> str:
        self.evaluate_exp()
        sop = sum_of_prod(bool_exp=self.bool_exp)
        init_match = initial_match(sop=sop)
        final_match = get_final_match(init_match=init_match)
        
        if '1' in self.bool_exp or '0' in self.bool_exp:
            exp = self.bool_exp
            result = Minimize(exp).minimize_expression()
        
        else:
            result = get_minimize_exp(final_match=final_match)
               
            
        return result
    
if __name__ == "__main__":
    exp = "A + B"
    exp = App(exp)
    print(exp.generate_result())