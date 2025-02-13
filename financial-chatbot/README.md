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

- Enter one of the predefined queries when prompted:
![Screenshot 2025-02-13 230322](https://github.com/user-attachments/assets/a5ef732d-31c0-44a3-bd91-67b3cc51d2fb)

- Enter querie that is not predefined when prompted:
![Screenshot 2025-02-13 230328](https://github.com/user-attachments/assets/d3d2c452-b33e-438d-aa8b-64dbe5d62c8e)

- Type exit to quit.
![Screenshot 2025-02-13 230352](https://github.com/user-attachments/assets/08463609-bd1d-4a3a-abde-3e4a73c2bc37)

### Web Interface (Flask)
- Clone the repository or download the app.py file.
- Navigate to the project directory in your terminal.
- Run the Flask app:
```
python app.py
```
![Screenshot 2025-02-13 231759](https://github.com/user-attachments/assets/36d117cd-23a7-4c52-ba70-1d9d8ed51307)

- Browse `http://127.0.0.1:5000`.
![Screenshot 2025-02-13 230925](https://github.com/user-attachments/assets/2298ebf9-869f-46c0-8465-c5face68b921)

- Open your browser or a tool like Postman and send a POST request to `http://127.0.0.1:5000/chatbot` with a JSON payload.
- Enter one of the predefined queries:
![Screenshot 2025-02-13 232146](https://github.com/user-attachments/assets/caee64ce-f46b-43c8-bdc4-95c5d8a7a857)

- Enter querie that is not predefined:
![Screenshot 2025-02-13 232150](https://github.com/user-attachments/assets/c640829a-71c8-45f9-8ac4-dba8cc644ef7)

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
