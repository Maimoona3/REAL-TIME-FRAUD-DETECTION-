🚀 **Real-Time Fraud Detection System**

A Real-Time Fraud Detection System built with FastAPI that detects suspicious transactions using rule-based logic and machine learning.
Includes authentication, logging, and a dashboard for monitoring transactions.

📌 **Features**
🔍 Real-time fraud detection
🤖 Machine Learning (Isolation Forest)
📊 Transaction history dashboard
🔐 JWT Authentication
🧾 Logging system for audit tracking
⚡ FastAPI high-performance backend


🛠️ **Tech Stack**
Backend: Python, FastAPI
Database: SQLite, SQLAlchemy
ML Model: Scikit-learn (Isolation Forest)
Frontend: HTML, CSS, JavaScript
Auth: JWT
Server: Uvicorn


**Project Structure**

Frauddetection/
│
├── App/
│   ├── main.py
│   ├── database.py
│   ├── model.py
│   ├── schemas.py
│   ├── rules.py
│   ├── ml.py
│   ├── utils.py
│   ├── logging_config.py
│   ├── auth.py
│   ├── fraud_system.log
│   │
│   └── static/
│       └── dashboard.html


**⚙️ Installation & Setup**
1. Clone the repository
git clone https://github.com/Maimoona3/REAL-TIME-FRAUD-DETECTION-
cd fraud-detection/App
2. Install dependencies
pip install fastapi uvicorn sqlalchemy scikit-learn python-jose
3. Run the server
python -m uvicorn main:app --reload
4. Open in browser
API Docs:
http://127.0.0.1:8000/docs
Dashboard:
Open static/dashboard.html
🔑 Login Credentials
Username: admin
Password: admin123
🧪 Sample Test Data
{
  "user_id": 101,
  "amount": 75000,
  "location": "Mumbai",
  "device": "Mobile"
}


**📊 API Endpoints**
Method	Endpoint	Description
POST	/login	User authentication
POST	/transaction	Detect fraud
GET	/transactions	Transaction history


**User sends transaction**
Rule engine evaluates risk
ML model predicts anomaly
Risk score is calculated
Transaction is approved or blocked
Data is stored and logged

**📈 Future Enhancements**
📧 Email alerts for fraud
📊 Advanced analytics dashboard
☁️ Cloud deployment
👥 Role-based access control


👨‍💻 Author
**MAI MOONA FATHIMA**

⭐ Support
If you like this project, give it a ⭐ on GitHub!
