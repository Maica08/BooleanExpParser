from .truth_tables import *
from typing import List, Dict

def sum_of_prod(bool_exp: str) -> Dict:
    """
    Gets the sum of products based on the generated truth table, 
    for later use in determining primary implicants

    Args:
        bool_exp (str): boolean expression

    Returns:
        Dict: min_terms with their corresponding truth values
    """
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
    """
    Gets the initial matching of min terms using the sum of products
    by grouping them first according to the number of 1's each of min term has

    Args:
        sop (Dict): sum of products

    Returns:
        List[List[Dict]]: initial matches of min terms
    """
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
    """
    Gets the matches of min terms depending on the changes
    that occur in their values

    Args:
        init_match (List): min terms initial match

    Returns:
        List[List[Dict]]: min terms match
    """
    result = []
    
    i = 0
    j = i + 1
        
    new_minterms = []
    
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
                    new_minterms.append(new_key)
                    
        if temp:       
            result.append(temp)
                    
        i += 1
        j += 1
    
    init_minterm = []
    for group in init_match:
        for dict in group:
            init_minterm.append(dict)
            
    unmatched_minterm = []
                        
    for minterm in init_minterm:
        count = 0
        for new_minterm in new_minterms:
            if list(minterm.keys())[0] in new_minterm:
                count += 1
                
        if count == 0:
            unmatched_minterm.append(minterm)
        
    if not result:
        return init_match, unmatched_minterm
    
    
    return result, unmatched_minterm

def get_final_match(init_match: List, exemption: List = []) -> List[List[Dict]]:
    """
    Recursive function that uses the get_matches function to
    arrive to the final match of min terms in order to determine
    the primary implicants

    Args:
        init_match (List): min terms initial match

    Returns:
        List[List[Dict]]: final match of min terms
    """
    
    first, init_exemption = get_matches(init_match=init_match)
    second, add_exemp = get_matches(init_match=first)
    
    exemption.append(add_exemp[0])
    
    if first == second:
        final_result = []
        for group in second:
            for term in group:
                final_result.append(term)
                
        final_result += exemption
        return final_result
    
    else:
        return get_final_match(init_match=second, exemption=exemption)
    
    
def get_minimize_exp(final_match: List[List[Dict]], operands: List) -> str:
    """
    Determines the significant primary implicants based on the 
    final match of min terms

    Args:
        final_match (List[List[Dict]]): final match of min terms

    Returns:
        str: simplified boolean expression
    """
    f_match = []
    for match in final_match:
        f_match.append(match)
                
    prime_implicants = []
    keys = []
    for match in f_match:
        for key, value in match.items():
            new_key = []
            for i in range(len(value)):
                if value[i] == 1:
                    new_key.append(operands[i])
                elif value[i] == 0:
                    new_key.append("!" + operands[i])
                    
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
    expr = "(A + !B + !C)*(A + !B + C)*(A + B + !C)"
    operands = get_identifiers(expression=expr)
    sop = sum_of_prod(bool_exp=expr)    
    init_mp = initial_match(sop=sop)
    new_mp = get_final_match(init_match=init_mp)
    f_match = get_minimize_exp(new_mp, operands)
    
    print(f_match)
