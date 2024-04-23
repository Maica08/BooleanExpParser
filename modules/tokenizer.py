import re

class Tokenize:
    def __init__(self, bool_expr):
        self.bool_expr = bool_expr
        self.token_patterns = [
            {"pattern": r'\+', "type": "operator", "name": "OR", "weight": 3},
            {"pattern": r'\*', "type": "operator", "name": "AND", "weight": 2},
            {"pattern": r'!', "type": "operator", "name": "NOT", "weight": 1},
            {"pattern": r'\(', "type": "delimiter", "name": "l_parenthesis", "weight": 0},
            {"pattern": r'\)', "type": "delimiter", "name": "r_parenthesis", "weight": 0},
            {"pattern": r'\s+', "type": "delimiter", "name": "whitespace", "weight": 0},
            {"pattern": r'[a-zA-Z]+', "type": "operand", "name": "operand", "weight": 0}
        ]
        self.tokens = []
        
    def __repr__(self) -> str:
        return str(self.tokens)
        
    def tokenize(self):
        current_index = 0
        for current_index, char in enumerate(self.bool_expr):
            if char != r'\s+':
                match = None
                for token_pattern in self.token_patterns:
                    pattern = re.compile(token_pattern["pattern"])
                    match = pattern.match(char)
                    if match:
                        token = {
                            "value": match.group(),
                            "type": token_pattern["type"],
                            "name": token_pattern["name"],
                            "weight": token_pattern["weight"]
                        }
                        self.tokens.append(token)
                    
                current_index += 1
        
        return self.tokens

                    
if __name__ == "__main__":
    expr = "!AB * C"
    expr = Tokenize(bool_expr=expr)
    lines = expr.tokenize()

    print(lines)