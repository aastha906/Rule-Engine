import re

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value
    def to_dict(self):
        """Convert the Node to a dictionary."""
        return {
            'type': self.type,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
            'value': self.value
        }

    @staticmethod
    def from_dict(data):
        """Create a Node from a dictionary."""
        left = Node.from_dict(data['left']) if data['left'] else None
        right = Node.from_dict(data['right']) if data['right'] else None
        return Node(type=data['type'], left=left, right=right, value=data['value'])

def tokenize(rule_string):
    # Tokenizing the rule string
    tokens = re.findall(r'\w+|[()><=]|AND|OR', rule_string)
    return tokens

def parse_expression(index):
    token = tokens[index]

    if token == '(':
        # Parse the expression within the parentheses
        left, next_index = parse_expression(index + 1)
        operator = tokens[next_index]  # This should be the operator
        right, next_index = parse_expression(next_index + 1)  # Parse the right side
        if tokens[next_index] != ')':
            raise SyntaxError("Expected closing parenthesis")
        # Return a node for the expression
        return Node(type="operator", left=left, right=right, value=operator), next_index + 1

    elif token.isidentifier():  # Check if it's an identifier (like 'age')
        # Handle operand (e.g., 'age > 30')
        next_index = index + 1
        operator = tokens[next_index]  # This should be the operator (>, <, =, etc.)
        value = tokens[next_index + 1]  # Get the value (e.g., '30')
        # Return a node for the operand
        return Node(type="operand", left=Node("identifier", value=token), right=Node("value", value=value)), next_index + 2

    elif token in ('AND', 'OR'):
        # Handle logical operators, but they should only appear between expressions
        raise SyntaxError(f"Unexpected logical operator: {token}")

    else:
        raise SyntaxError(f"Unexpected token: {token}")

def parse_tokens(tokens):
    return parse_expression(0)

def create_rule(rule_string):
    global tokens  # Use global variable to access tokens in parsing functions
    tokens = tokenize(rule_string)
    ast, _ = parse_tokens(tokens)
    return ast

def combine_rules(rule_strings):
    asts = [create_rule(rule) for rule in rule_strings]
    
    # Combine using OR operator for simplicity
    combined_ast = asts[0]  # Start with the first rule
    
    for ast in asts[1:]:
        combined_ast = Node(type="operator", left=combined_ast, right=ast, value="OR")

    return combined_ast

def evaluate_rule(ast, data):
    if ast.type == "operand":
        identifier_value = data.get(ast.left.value)
        if ast.right.value.isdigit():
            comparison_value = int(ast.right.value)
        else:
            comparison_value = ast.right.value
        
        # Perform the comparison
        if isinstance(comparison_value, int):
            if ast.left.value == "age":  # Adjust according to your attribute names
                return identifier_value > comparison_value
        # Add more comparisons based on your attributes and logic
        return False

    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    
    return False
