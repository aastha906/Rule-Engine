from flask import Flask, request, jsonify
from r_ast import create_rule
from combine import combine_rules
from evaluate import evaluate_rule
from models import Rules

app = Flask(__name__)

# Initialize the database model
rules_db = Rules()

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get("rule_string")
    ast = create_rule(rule_string)
    rule_id = rules_db.save_rule(rule_string, ast)
    return jsonify({"rule_id": rule_id, "ast": str(ast)})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    data = request.json
    rule_strings = data.get("rule_strings", [])
    
    if not rule_strings:  # Handle empty list or None case
        return jsonify({"error": "No rules provided"}), 400

    combined_ast = combine_rules(rule_strings)
    return jsonify({"combined_ast": str(combined_ast)})  # Ensure appropriate representation


@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')

    ast = rules_db.get_rule_ast(rule_id)
    if ast is None:
        print(f"Error: No AST found for rule_id: {rule_id}")
        return jsonify({"error": "Rule not found"}), 404

    result = evaluate_rule(ast, data)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
