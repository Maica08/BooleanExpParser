from .truth_tables import *
from typing import List, Dict

def sum_of_prod(bool_exp: str) -> Dict:
    init_table = initial_table(get_identifiers(expression=bool_exp))
    truth_table = final_table(init_table=init_table, bool_exp=bool_exp)
    
    min_terms = [i for i in range(len((truth_table[bool_exp]))) if truth_table[bool_exp][i] == 1]
    mt_values = []
    for i in min_terms:
        temp = []
        for value in init_table.values():
            temp.append(value[i])
        mt_values.append(temp)
        
    sop = {str(min_terms[i]): mt_values[i] for i in range(len(min_terms))}
    
    return sop

def initial_match(sop: Dict) -> List[List[Dict]]:
    # group the minterms first according to the number of ones they have
    # sop = {idx: [truth values]}
    ones_num = []
    for value in sop.values():
        cur_1_count = value.count(1)
        if cur_1_count not in ones_num:
            ones_num.append(cur_1_count)
            
    ones_num.sort()
            
    init_group = {num: [] for num in ones_num}
    for key, value in sop.items():
        init_group[(value.count(1))].append({key: value})
        
    init_groupings = list(init_group.values())

    return init_groupings
    
def get_matches(init_match: List) -> List[List[Dict]]:
    result = []
    
    i = 0
    j = i + 1
    
    while i in range(len(init_match) - 1):
        temp = []
        for val1 in init_match[i]:
            for val2 in init_match[j]:
        
                list1 = list(val1.values())[0]
                list2 = list(val2.values())[0]
                key1 = list(val1.keys())[0]
                key2 = list(val2.keys())[0]
                
                unmatched_count = 0
                unmatched_idx = None
                for index, (elem1, elem2) in enumerate(zip(list1, list2)):
                    if elem1 != elem2:
                        unmatched_count += 1
                        unmatched_idx = index
                                         
                if unmatched_count == 1:
                    new_key = '-'.join(str(i) for i in [key1, key2])
                    new_val = list1.copy()
                    new_val[unmatched_idx] = "_"
                                    
                    temp.append({new_key: new_val})
                    
        if temp:       
            result.append(temp)
                    
        i += 1
        j += 1
    
    if not result:
        return init_match
    
    return result

def get_final_match(init_match: List) -> List[List[Dict]]:
    first = get_matches(init_match=init_match)
    second = get_matches(init_match=first)
    
    if first == second:
        return second
    
    else:
        return get_final_match(init_match=second)
    
def get_minimize_exp(final_match: List[List[Dict]]) -> str:
    f_match = []
    for match in final_match:
        f_match.extend(match)
        
    prime_implicants = []
    keys = []
    for match in f_match:
        for key, value in match.items():
            new_key = []
            for i in range(len(value)):
                if value[i] == 1:
                    new_key.append(chr(96 + i + 1).upper())
                elif value[i] == 0:
                    new_key.append("!" + chr(96 + i + 1).upper())
                    
            new_key = ''.join(new_key)
            new_value = key.split('-')
            keys.append(new_key)
            
            if keys.count(new_key) <= 1:
                prime_implicants.append({new_key: new_value})
                
    exp = []
    implicants = []
    
    for implicant in prime_implicants:
        implicants += list(implicant.values())[0]
        
    set_of_mt = list(set(implicants))
    mt_count = {mt: implicants.count(mt) for mt in set_of_mt}
    
    for mt, count in mt_count.items():
        if count == 1:
            for implicant in prime_implicants:
                for key, value in implicant.items():
                    if mt in value and key not in exp:
                        exp.append(key)
    
    final_exp = ' + '.join(exp)
    
    return final_exp

    
if __name__ == "__main__":
    expr = "A"
    sop = sum_of_prod(bool_exp=expr)    
    init_mp = initial_match(sop=sop)
    new_mp = get_final_match(init_match=init_mp)
    f_match = get_minimize_exp(new_mp)