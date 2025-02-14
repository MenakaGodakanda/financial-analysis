# AI-Powered Financial Data Analysis

This project involves extracting, analyzing, and visualizing financial data from Microsoft, Tesla, and Apple based on their SEC 10-K filings. The analysis focuses on key financial metrics over the last three fiscal years, including Total Revenue, Net Income, Total Assets, Total Liabilities and Cash Flow from Operating Activities. Using Python (pandas, matplotlib) in a Jupyter Notebook, identify trends, calculate year-over-year (YoY) growth, and summarize insights that could be useful for developing an AI-powered financial chatbot. Then, this project designed a simple prototype of an AI chatbot to answer predefined financial queries based on analyzed financial data. It serves as an introduction to chatbot development, focusing on basic functionality and interaction.

## Overview

<img width="1271" alt="Screenshot 2025-02-14 at 1 00 58 pm" src="https://github.com/user-attachments/assets/85df9af9-720b-4c65-b213-924b780ba506" />

### Explanation

#### 1. Data Extraction:
- The process starts with extracting financial data (e.g., Total Revenue, Net Income) from the SEC EDGAR database (10-K filings for Microsoft, Tesla, and Apple).
- The extracted data is organized into a `financial_data.csv` file.

#### 2. Data Preprocessing:
- Sort by Company & Year
- Convert data types if needed

#### 4. Financial Data Analysis:
- The cleaned data is loaded into a Jupyter Notebook for analysis.
- Calculating growth rates (e.g., Revenue Growth, Net Income Growth).
- Visualizing trends using libraries like Matplotlib.
- Generating insights from the data.
- The analysis produces insights (e.g., trends, comparisons) and visualizations (e.g., line plots, bar charts) and saves them into `analysis.html`.

#### 5. AI-Powered Financial Chatbot:
- The insights are integrated into a financial chatbot.
- Provide insights to users.
- Answer financial queries.

## Getting Started

### 1. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/financial-analysis.git
cd financial-analysis
```

### 2. Set up a virtual environment:
```
python3 -m venv financial
source financial/bin/activate
```

### 3. Install Dependencies
First, install the required Python packages:
```
pip install pandas matplotlib notebook flask
```

### 4. Run Jupyter Notebook
Start Jupyter Notebook and open `analysis.ipynb`:
```
jupyter notebook
```

## Financial Analysis Breakdown

### 1. Data Extraction & Preparation
- Extracted financial data from 10-K filings.
- Stored the data in `financial_data.csv` for easy access.
- Loaded the dataset using pandas.

### 2. Print column names to verify
- The column name of the CSV file shold be exactly match with what you are referencing in the code.
- Use the following code to print all column names in your DataFrame:
```
import pandas as pd
df = pd.read_csv('./data/financial_data.csv')
print(df.columns)
```
![Screenshot 2025-02-14 214443](https://github.com/user-attachments/assets/880e58eb-145a-40c8-bb6f-4a0715ddc367)

### 3. Convert Financial Figures to Numeric
- In the dataset, financial figures can be stored as strings (likely due to commas in the numbers). 
- Clean the data by converting these columns into numeric format and then proceed with the analysis.
```
import pandas as pd
df = pd.read_csv('./data/financial_data.csv')

# Convert financial figures to numeric
df.replace(',', '', regex=True, inplace=True)
df.iloc[:, 2:] = df.iloc[:, 2:].astype(int)
```

### 4. Year-over-Year Growth Calculation
- Calculated the YoY growth for each financial metric:
  - **Calculates YoY revenue growth**: Computes the year-over-year revenue growth for each company.
  - **Calculates YoY net income growth**: Computes the percentage change in net income from the previous year.
  - **Calculates YoY assets growth**: Computes the year-over-year percentage change in total assets.
  - **Calculates YoY liabilities growth**: Computes the year-over-year percentage change in total liabilities. Indicates whether a company is increasing or decreasing its debt over time.
  - **Calculates YoY cash flow growth**: Computes the percentage change in cash flow from operations (CFO). CFO indicates how much cash a company generates from core business operations.
```
# Calculate YoY Growth
df.sort_values(by=['Company', 'Year'], inplace=True)
df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue (in millions)'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income (in millions)'].pct_change() * 100
df['Assets Growth (%)'] = df.groupby('Company')['Total Assets (in millions)'].pct_change() * 100
df['Liabilities Growth (%)'] = df.groupby('Company')['Total Liabilities (in millions)'].pct_change() * 100
df['Cash Flow Growth (%)'] = df.groupby('Company')['Cash Flow from Operating Activities (in millions)'].pct_change() * 100

print(df)
```
![Screenshot 2025-02-13 225846](https://github.com/user-attachments/assets/d9ff729b-ad67-4454-be01-3319d5907c2d)
![Screenshot 2025-02-13 225852](https://github.com/user-attachments/assets/d5f48b09-2229-45f4-8516-ad39c20d1753)

#### Key Notes
- **NaN Values**: The first year for each company will have NaN values for the growth rates because there is no previous year to compare to.
- **Units**: Ensure that the units (in millions) are consistent throughout your analysis. If needed, you can convert the values to billions by dividing by 1,000.

### 5. Data Visualization
- Visualized Revenue Growth Trends using matplotlib:
```
import matplotlib.pyplot as plt

# Visualize Revenue Growth
plt.figure(figsize=(10,5))
for company in df['Company'].unique():
    subset = df[df['Company'] == company]
    plt.plot(subset['Year'], subset['Revenue Growth (%)'], marker='o', label=company)
plt.xlabel('Year')
plt.ylabel('Revenue Growth (%)')
plt.title('Year-over-Year Revenue Growth')
plt.legend()
plt.grid(True)
plt.show()
```
![Screenshot 2025-02-14 214605](https://github.com/user-attachments/assets/4321f9db-d90a-482d-901d-8bdc18f4dfd7)

### 6. Average Growth Rate Calculation
- Computed the average growth rate for each financial metric:
```
# Calculate average growth rates
avg_growth = df.groupby('Company')[['Revenue Growth (%)', 'Net Income Growth (%)', 'Assets Growth (%)', 'Liabilities Growth (%)', 'Cash Flow Growth (%)']].mean()
print(avg_growth)
```
![Screenshot 2025-02-13 225943](https://github.com/user-attachments/assets/ba79c37a-d003-4d02-8c40-89d8d434806d)

## Financial Analysis Chatbot
### Features 
- **Predefined Queries**: The chatbot can answer 3–5 common financial questions, such as:
  - "What is Apple’s revenue trend over the past two years?"
  - "What is Microsoft’s revenue growth trend?"
  - "What is Tesla’s revenue growth trend?"
  - "Which company shows the strongest financial health?"
- **Command-Line Interface**: The chatbot interacts with users via a simple command-line interface.
- **Web Interface**: A Flask-based web app is provided for a more interactive experience.

### Command-Line Interface
- Navigate to the project directory in your terminal.
- Run the chatbot:
```
python chatbot.py
```
- Enter one of the predefined queries when prompted. Type `exit` to quit.
![Screenshot 2025-02-13 230322](https://github.com/user-attachments/assets/2a743269-fa08-41a7-ae60-65b90757e1c3)
![Screenshot 2025-02-13 230328](https://github.com/user-attachments/assets/56ef4653-e5d1-4136-8c1c-94f88ed0dbb6)
![Screenshot 2025-02-13 230352](https://github.com/user-attachments/assets/b5b50507-d8c8-4b04-ace1-3a25e50a633b)

### Web Interface (Flask)
- Navigate to the project directory in your terminal.
- Run the Flask app:
```
python app.py
```
![Screenshot 2025-02-13 231759](https://github.com/user-attachments/assets/bce368bc-6159-4fb2-9ef7-0cb5afaf79d5)
![Screenshot 2025-02-13 230925](https://github.com/user-attachments/assets/0dece177-0add-4fb0-bcd4-46b05e553fc1)

- Open your browser or a tool like Postman and send a POST request to `http://127.0.0.1:5000/chatbot` with a JSON payload.
- Open a new terminal window and use the following `curl` command to send a POST request to the `/chatbot` endpoints:
```
curl -X POST http://127.0.0.1:5000/chatbot \
-H "Content-Type: application/json" \
-d '{"query": "What is Apple’s revenue trend over the past two years?"}'
```
- The chatbot will return a JSON response with the answer.
![Screenshot 2025-02-13 232146](https://github.com/user-attachments/assets/942c19e1-e56f-494b-b65d-8737f751ac2e)
![Screenshot 2025-02-13 232150](https://github.com/user-attachments/assets/0c382d90-6dd9-4dff-9a99-6fa069a350c3)

#### Key Notes
- The apostrophe (’) removed from the the queries and responses because JSON responses prints out apostrophe (’) as `\u2019` which is simply a Unicode representation of the apostrophe (’).

## Project Structure
```
financial-analysis/
├── financial-chatbot/
│   ├── chatbot.py              # Command-line chatbot script
│   ├── app.py                  # Flask web app for the chatbot
│   └── README.md               # Project documentation for chatbot
├── data/                       
│   └── financial_data.csv      # Extracted financial data from SEC filings
│── analysis.ipynb              # Jupyter Notebook containing the analysis
│── analysis.html               # Jupyter Notebook output
└── README.md                   # Project documentation
```

## License
This project is licensed under the MIT License.
