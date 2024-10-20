# Rule Engine with Abstract Syntax Tree (AST)

This project implements a simple Rule Engine that evaluates user eligibility based on attributes such as age, department, and income using an Abstract Syntax Tree (AST). It provides a RESTful API to evaluate rules defined in a JSON format.

## Features

- Define rules using a structured AST.
- Evaluate rules against user data.
- RESTful API for rule evaluation.
- Easy integration and extension.

## Technology Stack

- Python 3.12
- Flask for the web framework
- SQLite for the database (or any other database of your choice)
- JSON for data interchange

## Prerequisites

Make sure you have the following installed:

- Python 3.12 or higher
- Flask
- Any required database adapter (if using a database)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aastha906/rule-engine.git
   cd rule-engine
   ```

2. **Install the required packages**:
   You can use `pip` to install the necessary dependencies. Create a virtual environment for better isolation (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install Flask
   ```

3. **Database Setup**:
   If you're using SQLite, make sure to set up the database as required. You might need to create a table for storing rules and user attributes.

4. **Run the Application**:
   Start the Flask application:
   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### POST /evaluate_rule

Evaluates a rule based on the provided user data.

#### Request Body

```json
{
  "rule_id": 1,
  "data": {
    "age": 20
  }
}
```

- `rule_id`: The ID of the rule to evaluate.
- `data`: A JSON object containing user attributes.

#### Example Rule Strings

Here are examples of different rule strings you can use for testing:

1. **Rule for Age Eligibility**:
   - **Description**: Evaluates if a user is above a certain age.
   - **Rule String**:
     ```json
     {
       "type": "operator",
       "value": ">",
       "left": {
         "type": "attribute",
         "value": "age"
       },
       "right": {
         "type": "constant",
         "value": 18
       }
     }
     ```

   - **Sample Request**:
     ```json
     {
       "rule_id": 1,
       "data": {
         "age": 20
       }
     }
     ```
   - **Expected Response**:
     ```json
     {
       "result": true
     }
     ```

2. **Rule for Department Membership**:
   - **Description**: Checks if a user belongs to a specific department.
   - **Rule String**:
     ```json
     {
       "type": "operator",
       "value": "==",
       "left": {
         "type": "attribute",
         "value": "department"
       },
       "right": {
         "type": "constant",
         "value": "Sales"
       }
     }
     ```

   - **Sample Request**:
     ```json
     {
       "rule_id": 2,
       "data": {
         "department": "Sales"
       }
     }
     ```
   - **Expected Response**:
     ```json
     {
       "result": true
     }
     ```

3. **Rule for Income Requirement**:
   - **Description**: Evaluates if a user's income exceeds a threshold.
   - **Rule String**:
     ```json
     {
       "type": "operator",
       "value": ">=",
       "left": {
         "type": "attribute",
         "value": "income"
       },
       "right": {
         "type": "constant",
         "value": 50000
       }
     }
     ```

   - **Sample Request**:
     ```json
     {
       "rule_id": 3,
       "data": {
         "income": 60000
       }
     }
     ```
   - **Expected Response**:
     ```json
     {
       "result": true
     }
     ```

## Testing

You can test the API using tools like Postman or directly from your frontend application by sending POST requests with the appropriate request body as shown in the examples above.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### How to Use the `README.md`

1. **Replace Placeholder Text**: Ensure that the repository link and other specific information about your project are accurate.

2. **Add Additional Sections**: You can expand on sections like "Contributing" or "License" as necessary.

3. **Formatting**: Save this content in a file named `README.md` to maintain the markdown formatting.

This detailed `README.md` provides users with comprehensive information on how to use your rule engine, including examples for each rule type. Let me know if you need any changes or additional information!
