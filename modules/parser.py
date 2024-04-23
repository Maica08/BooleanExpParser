from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import to_cnf

# Define boolean variables
A, B, C = symbols('A B C')

my_list = [
    "A | 1",         # annulment
    "A&0",           # annulment
    "A | 0",         # identity
    "A&1",           # identity
    "A | A",         # idempotent
    "A&A",           # idempotent
    " A | ~A",      # complement
    "A&(~A)",        # complement
    "~~A",           # double negation
    "~(~A)",         # double negation
    "(A | B) | C",   # associativity
    "(A&B)&C",       # associativity
    "A | B",         # commutative
    "A&B",           # commutative
    "A | (A&B)",     # absorptive
    "A&(A | B)",     # absorptive
    "~(A&B)",        # de morgans
    "~(A | B)",      # de morgans
    "(A | B)&(A | C)",
    "~A"   
]

for i, expression in enumerate(my_list):
    # Preprocess the expression to replace 0 and 1 with appropriate boolean variables
    expression = expression.replace('0', 'False').replace('1', 'True')
    # Parse the expression using eval to handle boolean variables
    res = eval(expression)
    # Convert the result to Conjunctive Normal Form (CNF) for better simplification
    res_cnf = to_cnf(res)
    print(f"{i+1}. {expression}\n\t{res_cnf}")
