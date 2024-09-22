from flask import Flask, render_template, request, jsonify
from server import getResponse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json

    if not data:
        return jsonify({"error": "No data received"}), 400

    user_input = data.get('input')
    if not user_input or user_input.strip() == "":
        return jsonify({"error": "User input is required"}), 400

    restrictions = data.get('restrictions', [])
    allergens = data.get('allergens', [])
    budget = '£' + data.get('budget', [])
    goals = data.get('goals')
    cuisines = data.get('cuisines')

    if len(restrictions) == 0:
        restrictions.append("None")
    if len(allergens) == 0:
        allergens.append("None")
    if len(goals) == 0:
        goals.append("None")

    if len(cuisines) == 0:
        cuisines.append("None")
    if budget == "£None":
        budget = ""

    print("User input:", user_input)
    print("Selected Restrictions:", restrictions)
    print("Selected Allergens:", allergens)
    print("Selected Budget:", budget)
    print("Selected Goals:", goals)
    print("Selected Cuisines:", budget)

    try:
        response = getResponse(user_input, restrictions, allergens, budget, goals, cuisines)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
