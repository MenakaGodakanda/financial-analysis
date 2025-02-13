# Financial Analysis Chatbot

This project is a simple prototype of an AI chatbot designed to answer predefined financial queries based on analyzed financial data. It serves as an introduction to chatbot development, focusing on basic functionality and interaction.

## Features
- **Predefined Queries**: The chatbot can answer common financial questions, such as:
  - What is Apple revenue trend over the past two years?
  - How has Apple net income changed recently?":
  - What is Microsoft revenue growth trend?":
  - How has Microsoft net income changed in 2024?":
  - What is Tesla revenue growth trend?":
  - How has Tesla net income changed recently?":
  - Which company shows the strongest financial health?":
  - What are the key challenges for Apple and Tesla?":
- **Command-Line Interface**: The chatbot interacts with users via a simple command-line interface.
- **Web Interface**: A Flask-based web app is provided for a more interactive experience.

## Prerequisites
Before running the chatbot, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
```
pip install pandas flask
```

## How to Run the Chatbot
### Command-Line Interface
- Clone the repository or download the `chatbot.py` file.
- Navigate to the project directory in your terminal.
- Run the chatbot:
```
python chatbot.py
```

- Enter one of the predefined queries when prompted. Type exit to quit.


### Web Interface (Flask)
- Clone the repository or download the app.py file.
- Navigate to the project directory in your terminal.
- Run the Flask app:
```
python app.py
```

- Open your browser or a tool like Postman and send a POST request to `http://127.0.0.1:5000/chatbot` with a JSON payload:
```

```

- The chatbot will return a JSON response with the answer.

## Project Structure
```
financial-chatbot/
│
├── chatbot.py              # Command-line chatbot script
├── app.py                  # Flask web app for the chatbot
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
