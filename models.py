import sqlite3
import json
from evaluate import Node  # Ensure this import is present

class Rules:
    def __init__(self):
        self.conn = sqlite3.connect('rules.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_text TEXT,
            rule_ast TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def save_rule(self, rule_text, rule_ast):
        query = "INSERT INTO rules (rule_text, rule_ast) VALUES (?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (rule_text, json.dumps(rule_ast.to_dict())))  # Use json.dumps for serialization
        self.conn.commit()
        return cursor.lastrowid

    def get_rule_ast(self, rule_id):
        result = self.database.query("SELECT rule_ast FROM rules WHERE id = ?", (rule_id,))
        if result:
            # Ensure result[0] is not empty or malformed
            if result[0]:
                try:
                    return Node.from_dict(json.loads(result[0]))  # Convert JSON back to Node
                except json.JSONDecodeError as e:
                    print(f"JSON decode error for rule_id {rule_id}: {e}")
            else:
                print(f"No AST found for rule_id: {rule_id}")
        else:
            print(f"No result found for rule_id: {rule_id}")
        return None
