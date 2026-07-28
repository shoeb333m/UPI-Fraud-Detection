# UPI Fraud Detection System

A web-based Machine Learning application developed using Python and Django to detect fraudulent UPI transactions. Users can update the test dataset with transaction details and generate fraud predictions using a trained machine learning model.

## Features

- Detects fraudulent UPI transactions using Machine Learning
- User-friendly web interface
- Predicts fraud from transaction records
- Supports testing with custom transaction data by updating `testData.csv`
- Data preprocessing and feature encoding
- Fast and accurate prediction results

## Technologies Used

- Python
- Django
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS
- SQLite

## Project Structure

```
UPI-Fraud-Detection/
│
├── Dataset/
│   └── testData.csv
├── Fraud/
├── FraudApp/
├── model/
├── manage.py
├── train_model.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shoeb333m/UPI-Fraud-Detection.git
```

### 2. Move to the project directory

```bash
cd UPI-Fraud-Detection
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Django server

```bash
python manage.py runserver
```

### 5. Open your browser

```
http://127.0.0.1:8000
```

## How to Use

1. Start the Django server.
2. Open the application in your browser.
3. Update the transaction records in `Dataset/testData.csv`.
4. Run the prediction through the application.
5. View whether the transactions are classified as **Fraudulent** or **Legitimate**.

## Future Improvements

- Support direct CSV upload from the web interface.
- Improve prediction accuracy with advanced ML models.
- Deploy the application to the cloud.
- Add user authentication.
- Real-time fraud monitoring.

## Author

**Shoeb Khan**

- GitHub: https://github.com/shoeb333m
- LinkedIn: https://www.linkedin.com/in/shoebkhan93
