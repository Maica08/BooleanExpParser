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
        
    simplify_exp = get_operands(res_exp)
    # complement
    for e in simplify_exp: 
        if '-' in e and e[1] in simplify_exp:
            final_exp = '0'
            used_laws.append(4)
            
            return final_exp
        
        # idempotent
        else:              
            final_exp = ''.join(sorted(simplify_exp))
            if len(res_exp) != len(simplify_exp):
                used_laws.append(3)
        
    return final_exp

def disjunction_operands(exp: str):
    used_laws = []
    res_exp = [e.strip() for e in exp.split('+')]
    # res_exp = sorted(res_exp, key=lambda x:len(x))
    print(res_exp)
    
    # annulment
    if '1' in res_exp:
        final_exp = '1'
        used_laws.append(1)
        return final_exp
    
    # identity
    elif '0' in res_exp:
        for e in res_exp:
            if '0' != e != '+':
                final_exp = e
        used_laws.append(2)
        return final_exp
    
    # idempotent
    if res_exp[0] == res_exp[-1]:
        final_exp = res_exp[0]
        used_laws.append(3)
        return final_exp
    
    
    # absorption & adsorption w/out parenthesis
    in_exp1 = [e for e in res_exp[0]]
    in_exp2 = [e for e in res_exp[-1]]
    exp1 = []
    exp2 = []
    
    for e in in_exp1:
        if e == '-':
            f = in_exp1.pop(in_exp1.index(e) + 1)
            exp1.append(e + f)
        else:
            exp1.append(e)
            
    for e in in_exp2:
        if e == '-':
            f = in_exp2.pop(in_exp2.index(e) + 1)
            exp2.append(e + f)
        else:
            exp2.append(e)
    
    if len(exp1) == 1 and len(exp2) == 2:
        if exp1[0] in exp2:
            final_exp = exp1[0]
            used_laws.append(9)
            return final_exp
        else:
            for e in exp2:
                if exp1[0][-1] in e:
                    exp2.remove(e)
            final_exp = f'{exp1[0]} + {exp2[0]}'
            used_laws.append(10)
            return final_exp
    
    elif len(exp1) == 2 and len(exp2) == 1:
        if exp2[0] in exp1:
            final_exp = exp2[0]
            used_laws.append(9)
            return final_exp
        else:
            for e in exp1:
                if exp2[0][-1] in e:
                    exp1.remove(e) 
            final_exp = f'{exp2[0]} + {exp1[0]}'
            return final_exp
            
    
if __name__ == "__main__":    
    print(disjunction_operands('-A + AB'))
        