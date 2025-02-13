from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_chatbot(user_query):
    if user_query == "What is Apple’s revenue trend over the past two years?":
        return "Apple’s revenue declined by 2.8% in 2023 but recovered slightly with a 2.02% increase in 2024."
    elif user_query == "How has Apple’s net income changed recently?":
        return "Apple’s net income decreased by 2.81% in 2023 and further declined by 3.36% in 2024, indicating rising expenses or lower profit margins."
    elif user_query == "What is Microsoft’s revenue growth trend?":
        return "Microsoft’s revenue grew by 6.88% in 2023 and surged by 15.67% in 2024, reflecting strong market performance."
    elif user_query == "How has Microsoft’s net income changed in 2024?":
        return "Microsoft’s net income jumped by 21.80% in 2024, suggesting better cost management or revenue streams."
    elif user_query == "What is Tesla’s revenue growth trend?":
        return "Tesla’s revenue grew by 18.79% in 2023 but slowed significantly to 0.95% in 2024, indicating potential market saturation or production challenges."
    elif user_query == "How has Tesla’s net income changed recently?":
        return "Tesla’s net income declined sharply by 52.23% in 2024, despite revenue growth, suggesting rising costs or shrinking margins."
    elif user_query == "Which company shows the strongest financial health?":
        return "Microsoft shows the strongest financial health with consistent revenue growth, rising profitability, and strong cash flow."
    elif user_query == "What are the key challenges for Apple and Tesla?":
        return "Apple faces declining net income and cash flow issues, while Tesla struggles with high volatility, slowing revenue growth, and declining profitability."
    else:
        return "Sorry, I can only provide information on predefined queries."

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("query")
    response = simple_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
