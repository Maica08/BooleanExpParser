def find_leaf_nodes(expression):
    leaf_nodes = []

    def traverse(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if isinstance(value, list):
                    if dict in [type(x) for x in value]:
                        for operand in value:
                            if isinstance(operand, dict):
                                traverse(operand)
                    
                    else:
                        leaf_nodes.append(node)
                else:
                    traverse(value)

    traverse(expression)
    return leaf_nodes

def tree_height(expression):
    if isinstance(expression, dict):
        max_height = 0
        for key, value in expression.items():
            if isinstance(value, list):
                height = 1 + max(tree_height(operand) for operand in value)
            else:
                height = 1 + tree_height(value)
            max_height = max(max_height, height)
        return max_height
    else:
        return 0

# Example usage
expression = {'+': [{'*': ['A', 'B']}, {'*': ['A', {'+': ['C', 'D']}]}]}
height = tree_height(expression)
print("Tree Height:", height)


# Example usage
expression = {'+': [{'*': ['A', 'B']}, {'*': ['A', {'+': ['C', 'D']}]}]}
leaf_nodes = find_leaf_nodes(expression)
print("Leaf Nodes:", leaf_nodes)

