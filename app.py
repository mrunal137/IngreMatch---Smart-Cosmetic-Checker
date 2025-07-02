from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app, resources={r"/*": {"origins": "*"}})

# Load and normalize CSV column names
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'cosmetics.csv'))
df.columns = df.columns.str.strip().str.lower()  # Normalize headers to lowercase

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_product', methods=['POST'])
def check_product():
    data = request.get_json()
    product_name = data.get('product_name', '').strip().lower()

    matched = df[df['name'].str.lower() == product_name]

    if not matched.empty:
        product = matched.iloc[0]

        return jsonify({
            "available": True,
            "product_name": str(product["name"]),
            "label": str(product.get("label", "N/A")),
            "price": str(product.get("price", "N/A")),
            "ingredients": str(product.get("ingredients", "N/A")),
            "skin_types": {
                "Oily": "Yes" if int(product.get("oily", 0)) == 1 else "No",
                "Dry": "Yes" if int(product.get("dry", 0)) == 1 else "No",
                "Sensitive": "Yes" if int(product.get("sensitive", 0)) == 1 else "No",
                "Normal": "Yes" if int(product.get("normal", 0)) == 1 else "No",
                "Combination": "Yes" if int(product.get("combination", 0)) == 1 else "No"
            }

        })
    else:
        return jsonify({"available": False})

if __name__ == '__main__':
    app.run(debug=True, port=5001)