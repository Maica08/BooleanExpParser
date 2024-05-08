import re

class Tokenize:
    def __init__(self, bool_expr):
        self.bool_expr = bool_expr
        self.token_patterns = [
            {"pattern": r'\+', "type": "operator", "name": "OR"},
            {"pattern": r'\*', "type": "operator", "name": "AND"},
            {"pattern": r'!', "type": "operator", "name": "NOT"},
            {"pattern": r'\(', "type": "delimiter", "name": "l_parenthesis"},
            {"pattern": r'\)', "type": "delimiter", "name": "r_parenthesis"},
            {"pattern": r'\s+', "type": "delimiter", "name": "whitespace"},
            {"pattern": r'[a-zA-Z]+', "type": "operand", "name": "operand"},
            {"pattern": r'1', "type": "constant", "name": "1"},
            {"pattern": r'0', "type": "constant", "name": "0"}
        ]
        self.accepted_symbols = ['+', '*', '!', '(', ')', '1', '0']
        self.tokens = []
        
    def __repr__(self) -> str:
        return str(self.tokens)
        
    def tokenize(self):
        current_index = 0
        for current_index, char in enumerate(self.bool_expr):
            if char != " " and char not in self.accepted_symbols and not char.isalpha():
                raise ValueError(f"Invalid character: {char}")
            if char != r'\s+':
                for token_pattern in self.token_patterns:
                    pattern = re.compile(token_pattern["pattern"])
                    match = pattern.match(char)
                    if match:
                        token = {
                            "value": match.group(),
                            "type": token_pattern["type"],
                            "name": token_pattern["name"]
                            }
                        self.tokens.append(token)
                    
                current_index += 1
        
        return self.tokens

                    
if __name__ == "__main__":
    expr = "!AB *   C + 1 + 2"
    expr = Tokenize(bool_expr=expr)
    lines = expr.tokenize()

    print(lines)
    
    