from r_ast import Node

def combine_rules(rules):
    combined_rule = None
    for rule in rules:
        if combined_rule:
            combined_rule = Node("operator", left=combined_rule, right=rule, value="AND")
        else:
            combined_rule = rule
    return combined_rule
