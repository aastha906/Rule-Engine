import re
from typing import Optional, Dict, Any

class Node:
    def __init__(self, type: str, left: Optional['Node'] = None, right: Optional['Node'] = None, value: Optional[str] = None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary for serialization."""
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Node':
        """Create a Node from a dictionary."""
        left = cls.from_dict(data["left"]) if data["left"] else None
        right = cls.from_dict(data["right"]) if data["right"] else None
        return cls(type=data["type"], left=left, right=right, value=data.get("value"))

def evaluate_node(node, data):
    if node is None:
        print("Received None node for evaluation.")
        return False  # or handle the case accordingly

    if node.type == "operator":
        left_value = evaluate_node(node.left, data)
        right_value = evaluate_node(node.right, data)
        if node.value == "AND":
            return left_value and right_value
        elif node.value == "OR":
            return left_value or right_value
    elif node.type == "operand":
        return eval_condition(node)

    return False


def eval_condition(node: Node, data: Dict[str, Any]) -> bool:
    """Evaluate a condition based on the left and right nodes."""
    left_val = data.get(node.left.value.strip())
    right_val = int(node.right.value.strip())

    if left_val is None:
        raise ValueError(f"Variable '{node.left.value.strip()}' not found in data.")
    
    if node.value == '>':
        return left_val > right_val
    elif node.value == '<':
        return left_val < right_val
    elif node.value == '=':
        return left_val == right_val
    
    raise ValueError(f"Unsupported operator: {node.value}")

def evaluate_rule(ast, data):
    """Evaluate the rule represented by the AST against the provided data."""
    if ast is None:
        print("AST is None. Cannot evaluate rule.")
        return False  # or handle the error as needed
    
    return evaluate_node(ast, data)
