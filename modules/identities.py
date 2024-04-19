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
    
    else:
        # idempotent
        temp_list = []
        for e in res_exp:
            if e in res_exp:
                if e not in temp_list and e[::-1] not in temp_list:
                    temp_list.append(e)
                
        final_exp = ' + '.join(temp_list)
        used_laws.append(3)
        
    return final_exp


def de_morgans(exp: str) -> str:
    used_laws = []
    if '+' in exp:
        temp_exp = [e.strip() for e in exp[2:-1].split('+')]
            
        for e in temp_exp:
            if len(e) > 1:
                temp_exp[temp_exp.index(e)] = f'-({e})'
            else:
                temp_exp[temp_exp.index(e)] = f'-{e}'
        final_exp = ''.join(temp_exp)
    
    else:
        temp_exp = [e for e in exp[2:-1]]
        print(temp_exp)
        for e in temp_exp:
            if e == '-':
                temp_exp[temp_exp.index(e) + 1] = e + temp_exp[temp_exp.index(e) + 1]
                temp_exp.remove(e)
        final_exp = ' + '.join(temp_exp)
    
    used_laws.append(11)    
    return final_exp        
                
def mixed_operands(exp: str) -> str:
    used_laws = []
    div = exp[:-1].split('(')
    left = div[0]
    right = [e.strip() for e in div[1].split('+')]
    
    if len(right) == 2 and len(left) == 1:                      # absorptive 
        for e in right:
            if '-' not in e and len(e) == 1:
                if e == left:
                    final_exp = left
                    used_laws.append(9)
                    
            elif left[0] in e and '-' in e:                     # adsorption
                right.remove(e)
                final_exp = f'{left[0]}{right[0]}'
                used_laws.append(10)

                
    elif len(left) == 2 and len(right) == 2 and '-' in left:    
        for e in right:
            if e in left:
                if e != left:                                   # adsorption
                    right.remove(e)
                    final_exp = f'{left}{right[0]}'
                    used_laws.append(10)
                
                elif e == left:                                 # absorptive
                    final_exp = left
                    
    else:
        int_exp = [left + e for e in right]                     # distributive (expanded)
        final_exp = (' + ').join(int_exp)
        used_laws.append(7)
        
    return final_exp

def extracted_distribution(exp: str) -> str:                    # distributive (extracted)
    used_laws = []
    common_opr = {}
    opr = [e.strip() for e in exp.split('+')]
    for e in opr:
        for i in range(opr.index(e), len(opr)):
            if opr.index(e) == i:
                pass
            else:
                common = list(set(e).intersection(set(opr[i])))
                print(f"e: {e}, common: {common}")
                if common:
                    if common[0] not in common_opr:
                        common_opr[common[0]] = 0
                    else:
                        common_opr[common[0]] += 1         
    
    max_value = max([n for n in common_opr.values()])
    max_keys = [key for key in common_opr if common_opr[key] == max_value]
    
    is_all_same = all(map(lambda x: x == list(common_opr.values())[0], common_opr.values()))
    
    if not is_all_same:
        if len(max_keys) > 1:
            for key in max_keys:
                for e in opr:
                    if key == e:
                        max_key = e
        else:
            max_key = max_keys[0]
            
        distributed_ops = []
        undistributed = []
        if max_key:
            for op in opr:
                if max_keys[0] in op:
                    if max_keys[0] == op:
                        x = '1'
                    else:
                        x = op.replace(max_keys[0], '')
                    distributed_ops.append(x)
                else:
                    undistributed.append(op)
                        
        new_exp = f'{max_keys[0]}({' + '.join(distributed_ops)})'
        if len(undistributed) != 0:
            final_exp = f'{new_exp} + {' + '.join(undistributed)}'
        else:
            final_exp = new_exp
        used_laws.append(7)
    
    else:
        final_exp = exp
        
    return final_exp
        
                
        
def helper(exp):
    # double negation
    if exp[0] == '-' and exp[0] == exp[1]:
        f_exp = exp.replace('-', '')

if __name__ == "__main__":    
    # print(extracted_distribution('AB + AC + A'))
    print(disjunction_operands("AB + AB + BA + CD"))
        