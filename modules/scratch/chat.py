def evaluate(expression) -> str:
    char_set = [exp.strip() for exp in expression]
    modified_chars = []
    skip_next = False

    for index, char in enumerate(char_set):
        if skip_next:
            skip_next = False
            continue
        
        if index < len(char_set) - 1:
            if char.isalpha() or char.isnumeric():
                if char_set[index + 1].isnumeric():
                    modified_chars.extend([char, '*', char_set[index + 1]])
                    skip_next = True
                else:
                    modified_chars.append(char)
            elif char == "(":
                modified_chars.append(char)
            elif char == ")":
                if char_set[index + 1].isalpha() or char_set[index + 1].isnumeric() or char_set[index + 1] == "(":
                    modified_chars.extend(['*', char])
                    skip_next = True
            else:
                modified_chars.append(char)

    result = ''.join(modified_chars)
    expression = result
    return result
# print(evaluate("1A"))

print(0 or 1)