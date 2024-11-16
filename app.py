from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'choco_house.db'

def query_db(query, args=(), one=False):
    """Helper function to interact with the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    return "Welcome to Chocolate House API!"

@app.route('/flavours', methods=['GET', 'POST'])
def flavours():
    if request.method == 'GET':
        flavours = query_db("SELECT * FROM seasonal_flavours")
        return jsonify(flavours)
    elif request.method == 'POST':
        data = request.json
        query_db(
            "INSERT INTO seasonal_flavours (flavor_name, available_until, description) VALUES (?, ?, ?)",
            (data['flavor_name'], data['available_until'], data['description']),
        )
        return jsonify({"message": "Flavor added successfully!"})

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'GET':
        ingredients = query_db("SELECT * FROM ingredient_inventory")
        return jsonify(ingredients)
    elif request.method == 'POST':
        data = request.json
        query_db(
            "INSERT INTO ingredient_inventory (ingredient_name, stock_quantity, description) VALUES (?, ?, ?)",
            (data['ingredient_name'], data['stock_quantity'], data['description']),
        )
        return jsonify({"message": "Ingredient added successfully!"})

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'GET':
        suggestions = query_db("SELECT * FROM customer_suggestions")
        return jsonify(suggestions)
    elif request.method == 'POST':
        data = request.json
        query_db(
            "INSERT INTO customer_suggestions (name, email, suggestion, allergy_concerns) VALUES (?, ?, ?, ?)",
            (data['name'], data['email'], data['suggestion'], data['allergy_concerns']),
        )
        return jsonify({"message": "Suggestion submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

