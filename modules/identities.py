from operands import *
from typing import List

IDENTITY_LAWS = {
    "annulment": 1,
    "identity": 2,
    "idempotent": 3,
    "complement": 4,
    "double negation": 5,
    "associative": 6,
    "distributive": 7,
    "commutative": 8,
    "absorptive": 9,
    "adsorption": 10,
    "de morgan's": 11,
    "consensus": 12
}

def adjoined_operands(exp: str) -> str:
    used_laws = []
    res_exp = exp
    
    # annulment
    if '0' in exp:
        final_exp = 0
        used_laws.append(1)
        
        return final_exp
    
    # identity
    if '1' in exp:
        res_exp = []
        for e in exp:
            if e != '1':
                res_exp.append(e)
        used_laws.append(2)
    
    # idempotent
    simplify_exp = get_operands(res_exp)
    final_exp = ''.join(sorted(simplify_exp))
    if len(res_exp) != len(simplify_exp):
        used_laws.append(3)
        
    return final_exp
    
if __name__ == "__main__":    
    print(adjoined_operands('A11111ACCAA11111BBBB1C'))
        